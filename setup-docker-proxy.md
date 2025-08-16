# 配置Docker使用代理

## 方法1：Docker Desktop GUI配置（推荐）

1. 打开Docker Desktop
2. 点击设置(Settings) → Resources → Proxies
3. 启用"Manual proxy configuration"
4. 填写以下信息：
   - HTTP proxy: `http://127.0.0.1:1087`（如果你有HTTP代理）
   - HTTPS proxy: `http://127.0.0.1:1087`
   - 或使用SOCKS5: `socks5://127.0.0.1:1081`
5. 点击"Apply & Restart"

## 方法2：使用镜像加速器

创建或编辑 `~/.docker/daemon.json`：

```json
{
  "registry-mirrors": [
    "https://docker.mirrors.ustc.edu.cn",
    "https://hub-mirror.c.163.com",
    "https://mirror.baidubce.com"
  ]
}
```

然后重启Docker Desktop。

## 方法3：使用代理拉取镜像

```bash
# 为Docker守护进程配置代理
sudo mkdir -p /etc/systemd/system/docker.service.d

# 创建代理配置
cat > /tmp/http-proxy.conf << EOF
[Service]
Environment="HTTP_PROXY=socks5://127.0.0.1:1081"
Environment="HTTPS_PROXY=socks5://127.0.0.1:1081"
Environment="NO_PROXY=localhost,127.0.0.1"
EOF

sudo mv /tmp/http-proxy.conf /etc/systemd/system/docker.service.d/

# 重启Docker
sudo systemctl daemon-reload
sudo systemctl restart docker
```

## 测试配置

配置完成后，运行：

```bash
docker pull hello-world
```

如果能成功拉取，说明代理配置正确。

## 启动Jekyll

配置成功后，运行：

```bash
./docker-with-proxy.sh
```

或直接：

```bash
docker run --rm \
  --volume="$PWD:/srv/jekyll" \
  --publish 4000:4000 \
  jekyll/jekyll:latest \
  jekyll serve --baseurl '' --host 0.0.0.0
```