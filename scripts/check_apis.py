#!/usr/bin/env python3
"""
Public API 可用性检测工具
并发检测API链接可用性，生成检测报告
"""

import asyncio
import argparse
import json
import csv
import time
import logging
from pathlib import Path
from typing import List, Dict, Optional, Any, Tuple
from datetime import datetime, timedelta
import aiohttp
from aiohttp import ClientTimeout, ClientError
import hashlib
from functools import wraps


__version__ = "1.0.0"

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("api_checker.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class Cache:
    """本地缓存实现，支持TTL过期"""
    def __init__(self, ttl: int = 3600):
        self.ttl = ttl  # 缓存过期时间（秒）
        self.cache: Dict[str, Tuple[Any, float]] = {}
        
    def get(self, key: str) -> Optional[Any]:
        """从缓存获取数据"""
        if key not in self.cache:
            return None
            
        value, timestamp = self.cache[key]
        # 检查缓存是否过期
        if time.time() - timestamp > self.ttl:
            del self.cache[key]
            return None
            
        return value
    
    def set(self, key: str, value: Any) -> None:
        """设置缓存"""
        self.cache[key] = (value, time.time())
    
    def clear(self) -> None:
        """清空缓存"""
        self.cache.clear()


def generate_api_hash(api_info: Dict[str, Any]) -> str:
    """生成API信息的哈希值作为缓存键"""
    hash_input = f"{api_info.get('name', '')}:{api_info.get('link', '')}"
    return hashlib.md5(hash_input.encode('utf-8')).hexdigest()


class APIReader:
    """API列表读取器，支持JSON和CSV格式"""
    
    @staticmethod
    def read_json(file_path: str) -> List[Dict[str, Any]]:
        """从JSON文件读取API列表"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data if isinstance(data, list) else [data]
        except Exception as e:
            logger.error(f"读取JSON文件失败: {str(e)}")
            raise
    
    @staticmethod
    def read_csv(file_path: str) -> List[Dict[str, Any]]:
        """从CSV文件读取API列表"""
        try:
            apis = []
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    apis.append(dict(row))
            return apis
        except Exception as e:
            logger.error(f"读取CSV文件失败: {str(e)}")
            raise
    
    @classmethod
    def read(cls, file_path: str) -> List[Dict[str, Any]]:
        """自动识别文件格式并读取"""
        path = Path(file_path)
        if path.suffix.lower() == '.json':
            return cls.read_json(file_path)
        elif path.suffix.lower() == '.csv':
            return cls.read_csv(file_path)
        else:
            raise ValueError(f"不支持的文件格式: {path.suffix}")


class APIWriter:
    """检测结果写入器，支持JSON和CSV格式"""
    
    @staticmethod
    def write_json(data: List[Dict[str, Any]], file_path: str) -> None:
        """将结果写入JSON文件"""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False, default=str)
            logger.info(f"检测结果已写入JSON文件: {file_path}")
        except Exception as e:
            logger.error(f"写入JSON文件失败: {str(e)}")
            raise
    
    @staticmethod
    def write_csv(data: List[Dict[str, Any]], file_path: str) -> None:
        """将结果写入CSV文件"""
        try:
            if not data:
                logger.warning("没有数据可写入CSV文件")
                return
                
            # 获取所有字段
            fieldnames = set()
            for item in data:
                fieldnames.update(item.keys())
            
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=sorted(fieldnames))
                writer.writeheader()
                writer.writerows(data)
            
            logger.info(f"检测结果已写入CSV文件: {file_path}")
        except Exception as e:
            logger.error(f"写入CSV文件失败: {str(e)}")
            raise
    
    @classmethod
    def write(cls, data: List[Dict[str, Any]], file_path: str) -> None:
        """自动识别文件格式并写入"""
        path = Path(file_path)
        if path.suffix.lower() == '.json':
            cls.write_json(data, file_path)
        elif path.suffix.lower() == '.csv':
            cls.write_csv(data, file_path)
        else:
            raise ValueError(f"不支持的文件格式: {path.suffix}")


class APIChecker:
    """API可用性检测核心类"""
    
    def __init__(
        self,
        concurrency: int = 10,
        timeout: int = 10,
        retries: int = 3,
        cache_ttl: int = 3600,
        force_refresh: bool = False
    ):
        self.concurrency = concurrency
        self.timeout = ClientTimeout(total=timeout)
        self.retries = retries
        self.cache = Cache(ttl=cache_ttl)
        self.force_refresh = force_refresh
        self.semaphore = asyncio.Semaphore(concurrency)
        
    async def fetch_api(
        self,
        session: aiohttp.ClientSession,
        api_info: Dict[str, Any]
    ) -> Dict[str, Any]:
        """单个API链接检测"""
        result = api_info.copy()
        result.update({
            'check_time': datetime.now().isoformat(),
            'status': 'pending',
            'response_time_ms': None,
            'error': None
        })
        
        link = api_info.get('link')
        if not link:
            result['status'] = 'error'
            result['error'] = 'Missing API link'
            return result
            
        # 检查缓存
        cache_key = generate_api_hash(api_info)
        if not self.force_refresh:
            cached_result = self.cache.get(cache_key)
            if cached_result:
                logger.debug(f"使用缓存结果: {link}")
                return cached_result
        
        try:
            async with self.semaphore:
                start_time = time.time()
                
                # 带重试机制的请求
                for attempt in range(self.retries + 1):
                    try:
                        async with session.get(link, timeout=self.timeout) as response:
                            response_time = int((time.time() - start_time) * 1000)
                            result.update({
                                'status': 'success',
                                'status_code': response.status,
                                'response_time_ms': response_time
                            })
                            break
                    except ClientError as e:
                        if attempt < self.retries:
                            # 指数退避
                            await asyncio.sleep(2 ** attempt)
                            continue
                        result['status'] = 'error'
                        result['error'] = str(e)
                    except asyncio.TimeoutError:
                        result['status'] = 'timeout'
                        result['error'] = f"Request timed out after {self.timeout.total}s"
                        break
                        
        except Exception as e:
            result['status'] = 'error'
            result['error'] = str(e)
            
        # 缓存结果
        self.cache.set(cache_key, result)
        return result
    
    async def check_apis(self, apis: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """批量检测API"""
        logger.info(f"开始检测 {len(apis)} 个API链接，并发数: {self.concurrency}")
        
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_api(session, api) for api in apis]
            
            # 显示进度
            results = []
            for i, task in enumerate(asyncio.as_completed(tasks), 1):
                result = await task
                results.append(result)
                if i % 10 == 0 or i == len(tasks):
                    logger.info(f"检测进度: {i}/{len(tasks)}")
                    
        logger.info("API检测完成")
        return results


def main() -> None:
    """主函数"""
    parser = argparse.ArgumentParser(
        description="Public API 可用性检测工具",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # 核心参数
    parser.add_argument("--input", required=True, help="输入API列表文件路径 (JSON/CSV格式)")
    parser.add_argument("--output", required=True, help="输出检测报告文件路径 (JSON/CSV格式)")
    
    # 配置参数
    parser.add_argument("--concurrency", type=int, default=10, help="并发请求数")
    parser.add_argument("--timeout", type=int, default=10, help="请求超时时间(秒)")
    parser.add_argument("--retries", type=int, default=3, help="重试次数")
    parser.add_argument("--cache-ttl", type=int, default=3600, help="缓存过期时间(秒)")
    parser.add_argument("--force", action="store_true", help="强制刷新缓存，忽略已有缓存结果")
    
    args = parser.parse_args()
    
    try:
        # 读取API列表
        apis = APIReader.read(args.input)
        logger.info(f"成功读取 {len(apis)} 个API")
        
        # 初始化检测工具
        checker = APIChecker(
            concurrency=args.concurrency,
            timeout=args.timeout,
            retries=args.retries,
            cache_ttl=args.cache_ttl,
            force_refresh=args.force
        )
        
        # 执行检测
        results = asyncio.run(checker.check_apis(apis))
        
        # 生成报告
        APIWriter.write(results, args.output)
        
        # 统计结果
        success_count = sum(1 for r in results if r['status'] == 'success')
        error_count = sum(1 for r in results if r['status'] == 'error')
        timeout_count = sum(1 for r in results if r['status'] == 'timeout')
        
        logger.info(f"=== 检测统计 ===")
        logger.info(f"成功: {success_count} ({success_count/len(results)*100:.1f}%)")
        logger.info(f"错误: {error_count} ({error_count/len(results)*100:.1f}%)")
        logger.info(f"超时: {timeout_count} ({timeout_count/len(results)*100:.1f}%)")
        
    except Exception as e:
        logger.error(f"程序执行失败: {str(e)}", exc_info=True)
        exit(1)


if __name__ == "__main__":
    main()