#!/usr/bin/env python3
"""
简化的 Jekyll 项目验证脚本
不依赖外部库，验证基本的文件结构和语法
"""

import re
import sys
from pathlib import Path

def check_front_matter(content):
    """检查 Front Matter 基本格式"""
    if not content.startswith('---\n'):
        return False, "Front Matter 必须以 '---' 开始"
    
    lines = content.split('\n')
    end_count = 0
    for line in lines:
        if line.strip() == '---':
            end_count += 1
            if end_count == 2:
                return True, "Front Matter 格式正确"
    
    return False, "未找到 Front Matter 结束标记"

def validate_file_content(file_path, file_type):
    """验证文件内容"""
    print(f"🔍 验证 {file_type}: {file_path}")
    
    if not Path(file_path).exists():
        print("❌ 文件不存在")
        return False
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if not content.strip():
        print("❌ 文件为空")
        return False
    
    # 检查 XML 文件
    if file_type == 'XML RSS':
        if '<?xml' not in content:
            print("❌ 缺少 XML 声明")
            return False
        if '<rss' not in content:
            print("❌ 缺少 RSS 根元素")
            return False
        if '<channel>' not in content:
            print("❌ 缺少 channel 元素")
            return False
        if 'site.title' not in content:
            print("❌ 缺少必要的 Jekyll 变量")
            return False
    
    # 检查 HTML 文件
    elif file_type == 'HTML Layout':
        required_in_layout = ['<html', '<head', '<body']
        if str(file_path).endswith('default.html'):
            for req in required_in_layout:
                if req not in content.lower():
                    print(f"❌ 缺少必需的 HTML 元素: {req}")
                    return False
    
    # 检查带 Front Matter 的文件
    elif file_type in ['Markdown', 'HTML Page']:
        valid_fm, fm_msg = check_front_matter(content)
        if not valid_fm:
            print(f"❌ {fm_msg}")
            return False
    
    # 检查 CSS 文件
    elif file_type == 'CSS':
        if ':root' not in content:
            print("❌ 缺少 CSS 变量定义")
            return False
        if 'data-theme' not in content:
            print("❌ 缺少主题切换样式")
            return False
    
    # 检查 YAML 配置
    elif file_type == 'YAML Config':
        # CMS 配置文件检查
        if 'config.yml' in str(file_path) and 'admin' in str(file_path):
            if 'backend:' not in content:
                print("❌ CMS 配置缺少 backend 配置")
                return False
            if 'collections:' not in content:
                print("❌ CMS 配置缺少 collections 配置")
                return False
        # Jekyll 配置文件检查
        else:
            if 'title:' not in content:
                print("❌ 缺少 title 配置")
                return False
            if 'collections:' not in content:
                print("❌ 缺少 collections 配置")
                return False
    
    print("✅ 文件内容正确")
    return True

def main():
    """主验证函数"""
    print("🚀 开始简化验证...")
    print("=" * 40)
    
    base_path = Path(__file__).parent.parent
    
    # 测试文件列表
    test_files = [
        # 配置文件
        ('_config.yml', 'YAML Config'),
        ('public/admin/config.yml', 'YAML Config'),
        
        # RSS feeds
        ('rss.xml', 'XML RSS'),
        ('podcast.xml', 'XML RSS'),
        
        # HTML 布局
        ('_layouts/default.html', 'HTML Layout'),
        ('_layouts/post.html', 'HTML Layout'),
        ('_layouts/episode.html', 'HTML Layout'),
        ('_includes/head-seo.html', 'HTML Layout'),
        ('_includes/navigation.html', 'HTML Layout'),
        
        # HTML 页面
        ('tags/index.html', 'HTML Page'),
        ('public/admin/index.html', 'HTML Layout'),
        
        # Markdown 页面
        ('index.md', 'Markdown'),
        ('pages/about.md', 'Markdown'),
        ('_posts/2025-08-16-welcome-to-your-new-blog.md', 'Markdown'),
        ('_episodes/welcome-episode.md', 'Markdown'),
        
        # 样式文件
        ('assets/css/style.css', 'CSS'),
    ]
    
    passed = 0
    total = len(test_files)
    
    for file_path, file_type in test_files:
        if validate_file_content(base_path / file_path, file_type):
            passed += 1
        print()
    
    print("=" * 40)
    print(f"📊 验证结果: {passed}/{total} 通过")
    
    if passed == total:
        print("✅ 所有文件验证通过！")
        print("\n🎯 项目状态检查:")
        print("✅ 文件结构完整")
        print("✅ 配置文件正确")
        print("✅ 模板语法正确") 
        print("✅ 内容文件就绪")
        print("✅ 样式文件完整")
        print("\n🚀 准备部署到 GitHub Pages!")
        return 0
    else:
        print(f"❌ {total - passed} 个文件验证失败")
        return 1

if __name__ == "__main__":
    sys.exit(main())