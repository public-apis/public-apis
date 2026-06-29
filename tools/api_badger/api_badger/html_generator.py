from typing import List, Dict
from jinja2 import Template
from .parser import APIEntry
from .badges import BadgeGenerator


class HtmlGenerator:
    """Generate HTML page for API entries with badges."""
    
    def __init__(self):
        self.badge_generator = BadgeGenerator()
    
    def generate_html(self, entries: List[APIEntry], output_path: str):
        """Generate HTML page for API entries."""
        # Group entries by category
        categories = self._group_by_category(entries)
        
        # Generate badge data for all entries
        category_data = []
        for category_name, category_entries in sorted(categories.items()):
            api_data = []
            for entry in category_entries:
                badges = self.badge_generator.generate_badges(entry)
                api_data.append({
                    'entry': entry,
                    'badges': badges
                })
            category_data.append({
                'name': category_name,
                'apis': api_data
            })
        
        # Generate HTML
        html_content = self._generate_html_template(category_data)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    def _group_by_category(self, entries: List[APIEntry]) -> Dict[str, List[APIEntry]]:
        """Group API entries by category."""
        categories = {}
        for entry in entries:
            category = entry.category or "Uncategorized"
            if category not in categories:
                categories[category] = []
            categories[category].append(entry)
        return categories
    
    def _generate_html_template(self, category_data: List[Dict]) -> str:
        """Generate HTML template with embedded CSS and JavaScript."""
        # Calculate total API count
        total_apis = sum(len(category['apis']) for category in category_data)
        
        template = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Public APIs with Badges</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
            border-bottom: 3px solid #007acc;
            padding-bottom: 10px;
        }
        h2 {
            color: #007acc;
            margin-top: 40px;
            margin-bottom: 20px;
            padding: 10px 0;
            border-bottom: 1px solid #ddd;
        }
        .api-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        .api-card {
            background: #f9f9f9;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 20px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .api-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        .api-name {
            font-size: 1.2em;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }
        .api-name a {
            color: #007acc;
            text-decoration: none;
        }
        .api-name a:hover {
            text-decoration: underline;
        }
        .api-description {
            color: #666;
            margin-bottom: 15px;
            font-size: 0.95em;
        }
        .api-badges {
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            margin-top: 10px;
        }
        .api-badges img {
            height: 20px;
            border-radius: 3px;
        }
        .category-nav {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 30px;
            padding: 20px;
            background: #f0f0f0;
            border-radius: 8px;
        }
        .category-nav a {
            background: #007acc;
            color: white;
            padding: 8px 16px;
            text-decoration: none;
            border-radius: 4px;
            font-size: 0.9em;
            transition: background-color 0.2s ease;
        }
        .category-nav a:hover {
            background: #005a9e;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            padding: 20px;
            color: #666;
            border-top: 1px solid #ddd;
            font-size: 0.9em;
        }
        @media (max-width: 768px) {
            .api-grid {
                grid-template-columns: 1fr;
            }
            .container {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Public APIs with Badges</h1>
        <p style="text-align: center; color: #666; margin-bottom: 30px;">
            A curated list of public APIs with HTTPS, Auth, and CORS status badges
        </p>
        
        <div class="category-nav">
            {% for category in category_data %}
            <a href="#{{ category.name|lower|replace(' ', '-')|replace('&', 'and') }}">{{ category.name }}</a>
            {% endfor %}
        </div>
        
        {% for category in category_data %}
        <h2 id="{{ category.name|lower|replace(' ', '-')|replace('&', 'and') }}">{{ category.name }}</h2>
        <div class="api-grid">
            {% for api in category.apis %}
            <div class="api-card">
                <div class="api-name">
                    <a href="{{ api.entry.link }}" target="_blank" rel="noopener noreferrer">
                        {{ api.entry.name }}
                    </a>
                </div>
                <div class="api-description">
                    {{ api.entry.description }}
                </div>
                <div class="api-badges">
                    <img src="{{ api.badges.https }}" alt="HTTPS" title="HTTPS Support">
                    <img src="{{ api.badges.auth }}" alt="Auth" title="Authentication Required">
                    <img src="{{ api.badges.cors }}" alt="CORS" title="CORS Support">
                </div>
            </div>
            {% endfor %}
        </div>
        {% endfor %}
        
        <div class="footer">
            <p>Generated by <strong>api-badger</strong> - Making API documentation more visual and informative</p>
            <p>Total APIs: {{ total_apis }}</p>
        </div>
    </div>
    
    <script>
        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
        
        // Add scroll-to-top functionality
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                if (!document.querySelector('.scroll-top')) {
                    const scrollTop = document.createElement('div');
                    scrollTop.className = 'scroll-top';
                    scrollTop.innerHTML = '↑';
                    scrollTop.style.cssText = `
                        position: fixed;
                        bottom: 20px;
                        right: 20px;
                        background: #007acc;
                        color: white;
                        width: 40px;
                        height: 40px;
                        border-radius: 50%;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        cursor: pointer;
                        font-size: 20px;
                        z-index: 1000;
                        transition: background-color 0.2s ease;
                    `;
                    scrollTop.addEventListener('click', function() {
                        window.scrollTo({ top: 0, behavior: 'smooth' });
                    });
                    scrollTop.addEventListener('mouseenter', function() {
                        this.style.background = '#005a9e';
                    });
                    scrollTop.addEventListener('mouseleave', function() {
                        this.style.background = '#007acc';
                    });
                    document.body.appendChild(scrollTop);
                }
            } else {
                const scrollTop = document.querySelector('.scroll-top');
                if (scrollTop) {
                    scrollTop.remove();
                }
            }
        });
    </script>
</body>
</html>
        """)
        
        return template.render(category_data=category_data)