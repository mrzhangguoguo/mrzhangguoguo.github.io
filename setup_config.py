#!/usr/bin/env python3
"""
配置更新脚本
根据用户输入更新站点配置信息
"""

import sys
import re
from pathlib import Path

def update_jekyll_config(site_title, site_description, site_url, base_url, email=""):
    """更新 Jekyll 配置文件"""
    config_path = Path("_config.yml")
    
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新配置项
    content = re.sub(r'title:.*', f'title: "{site_title}"', content)
    content = re.sub(r'description:.*', f'description: "{site_description}"', content)
    content = re.sub(r'url:.*', f'url: "{site_url}"', content)
    content = re.sub(r'baseurl:.*', f'baseurl: "{base_url}"', content)
    
    # 添加邮箱（如果提供）
    if email:
        if 'email:' in content:
            content = re.sub(r'email:.*', f'email: "{email}"', content)
        else:
            # 在最后添加邮箱配置
            content += f'\nemail: "{email}"\n'
    
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 已更新 Jekyll 配置文件")

def update_cms_config(github_username, repo_name):
    """更新 CMS 配置文件"""
    cms_config_path = Path("public/admin/config.yml")
    
    with open(cms_config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新仓库配置
    content = re.sub(
        r'repo: username/blogs-for-github.*', 
        f'repo: {github_username}/{repo_name}',
        content
    )
    
    with open(cms_config_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 已更新 CMS 配置文件")

def main():
    """主配置函数"""
    print("🔧 Jekyll 博客配置向导")
    print("=" * 40)
    
    # 获取用户输入
    print("请提供以下信息来配置你的博客：\n")
    
    site_title = input("1. 博客/播客名称: ").strip()
    if not site_title:
        site_title = "My Blog & Podcast"
    
    site_description = input("2. 博客描述: ").strip()
    if not site_description:
        site_description = "A personal blog and podcast platform"
    
    github_username = input("3. GitHub 用户名: ").strip()
    if not github_username:
        print("❌ GitHub 用户名不能为空")
        return 1
    
    repo_name = input("4. 仓库名称: ").strip()
    if not repo_name:
        print("❌ 仓库名称不能为空")
        return 1
    
    email = input("5. 联系邮箱 (可选): ").strip()
    
    # 生成 URL
    site_url = f"https://{github_username}.github.io"
    base_url = f"/{repo_name}" if repo_name != f"{github_username}.github.io" else ""
    
    print("\n📝 配置摘要:")
    print(f"   站点名称: {site_title}")
    print(f"   站点描述: {site_description}")
    print(f"   GitHub 用户: {github_username}")
    print(f"   仓库名称: {repo_name}")
    print(f"   站点 URL: {site_url}{base_url}")
    if email:
        print(f"   联系邮箱: {email}")
    
    confirm = input("\n确认配置信息正确吗? (y/N): ").strip().lower()
    if confirm != 'y':
        print("❌ 已取消配置")
        return 1
    
    # 更新配置文件
    print("\n🔄 正在更新配置文件...")
    
    try:
        update_jekyll_config(site_title, site_description, site_url, base_url, email)
        update_cms_config(github_username, repo_name)
        
        print("\n✅ 配置更新完成！")
        print("\n📋 下一步操作:")
        print("1. 运行测试验证配置: python3 test/simple_validation.py")
        print("2. 初始化 Git 仓库: git init")
        print("3. 推送代码到 GitHub")
        
        return 0
        
    except Exception as e:
        print(f"❌ 配置更新失败: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())