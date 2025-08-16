#!/usr/bin/env python3
"""
直接测试服务器 - 不需要Jekyll
用于预览HTML文件
"""

import http.server
import socketserver
import os
import sys

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 处理根路径
        if self.path == '/':
            self.path = '/index.html'
        
        # 检查是否存在HTML文件
        if not self.path.endswith('.html') and not '.' in os.path.basename(self.path):
            # 尝试添加.html扩展名
            html_path = self.path + '.html'
            if os.path.exists('.' + html_path):
                self.path = html_path
        
        return super().do_GET()

def main():
    print("🚀 测试服务器")
    print("=" * 40)
    print(f"📁 服务目录: {os.getcwd()}")
    print(f"🌐 访问地址: http://localhost:{PORT}")
    print("   按 Ctrl+C 停止服务器")
    print("=" * 40)
    
    # 检查index.md是否存在
    if os.path.exists('index.md'):
        print("⚠️  注意：此服务器直接服务Markdown文件，不会渲染Jekyll模板")
        print("   要查看完整渲染的站点，需要使用Jekyll构建")
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 服务器已停止")
            sys.exit(0)

if __name__ == "__main__":
    main()