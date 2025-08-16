#!/usr/bin/env python3
"""
RSS 和 Podcast Feed 验证脚本
验证生成的 XML 文件格式是否正确
"""

import xml.etree.ElementTree as ET
import re
import sys
from pathlib import Path

def validate_xml_file(file_path):
    """验证 XML 文件格式"""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return True, root
    except ET.ParseError as e:
        return False, str(e)

def validate_rss_feed(file_path):
    """验证博客 RSS feed"""
    print(f"🔍 验证博客 RSS: {file_path}")
    
    if not Path(file_path).exists():
        print("❌ 文件不存在")
        return False
    
    valid, root_or_error = validate_xml_file(file_path)
    if not valid:
        print(f"❌ XML 格式错误: {root_or_error}")
        return False
    
    root = root_or_error
    
    # 检查基本结构
    if root.tag != 'rss':
        print("❌ 根元素不是 'rss'")
        return False
    
    channel = root.find('channel')
    if channel is None:
        print("❌ 缺少 'channel' 元素")
        return False
    
    # 检查必需字段
    required_fields = ['title', 'description', 'link']
    for field in required_fields:
        if channel.find(field) is None:
            print(f"❌ 缺少必需字段: {field}")
            return False
    
    print("✅ 博客 RSS 格式正确")
    return True

def validate_podcast_feed(file_path):
    """验证播客 RSS feed"""
    print(f"🔍 验证播客 RSS: {file_path}")
    
    if not Path(file_path).exists():
        print("❌ 文件不存在")
        return False
    
    valid, root_or_error = validate_xml_file(file_path)
    if not valid:
        print(f"❌ XML 格式错误: {root_or_error}")
        return False
    
    root = root_or_error
    
    # 检查基本结构
    if root.tag != 'rss':
        print("❌ 根元素不是 'rss'")
        return False
    
    channel = root.find('channel')
    if channel is None:
        print("❌ 缺少 'channel' 元素")
        return False
    
    # 检查播客特有字段
    required_fields = ['title', 'description', 'link']
    for field in required_fields:
        if channel.find(field) is None:
            print(f"❌ 缺少必需字段: {field}")
            return False
    
    # 检查 iTunes 命名空间
    if 'itunes' not in root.attrib.get('xmlns:itunes', ''):
        print("⚠️  建议添加 iTunes 命名空间")
    
    print("✅ 播客 RSS 格式正确")
    return True

def main():
    """主测试函数"""
    print("🚀 开始验证 RSS Feeds...")
    print("=" * 40)
    
    base_path = Path(__file__).parent.parent
    
    # 验证文件
    tests_passed = 0
    total_tests = 2
    
    # 测试博客 RSS
    if validate_rss_feed(base_path / "rss.xml"):
        tests_passed += 1
    
    # 测试播客 RSS  
    if validate_podcast_feed(base_path / "podcast.xml"):
        tests_passed += 1
    
    print("=" * 40)
    print(f"📊 测试结果: {tests_passed}/{total_tests} 通过")
    
    if tests_passed == total_tests:
        print("✅ 所有 Feed 验证通过！")
        return 0
    else:
        print("❌ 部分 Feed 验证失败")
        return 1

if __name__ == "__main__":
    sys.exit(main())