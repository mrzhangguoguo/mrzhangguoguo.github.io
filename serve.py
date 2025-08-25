#!/usr/bin/env python3
"""
Jekyll 站点本地测试服务器
使用Python构建Jekyll站点并启动本地HTTP服务器
"""

import subprocess
import sys
import os
import http.server
import socketserver
import threading
import time
from pathlib import Path

PORT = 4000
BUILD_DIR = "_site"

def build_jekyll():
    """构建Jekyll站点"""
    print("🔨 正在构建Jekyll站点...")
    try:
        # 设置环境变量，确保使用正确的baseurl
        env = os.environ.copy()
        env['JEKYLL_ENV'] = 'development'
        
        # 构建Jekyll站点
        result = subprocess.run(
            ['bundle', 'exec', 'jekyll', 'build', '--baseurl', ''],
            capture_output=True,
            text=True,
            env=env
        )
        
        if result.returncode != 0:
            print(f"❌ Jekyll构建失败:")
            print(f"错误输出:\n{result.stderr}")
            print(f"标准输出:\n{result.stdout}")
            return False
            
        print("✅ Jekyll站点构建成功!")
        return True
        
    except FileNotFoundError:
        print("❌ 未找到Jekyll，请确保已安装Jekyll并运行了 bundle install")
        return False
    except Exception as e:
        print(f"❌ 构建错误: {e}")
        return False

def start_server():
    """启动HTTP服务器"""
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=BUILD_DIR, **kwargs)
            
        def do_GET(self):
            # 处理没有扩展名的路径，尝试添加.html
            if '.' not in self.path.split('/')[-1]:
                html_path = self.path.rstrip('/') + '.html'
                test_path = Path(BUILD_DIR) / html_path.lstrip('/')
                if test_path.exists():
                    self.path = html_path
            super().do_GET()
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🚀 服务器运行在 http://localhost:{PORT}")
        print("   按 Ctrl+C 停止服务器")
        httpd.serve_forever()

def watch_and_rebuild():
    """监视文件变化并重新构建"""
    print("👁️  监视文件变化中...")
    last_build = time.time()
    
    while True:
        try:
            # 检查源文件是否有更新
            needs_rebuild = False
            for pattern in ['*.md', '*.html', '_config.yml', '_layouts/*', '_includes/*', 'assets/**/*']:
                for file_path in Path('.').glob(pattern):
                    if file_path.stat().st_mtime > last_build:
                        needs_rebuild = True
                        break
                if needs_rebuild:
                    break
            
            if needs_rebuild:
                print("\n📝 检测到文件变化，重新构建...")
                if build_jekyll():
                    last_build = time.time()
                    print("✅ 重新构建完成\n")
            
            time.sleep(2)  # 每2秒检查一次
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ 监视错误: {e}")
            time.sleep(5)

def main():
    """主函数"""
    print("🚀 Jekyll Python 测试服务器")
    print("=" * 40)
    
    # 首次构建
    if not build_jekyll():
        sys.exit(1)
    
    # 启动文件监视线程
    watcher = threading.Thread(target=watch_and_rebuild, daemon=True)
    watcher.start()
    
    # 启动服务器
    try:
        start_server()
    except KeyboardInterrupt:
        print("\n\n👋 服务器已停止")
        sys.exit(0)
    except Exception as e:
        print(f"❌ 服务器错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()