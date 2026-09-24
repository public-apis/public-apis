import pytest
import tempfile
import os
from api_badger.parser import MarkdownParser, APIEntry
from api_badger.badges import BadgeGenerator
from api_badger.readme_generator import ReadmeGenerator
from api_badger.html_generator import HtmlGenerator
from api_badger.csv_exporter import CsvExporter


class TestMarkdownParser:
    """Test cases for MarkdownParser."""
    
    def test_parse_simple_table(self):
        """Test parsing a simple API table."""
        content = """
### Animals
API | Description | Auth | HTTPS | CORS 
|:---|:---|:---|:---|:---|
| [Cat Facts](https://catfacts.example) | Daily cat facts | No | Yes | No |
| [Dog API](https://dogapi.example) | Dog pictures | apiKey | Yes | Yes |
"""
        parser = MarkdownParser()
        entries = parser.parse_content(content)
        
        assert len(entries) == 2
        assert entries[0].name == "Cat Facts"
        assert entries[0].link == "https://catfacts.example"
        assert entries[0].description == "Daily cat facts"
        assert entries[0].auth == "No"
        assert entries[0].https == "Yes"
        assert entries[0].cors == "No"
        assert entries[0].category == "Animals"
    
    def test_parse_with_missing_fields(self):
        """Test parsing table with missing fields."""
        content = """
### Test
API | Description | Auth | HTTPS | CORS 
|:---|:---|:---|:---|:---|
| [Test API](https://test.example) | Test description | | | |
"""
        parser = MarkdownParser()
        entries = parser.parse_content(content)
        
        assert len(entries) == 1
        assert entries[0].name == "Test API"
        assert entries[0].auth == "No"  # Default value
        assert entries[0].https == "No"  # Default value
        assert entries[0].cors == "No"  # Default value
    
    def test_parse_with_unknown_values(self):
        """Test parsing table with unknown values."""
        content = """
### Test
API | Description | Auth | HTTPS | CORS 
|:---|:---|:---|:---|:---|
| [Test API](https://test.example) | Test description | Unknown | Unknown | Unknown |
"""
        parser = MarkdownParser()
        entries = parser.parse_content(content)
        
        assert len(entries) == 1
        assert entries[0].auth == "Unknown"
        assert entries[0].https == "Unknown"
        assert entries[0].cors == "Unknown"
    
    def test_parse_multiple_categories(self):
        """Test parsing multiple categories."""
        content = """
### Animals
API | Description | Auth | HTTPS | CORS 
|:---|:---|:---|:---|:---|
| [Cat API](https://cat.example) | Cat pictures | No | Yes | No |

### Weather
API | Description | Auth | HTTPS | CORS 
|:---|:---|:---|:---|:---|
| [Weather API](https://weather.example) | Weather data | apiKey | Yes | Yes |
"""
        parser = MarkdownParser()
        entries = parser.parse_content(content)
        
        assert len(entries) == 2
        assert entries[0].category == "Animals"
        assert entries[1].category == "Weather"
    
    def test_parse_empty_content(self):
        """Test parsing empty content."""
        parser = MarkdownParser()
        entries = parser.parse_content("")
        
        assert len(entries) == 0
    
    def test_parse_file_not_found(self):
        """Test parsing non-existent file."""
        parser = MarkdownParser()
        
        with pytest.raises(FileNotFoundError):
            parser.parse_file("non_existent_file.md")


