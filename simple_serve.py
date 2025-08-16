#!/usr/bin/env python3
"""
简单的Jekyll站点测试服务器
"""

import subprocess
import os
import sys
from pathlib import Path

def build_jekyll():
    """构建Jekyll站点"""
    print("🔨 正在构建Jekyll站点...")
    
    # 首先检查bundle是否安装了依赖
    print("检查依赖...")
    result = subprocess.run(['which', 'jekyll'], capture_output=True)
    if result.returncode != 0:
        print("Jekyll未安装，尝试使用系统Jekyll...")
        # 尝试直接使用Jekyll
        result = subprocess.run(
            ['jekyll', 'build', '--baseurl', ''],
            capture_output=True,
            text=True
        )
    else:
        # 使用bundle exec
        result = subprocess.run(
            ['jekyll', 'build', '--baseurl', ''],
            capture_output=True,
            text=True
        )
    
    if result.returncode != 0:
        print(f"❌ Jekyll构建失败:")
        print(result.stderr)
        print("\n尝试简单HTTP服务器...")
        return False
    
    print("✅ Jekyll站点构建成功!")
    return True

def start_simple_server():
    """启动简单的Python HTTP服务器"""
    build_dir = "_site"
    
    # 如果构建目录不存在，创建一个测试页面
    if not os.path.exists(build_dir):
        print(f"⚠️  {build_dir} 目录不存在，将使用当前目录")
        build_dir = "."
    
    os.chdir(build_dir)
    
    print(f"🚀 在 http://localhost:8000 启动服务器")
    print("   按 Ctrl+C 停止服务器")
    
    # 启动Python HTTP服务器
    if sys.version_info[0] >= 3:
        subprocess.run(['python3', '-m', 'http.server', '8000'])
    else:
        subprocess.run(['python', '-m', 'SimpleHTTPServer', '8000'])

def main():
    """主函数"""
    print("🚀 Jekyll Python 测试服务器")
    print("=" * 40)
    
    # 尝试构建Jekyll
    build_success = build_jekyll()
    
    # 启动服务器
    try:
        start_simple_server()
    except KeyboardInterrupt:
        print("\n\n👋 服务器已停止")
        sys.exit(0)
    except Exception as e:
        print(f"❌ 服务器错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()