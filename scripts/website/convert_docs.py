#!/usr/bin/env python3
"""
Convert markdown files from the repository into VitePress documentation structure.
"""

import os
import shutil
import re
from pathlib import Path
import frontmatter
import yaml

class DocConverter:
    def __init__(self, repo_root, output_dir):
        self.repo_root = Path(repo_root)
        self.output_dir = Path(output_dir)
        self.docs_dir = self.output_dir / 'docs'
        self.sidebar_en = []
        self.sidebar_zh = []
        
    def setup_dirs(self):
        """Create necessary directories."""
        for dir_path in [self.docs_dir, self.docs_dir / 'zh', self.docs_dir / 'public']:
            dir_path.mkdir(parents=True, exist_ok=True)
            
    def copy_images(self):
        """Copy images to public directory."""
        images_dir = self.repo_root / 'images'
        if images_dir.exists():
            shutil.copytree(images_dir, self.docs_dir / 'public' / 'images', dirs_exist_ok=True)
            
    def fix_image_paths(self, content):
        """Fix image paths in markdown content."""
        return re.sub(r'!\[(.*?)\]\((.*?/images/.*?)\)', r'![\1](/images/\2)', content)
        
    def fix_internal_links(self, content):
        """Fix internal markdown links."""
        def replace_link(match):
            link = match.group(2)
            if link.endswith('.md'):
                link = link[:-3] + '.html'
            return f'[{match.group(1)}]({link})'
        return re.sub(r'\[(.*?)\]\((.*?)\)', replace_link, content)
        
    def process_markdown(self, file_path, is_chinese=False):
        """Process a markdown file and convert it for VitePress."""
        rel_path = file_path.relative_to(self.repo_root)
        output_subdir = 'zh' if is_chinese else '.'
        
        # Determine output path
        if file_path.name.lower() in ['readme.md', 'readme.cn.md']:
            output_name = 'index.md'
        else:
            output_name = file_path.stem.lower().replace(' ', '-') + '.md'
            
        output_path = self.docs_dir / output_subdir / output_name
        
        # Read and process content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Add frontmatter
        fm = {
            'title': self.extract_title(content) or file_path.stem,
            'lang': 'zh-CN' if is_chinese else 'en-US'
        }
        
        # Process content
        content = self.fix_image_paths(content)
        content = self.fix_internal_links(content)
        
        # Write processed content
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('---\n')
            f.write(yaml.dump(fm))
            f.write('---\n\n')
            f.write(content)
            
        return output_path.relative_to(self.docs_dir)
        
    def extract_title(self, content):
        """Extract title from markdown content."""
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        return match.group(1) if match else None
        
    def process_directory(self, dir_path, is_chinese=False):
        """Process all markdown files in a directory."""
        items = []
        for item in sorted(dir_path.iterdir()):
            if item.is_file() and item.suffix.lower() == '.md':
                rel_path = self.process_markdown(item, is_chinese)
                title = self.extract_title(item.read_text('utf-8')) or item.stem
                items.append({
                    'text': title,
                    'link': f'/{rel_path}'.replace('.md', '.html')
                })
            elif item.is_dir() and item.name not in ['.git', 'venv', 'node_modules']:
                sub_items = self.process_directory(item, is_chinese)
                if sub_items:
                    items.append({
                        'text': item.name.capitalize(),
                        'items': sub_items
                    })
        return items
        
    def update_config(self):
        """Update VitePress config with sidebar information."""
        config_path = self.docs_dir / '.vitepress' / 'config.ts'
        if not config_path.exists():
            return
            
        config_content = config_path.read_text('utf-8')
        # Update sidebar configuration
        sidebar_config = {
            '/': self.sidebar_en,
            '/zh/': self.sidebar_zh
        }
        # TODO: Update config.ts with new sidebar information
        
    def convert(self):
        """Main conversion process."""
        self.setup_dirs()
        self.copy_images()
        
        # Process English docs
        self.sidebar_en = self.process_directory(self.repo_root)
        
        # Process Chinese docs
        chinese_dir = self.repo_root / 'chinese'
        if chinese_dir.exists():
            self.sidebar_zh = self.process_directory(chinese_dir, True)
            
        # Process additional Chinese docs in root
        for f in self.repo_root.glob('*.cn.md'):
            self.process_markdown(f, True)
            
        self.update_config()
        
def main():
    repo_root = Path('/Users/cs/work/AgentNetworkProtocol')
    output_dir = repo_root / 'scripts' / 'website'
    
    converter = DocConverter(repo_root, output_dir)
    converter.convert()
    
if __name__ == '__main__':
    main()