class TestBadgeGenerator:
    """Test cases for BadgeGenerator."""
    
    def test_generate_https_badges(self):
        """Test HTTPS badge generation."""
        generator = BadgeGenerator()
        
        # Test Yes
        entry = APIEntry("Test", "Test", "No", "Yes", "No", "http://test.com", "Test")
        badges = generator.generate_badges(entry)
        assert "https://img.shields.io/badge/HTTPS-Yes-brightgreen" in badges['https']
        
        # Test No
        entry = APIEntry("Test", "Test", "No", "No", "No", "http://test.com", "Test")
        badges = generator.generate_badges(entry)
        assert "https://img.shields.io/badge/HTTPS-No-red" in badges['https']
    
    def test_generate_auth_badges(self):
        """Test Auth badge generation."""
        generator = BadgeGenerator()
        
        # Test No auth
        entry = APIEntry("Test", "Test", "No", "Yes", "No", "http://test.com", "Test")
        badges = generator.generate_badges(entry)
        assert "https://img.shields.io/badge/Auth-No-brightgreen" in badges['auth']
        
        # Test API Key
        entry = APIEntry("Test", "Test", "apiKey", "Yes", "No", "http://test.com", "Test")
        badges = generator.generate_badges(entry)
        assert "https://img.shields.io/badge/Auth-apiKey-yellow" in badges['auth']
        
        # Test OAuth
        entry = APIEntry("Test", "Test", "OAuth", "Yes", "No", "http://test.com", "Test")
        badges = generator.generate_badges(entry)
        assert "https://img.shields.io/badge/Auth-OAuth-blue" in badges['auth']
    
    def test_generate_cors_badges(self):
        """Test CORS badge generation."""
        generator = BadgeGenerator()
        
        # Test Yes
        entry = APIEntry("Test", "Test", "No", "Yes", "Yes", "http://test.com", "Test")
        badges = generator.generate_badges(entry)
        assert "https://img.shields.io/badge/CORS-Yes-brightgreen" in badges['cors']
        
        # Test No
        entry = APIEntry("Test", "Test", "No", "Yes", "No", "http://test.com", "Test")
        badges = generator.generate_badges(entry)
        assert "https://img.shields.io/badge/CORS-No-red" in badges['cors']
    
    def test_generate_all_badges(self):
        """Test generating badges for multiple entries."""
        generator = BadgeGenerator()
        
        entries = [
            APIEntry("API 1", "Desc 1", "No", "Yes", "No", "http://test1.com", "Test"),
            APIEntry("API 2", "Desc 2", "apiKey", "Yes", "Yes", "http://test2.com", "Test")
        ]
        
        results = generator.generate_all_badges(entries)
        assert len(results) == 2
        assert 'badges' in results[0]
        assert 'badges' in results[1]


class TestReadmeGenerator:
    """Test cases for ReadmeGenerator."""
    
    def test_generate_readme_badges(self):
        """Test README generation with badges."""
        entries = [
            APIEntry("Test API", "Test description", "No", "Yes", "No", "http://test.com", "Test Category")
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            temp_path = f.name
        
        try:
            generator = ReadmeGenerator()
            generator.generate_readme_badges(entries, temp_path)
            
            with open(temp_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            assert "# Public APIs with Badges" in content
            assert "Test Category" in content
            assert "Test API" in content
            assert "Test description" in content
            assert "https://img.shields.io/badge/HTTPS-Yes-brightgreen" in content
        finally:
            os.unlink(temp_path)


class TestHtmlGenerator:
    """Test cases for HtmlGenerator."""
    
    def test_generate_html(self):
        """Test HTML generation."""
        entries = [
            APIEntry("Test API", "Test description", "No", "Yes", "No", "http://test.com", "Test Category")
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            temp_path = f.name
        
        try:
            generator = HtmlGenerator()
            generator.generate_html(entries, temp_path)
            
            with open(temp_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            assert "<!DOCTYPE html>" in content
            assert "Test API" in content
            assert "Test description" in content
            assert "https://img.shields.io/badge/HTTPS-Yes-brightgreen" in content
        finally:
            os.unlink(temp_path)


class TestCsvExporter:
    """Test cases for CsvExporter."""
    
    def test_export_to_csv(self):
        """Test CSV export functionality."""
        entries = [
            APIEntry("Test API", "Test description", "No", "Yes", "No", "http://test.com", "Test Category")
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            temp_path = f.name
        
        try:
            exporter = CsvExporter()
            exporter.export_to_csv(entries, temp_path)
            
            with open(temp_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            assert "name,description,auth,https,cors,link,category,https_badge,auth_badge,cors_badge" in content
            assert "Test API" in content
            assert "Test description" in content
            assert "http://test.com" in content
        finally:
            os.unlink(temp_path)