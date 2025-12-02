#!/usr/bin/env python3
"""
API检测工具单元测试
"""

import pytest
import asyncio
import json
from unittest.mock import Mock, patch, MagicMock
from aiohttp import ClientResponse, ClientTimeout
from aiohttp.web import HTTP_OK, HTTP_NOT_FOUND
from pathlib import Path

# 导入被测模块
import sys
sys.path.append(str(Path(__file__).parent.parent))
from check_apis import APIReader, APIWriter, Cache, APIChecker, generate_api_hash


class TestCache:
    """缓存模块测试"""
    
    def test_cache_set_get(self):
        """测试缓存设置与获取"""
        cache = Cache(ttl=3600)
        cache.set('test_key', 'test_value')
        
        assert cache.get('test_key') == 'test_value'
        assert cache.get('non_existent_key') is None
    
    def test_cache_expiration(self):
        """测试缓存过期"""
        cache = Cache(ttl=0.1)
        cache.set('test_key', 'test_value')
        
        # 缓存未过期
        assert cache.get('test_key') == 'test_value'
        
        # 等待缓存过期
        import time
        time.sleep(0.2)
        
        # 缓存已过期
        assert cache.get('test_key') is None


def test_generate_api_hash():
    """测试API哈希生成"""
    api_info = {
        'name': 'Test API',
        'link': 'https://example.com/api'
    }
    
    hash1 = generate_api_hash(api_info)
    hash2 = generate_api_hash(api_info)
    
    # 相同信息生成相同哈希
    assert hash1 == hash2
    
    # 不同信息生成不同哈希
    api_info2 = {
        'name': 'Another API',
        'link': 'https://example.com/api'
    }
    assert generate_api_hash(api_info2) != hash1


class TestAPIReader:
    """API读取器测试"""
    
    def test_read_json(self, tmp_path):
        """测试JSON文件读取"""
        test_data = [
            {'name': 'Test API 1', 'link': 'https://example.com/1'},
            {'name': 'Test API 2', 'link': 'https://example.com/2'}
        ]
        
        json_file = tmp_path / "test_apis.json"
        with open(json_file, 'w') as f:
            json.dump(test_data, f)
        
        apis = APIReader.read_json(str(json_file))
        assert len(apis) == 2
        assert apis[0]['name'] == 'Test API 1'
    
    def test_read_csv(self, tmp_path):
        """测试CSV文件读取"""
        csv_content = "name,link\nTest API 1,https://example.com/1\nTest API 2,https://example.com/2"
        
        csv_file = tmp_path / "test_apis.csv"
        with open(csv_file, 'w') as f:
            f.write(csv_content)
        
        apis = APIReader.read_csv(str(csv_file))
        assert len(apis) == 2
        assert apis[1]['link'] == 'https://example.com/2'


class TestAPIWriter:
    """API结果写入器测试"""
    
    def test_write_json(self, tmp_path):
        """测试JSON文件写入"""
        test_results = [
            {'name': 'Test API', 'link': 'https://example.com', 'status': 'success'}
        ]
        
        json_file = tmp_path / "results.json"
        APIWriter.write_json(test_results, str(json_file))
        
        with open(json_file, 'r') as f:
            data = json.load(f)
        assert len(data) == 1
        assert data[0]['status'] == 'success'


@pytest.mark.asyncio
class TestAPIChecker:
    """API检测核心类测试"""
    
    @patch('aiohttp.ClientSession.get')
    async def test_fetch_api_success(self, mock_get):
        """测试API请求成功场景"""
        # Mock响应
        mock_response = Mock(spec=ClientResponse)
        mock_response.status = 200
        mock_response.__aenter__.return_value = mock_response
        
        mock_get.return_value.__aenter__.return_value = mock_response
        
        checker = APIChecker(timeout=10, retries=3)
        session = Mock()
        session.get = mock_get
        
        api_info = {'name': 'Test API', 'link': 'https://example.com'}
        result = await checker.fetch_api(session, api_info)
        
        assert result['status'] == 'success'
        assert result['status_code'] == 200
        assert result['response_time_ms'] is not None
        
    @patch('aiohttp.ClientSession.get')
    async def test_fetch_api_timeout(self, mock_get):
        """测试API请求超时场景"""
        mock_get.side_effect = asyncio.TimeoutError()
        
        checker = APIChecker(timeout=0.1, retries=0)
        session = Mock()
        session.get = mock_get
        
        api_info = {'name': 'Test API', 'link': 'https://example.com'}
        result = await checker.fetch_api(session, api_info)
        
        assert result['status'] == 'timeout'
        assert 'timed out' in result['error']
    
    @patch('aiohttp.ClientSession.get')
    async def test_fetch_api_failure(self, mock_get):
        """测试API请求失败场景"""
        from aiohttp import ClientError
        mock_get.side_effect = ClientError("Connection refused")
        
        checker = APIChecker(retries=0)
        session = Mock()
        session.get = mock_get
        
        api_info = {'name': 'Test API', 'link': 'https://example.com'}
        result = await checker.fetch_api(session, api_info)
        
        assert result['status'] == 'error'
        assert 'Connection refused' in result['error']
    
    async def test_fetch_api_missing_link(self):
        """测试缺少API链接场景"""
        checker = APIChecker()
        session = Mock()
        
        api_info = {'name': 'Test API'}
        result = await checker.fetch_api(session, api_info)
        
        assert result['status'] == 'error'
        assert 'Missing API link' in result['error']


if __name__ == '__main__':
    pytest.main([__file__])