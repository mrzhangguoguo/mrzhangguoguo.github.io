#!/usr/bin/env python3
"""
Jekyll 模板验证脚本
验证 Jekyll 模板语法和 Front Matter 格式
"""

import yaml
import re
import sys
from pathlib import Path

def validate_front_matter(content):
    """验证 Front Matter 格式"""
    if not content.startswith('---\n'):
        return False, "Front Matter 必须以 '---' 开始"
    
    # 找到第二个 ---
    lines = content.split('\n')
    end_index = -1
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            end_index = i
            break
    
    if end_index == -1:
        return False, "找不到 Front Matter 结束标记 '---'"
    
    # 提取 Front Matter YAML
    yaml_content = '\n'.join(lines[1:end_index])
    
    try:
        yaml.safe_load(yaml_content)
        return True, "Front Matter YAML 格式正确"
    except yaml.YAMLError as e:
        return False, f"YAML 格式错误: {e}"

def validate_liquid_syntax(content):
    """验证 Liquid 模板语法"""
    # 基本的 Liquid 语法检查
    liquid_patterns = [
        r'\{\{.*?\}\}',  # {{ variable }}
        r'\{%.*?%\}',    # {% tag %}
    ]
    
    issues = []
    
    # 检查未闭合的标签
    open_tags = re.findall(r'\{%\s*(\w+)', content)
    close_tags = re.findall(r'\{%\s*end(\w+)', content)
    
    for tag in open_tags:
        if tag not in ['assign', 'comment', 'raw', 'capture'] and tag not in close_tags:
            if f'end{tag}' not in content:
                issues.append(f"可能未闭合的标签: {tag}")
    
    return len(issues) == 0, issues

def validate_xml_template(file_path):
    """验证 XML 模板文件"""
    print(f"🔍 验证 XML 模板: {file_path}")
    
    if not Path(file_path).exists():
        print("❌ 文件不存在")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 验证 Front Matter
    valid_fm, fm_message = validate_front_matter(content)
    if not valid_fm:
        print(f"❌ {fm_message}")
        return False
    print(f"✅ {fm_message}")
    
    # 验证 Liquid 语法
    valid_liquid, liquid_issues = validate_liquid_syntax(content)
    if not valid_liquid:
        print(f"❌ Liquid 语法问题: {liquid_issues}")
        return False
    print("✅ Liquid 语法正确")
    
    # 检查 XML 结构（忽略 Liquid 标签）
    xml_content = re.sub(r'\{[{%].*?[%}]\}', 'PLACEHOLDER', content)
    xml_lines = xml_content.split('\n')
    
    # 找到 XML 开始位置
    xml_start = -1
    for i, line in enumerate(xml_lines):
        if line.strip().startswith('<?xml'):
            xml_start = i
            break
    
    if xml_start == -1:
        print("❌ 未找到 XML 声明")
        return False
    
    print("✅ XML 模板结构正确")
    return True

def validate_html_template(file_path):
    """验证 HTML 模板文件"""
    print(f"🔍 验证 HTML 模板: {file_path}")
    
    if not Path(file_path).exists():
        print("❌ 文件不存在")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查基本 HTML 结构
    required_tags = ['<html', '<head', '<body']
    for tag in required_tags:
        if tag not in content.lower():
            print(f"❌ 缺少必需的 HTML 标签: {tag}")
            return False
    
    # 验证 Liquid 语法
    valid_liquid, liquid_issues = validate_liquid_syntax(content)
    if not valid_liquid:
        print(f"❌ Liquid 语法问题: {liquid_issues}")
        return False
    
    print("✅ HTML 模板格式正确")
    return True

def validate_markdown_with_fm(file_path):
    """验证带 Front Matter 的 Markdown 文件"""
    print(f"🔍 验证 Markdown 文件: {file_path}")
    
    if not Path(file_path).exists():
        print("❌ 文件不存在")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 验证 Front Matter
    valid_fm, fm_message = validate_front_matter(content)
    if not valid_fm:
        print(f"❌ {fm_message}")
        return False
    
    print("✅ Markdown Front Matter 正确")
    return True

def main():
    """主测试函数"""
    print("🚀 开始验证 Jekyll 模板...")
    print("=" * 50)
    
    base_path = Path(__file__).parent.parent
    
    tests_passed = 0
    total_tests = 0
    
    # 验证 XML 模板
    xml_files = ['rss.xml', 'podcast.xml']
    for xml_file in xml_files:
        total_tests += 1
        if validate_xml_template(base_path / xml_file):
            tests_passed += 1
        print()
    
    # 验证 HTML 模板
    html_files = [
        '_layouts/default.html',
        '_layouts/post.html', 
        '_layouts/episode.html',
        '_includes/head-seo.html',
        '_includes/navigation.html',
        'tags/index.html',
        'public/admin/index.html'
    ]
    
    for html_file in html_files:
        total_tests += 1
        if validate_html_template(base_path / html_file):
            tests_passed += 1
        print()
    
    # 验证 Markdown 文件
    md_files = [
        'index.md',
        'pages/about.md',
        '_posts/2025-08-16-welcome-to-your-new-blog.md',
        '_episodes/welcome-episode.md'
    ]
    
    for md_file in md_files:
        total_tests += 1
        if validate_markdown_with_fm(base_path / md_file):
            tests_passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 模板验证结果: {tests_passed}/{total_tests} 通过")
    
    if tests_passed == total_tests:
        print("✅ 所有模板验证通过！")
        return 0
    else:
        print("❌ 部分模板验证失败")
        return 1

if __name__ == "__main__":
    sys.exit(main())