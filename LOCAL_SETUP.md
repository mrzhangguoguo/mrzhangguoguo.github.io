# 本地Jekyll环境设置指南（不污染系统）

## 方案选择

### 方案1: Docker（推荐） ⭐⭐⭐⭐⭐
**完全隔离，零污染**

```bash
# 一键启动
./start.sh

# 或直接运行
docker run --rm -v "$PWD:/srv/jekyll" -p 4000:4000 jekyll/jekyll jekyll serve --baseurl ''
```

**优点：**
- ✅ 完全隔离，不安装任何东西到系统
- ✅ 一键启动，无需配置
- ✅ 版本一致性好
- ✅ 可以随时删除，不留痕迹

**缺点：**
- 需要安装Docker Desktop
- 首次启动需要下载镜像（约200MB）

---

### 方案2: rbenv（次推荐） ⭐⭐⭐⭐
**Ruby版本隔离**

```bash
# 安装设置
./setup-rbenv.sh

# 启动服务器
bundle exec jekyll serve --baseurl ''
```

**优点：**
- ✅ 不影响系统Ruby
- ✅ 每个项目可以用不同Ruby版本
- ✅ 性能比Docker好

**缺点：**
- 需要安装rbenv到系统
- 配置稍微复杂

---

### 方案3: Python预览（最简单） ⭐⭐⭐
**仅静态预览**

```bash
# 启动Python服务器
python3 test_server.py

# 访问预览页面
# http://localhost:8000/preview.html
# http://localhost:8000/preview-post.html
```

**优点：**
- ✅ 无需安装任何东西
- ✅ 立即可用

**缺点：**
- ❌ 不能渲染Jekyll模板
- ❌ 只能看静态HTML

---

## 快速开始

### 如果你想要完全不污染系统：
```bash
# 使用Docker
./start.sh
```

### 如果你不介意安装rbenv：
```bash
# 使用rbenv
./setup-rbenv.sh
bundle exec jekyll serve --baseurl ''
```

### 如果只想快速预览样式：
```bash
# 使用Python
python3 test_server.py
# 打开 http://localhost:8000/preview.html
```

---

## Docker详细命令

```bash
# 启动开发服务器
docker-compose up

# 后台运行
docker-compose up -d

# 停止服务器
docker-compose down

# 构建站点
docker run --rm -v "$PWD:/srv/jekyll" jekyll/jekyll jekyll build

# 进入容器shell
docker run --rm -it -v "$PWD:/srv/jekyll" jekyll/jekyll /bin/bash

# 清理所有Docker缓存
docker system prune -a
```

---

## 常见问题

### Q: Docker太慢怎么办？
A: 可以配置Docker镜像加速器，或使用rbenv方案。

### Q: rbenv和rvm有什么区别？
A: rbenv更轻量，rvm功能更多。对于Jekyll来说rbenv足够。

### Q: 可以用虚拟机吗？
A: 可以，但太重了。Docker本质上就是轻量级虚拟化。

### Q: 如何完全清理环境？
A: 
- Docker: `docker system prune -a` 
- rbenv: `rm -rf ~/.rbenv`
- 项目: `rm -rf vendor/ _site/ .bundle/`

---

## 推荐工作流

1. **开发环境**: Docker或rbenv
2. **快速预览**: Python服务器
3. **生产部署**: GitHub Pages（自动构建）

选择最适合你的方案即可！