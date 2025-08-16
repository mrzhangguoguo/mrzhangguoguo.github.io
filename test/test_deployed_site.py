#!/usr/bin/env python3
"""
部署后网站验证脚本
用于验证已部署的 GitHub Pages 网站功能
"""

import urllib.request
import urllib.error
import sys
import time

def test_url(url, test_name, expected_content=None):
    """测试 URL 是否可访问"""
    print(f"🔍 测试: {test_name}")
    print(f"   URL: {url}")
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            if response.status == 200:
                content = response.read().decode('utf-8')
                
                if expected_content:
                    if expected_content in content:
                        print("✅ 通过 - 页面加载正常且包含预期内容")
                        return True
                    else:
                        print(f"❌ 失败 - 页面加载但缺少预期内容: {expected_content}")
                        return False
                else:
                    print("✅ 通过 - 页面加载正常")
                    return True
            else:
                print(f"❌ 失败 - HTTP 状态码: {response.status}")
                return False
                
    except urllib.error.HTTPError as e:
        print(f"❌ 失败 - HTTP 错误: {e.code} {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"❌ 失败 - URL 错误: {e.reason}")
        return False
    except Exception as e:
        print(f"❌ 失败 - 其他错误: {e}")
        return False

def main():
    """主测试函数"""
    if len(sys.argv) != 2:
        print("使用方法: python3 test_deployed_site.py <网站URL>")
        print("示例: python3 test_deployed_site.py https://username.github.io")
        return 1
    
    base_url = sys.argv[1].rstrip('/')
    
    print("🚀 开始测试已部署的网站...")
    print("=" * 50)
    print(f"测试网站: {base_url}")
    print("=" * 50)
    
    # 测试项目列表
    tests = [
        # 基本页面
        (f"{base_url}/", "主页访问", "Your Podcast"),
        (f"{base_url}/pages/about/", "关于页面", "About"),
        (f"{base_url}/tags/", "标签页面", "Tags"),
        
        # 示例内容
        (f"{base_url}/posts/welcome-to-your-new-blog/", "示例文章", "Welcome"),
        (f"{base_url}/episodes/welcome-episode/", "示例播客", "Episode 1"),
        
        # RSS Feeds
        (f"{base_url}/rss.xml", "博客 RSS Feed", "<?xml"),
        (f"{base_url}/podcast.xml", "播客 RSS Feed", "<?xml"),
        
        # CMS
        (f"{base_url}/public/admin/", "CMS 管理界面", "Content Manager"),
        
        # 静态资源
        (f"{base_url}/assets/css/style.css", "CSS 样式文件", ":root"),
    ]
    
    passed = 0
    total = len(tests)
    
    for url, test_name, expected in tests:
        if test_url(url, test_name, expected):
            passed += 1
        print()
        time.sleep(1)  # 避免请求过于频繁
    
    print("=" * 50)
    print(f"📊 测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("✅ 所有测试通过！")
        print("\n🎉 网站部署成功，功能正常！")
        print("\n📋 后续步骤:")
        print("1. 通过 /public/admin/ 创建你的第一篇文章")
        print("2. 更新站点信息和配置")
        print("3. 上传真实的播客音频文件")
        print("4. 自定义样式和品牌元素")
        return 0
    else:
        print(f"❌ {total - passed} 个测试失败")
        print("\n🔧 请检查:")
        print("1. GitHub Pages 是否已正确配置")
        print("2. 仓库是否设置为 public")
        print("3. 域名和 baseurl 配置是否正确")
        return 1

if __name__ == "__main__":
    sys.exit(main())