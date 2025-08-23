---
layout: post
title: "Claude Code安装配置完全指南：零基础到专业部署"
date: 2025-08-16 10:00:00 +0800
tags: [Claude Code, 安装配置, 开发环境, 教程]
excerpt: "详细的Claude Code安装配置指南，涵盖Windows、Mac、Linux全平台，包含常见问题解决方案和最佳实践配置。"
---

## 引言：准备开启AI编程之旅

在上一篇文章中，我们了解了[什么是Claude Code](01-什么是Claude-Code.md)。现在，让我们动手安装并配置这个革命性的AI编程工具。

本文将提供**最详细、最实用**的安装指南，确保你能够在任何操作系统上成功部署Claude Code。

## 系统要求与环境准备

### 最低系统要求

| 项目 | Windows | macOS | Linux |
|------|---------|-------|--------|
| **操作系统** | Windows 10/11 | macOS 10.15+ | Ubuntu 18.04+ / CentOS 7+ |
| **内存** | 4GB RAM | 4GB RAM | 4GB RAM |
| **存储** | 1GB可用空间 | 1GB可用空间 | 1GB可用空间 |
| **网络** | 稳定的互联网连接 | 稳定的互联网连接 | 稳定的互联网连接 |

### 推荐系统配置

| 项目 | 推荐配置 |
|------|----------|
| **内存** | 8GB+ RAM |
| **存储** | SSD硬盘，5GB+可用空间 |
| **网络** | 宽带连接（用于大型项目分析） |
| **终端** | 支持UTF-8的现代终端 |

## 安装前准备工作

### 1. 检查Node.js版本

Claude Code需要Node.js 18.x或更高版本：

```bash
# 检查Node.js版本
node --version

# 检查npm版本  
npm --version
```

**如果未安装或版本过低，请先安装Node.js：**

#### Windows用户
```bash
# 方法1：从官网下载
# 访问 https://nodejs.org 下载LTS版本

# 方法2：使用Chocolatey
choco install nodejs

# 方法3：使用Scoop
scoop install nodejs
```

#### macOS用户
```bash
# 方法1：使用Homebrew（推荐）
brew install node

# 方法2：使用MacPorts
sudo port install nodejs18

# 方法3：从官网下载
# 访问 https://nodejs.org
```

#### Linux用户
```bash
# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# CentOS/RHEL/Fedora  
curl -fsSL https://rpm.nodesource.com/setup_lts.x | sudo bash -
sudo yum install -y nodejs

# Arch Linux
sudo pacman -S nodejs npm
```

### 2. 配置npm权限（重要！）

⚠️ **绝对不要使用 `sudo npm install -g`！** 这会导致权限问题和安全风险。

#### 正确的权限配置方法：

**方法1：使用npm内置配置（推荐）**
```bash
# 设置全局包安装目录
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'

# 添加到PATH（添加到你的 .bashrc 或 .zshrc）
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

**方法2：修改npm默认目录权限**
```bash
# 获取npm全局目录
npm config get prefix

# 修改权限（将 /usr/local 替换为实际路径）
sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}
```

### 3. 网络环境检查

Claude Code需要访问Anthropic的API服务：

```bash
# 检查网络连接
curl -I https://api.anthropic.com

# 如果你在中国大陆，可能需要配置代理
# 设置代理（临时）
export https_proxy=http://your-proxy:port
export http_proxy=http://your-proxy:port
```

## Claude Code安装方法

### 方法1：NPM安装（推荐）

这是最简单且最可靠的安装方式：

```bash
# 安装Claude Code
npm install -g @anthropic-ai/claude-code

# 验证安装
claude --version
```

**如果遇到权限错误：**
```bash
# 错误示例
npm ERR! Error: EACCES: permission denied

# 解决方案：使用npx（临时使用）
npx @anthropic-ai/claude-code --version

# 或者重新配置npm权限（参考上面的权限配置部分）
```

### 方法2：原生二进制安装

Anthropic提供了预编译的二进制文件：

#### macOS
```bash
# 使用curl下载
curl -fsSL https://claude.ai/install.sh | sh

# 或手动下载
curl -L https://github.com/anthropics/claude-code/releases/latest/download/claude-macos.tar.gz -o claude.tar.gz
tar -xzf claude.tar.gz
sudo mv claude /usr/local/bin/
```

#### Linux
```bash
# x64版本
curl -L https://github.com/anthropics/claude-code/releases/latest/download/claude-linux-x64.tar.gz -o claude.tar.gz

# ARM64版本（如树莓派）
curl -L https://github.com/anthropics/claude-code/releases/latest/download/claude-linux-arm64.tar.gz -o claude.tar.gz

# 解压和安装
tar -xzf claude.tar.gz
sudo mv claude /usr/local/bin/
chmod +x /usr/local/bin/claude
```

#### Windows
```bash
# 使用PowerShell
Invoke-WebRequest -Uri "https://github.com/anthropics/claude-code/releases/latest/download/claude-windows.zip" -OutFile "claude.zip"
Expand-Archive -Path "claude.zip" -DestinationPath "C:\Program Files\Claude Code"

# 添加到PATH环境变量
$env:PATH += ";C:\Program Files\Claude Code"
```

### 方法3：从源码构建（高级用户）

```bash
# 克隆仓库
git clone https://github.com/anthropics/claude-code.git
cd claude-code

# 安装依赖
npm install

# 构建
npm run build

# 全局安装
npm link
```

## 身份认证配置

### 获取API访问权限

Claude Code需要Anthropic账户认证：

#### 选项1：Claude Pro/Max用户（推荐）

如果你有Claude Pro或Max订阅：

```bash
# 启动认证流程
claude auth

# 这会打开浏览器，完成OAuth认证
# 认证成功后，会自动保存token
```

#### 选项2：Anthropic Console用户

如果你有Anthropic开发者账户：

```bash
# 设置API密钥
claude auth --api-key your_api_key_here

# 或设置环境变量
export ANTHROPIC_API_KEY=your_api_key_here
```

#### 获取API密钥的步骤：

1. 访问 [Anthropic Console](https://console.anthropic.com)
2. 登录或注册账户
3. 进入 "API Keys" 页面
4. 点击 "Create Key"
5. 复制生成的API密钥

### 验证认证状态

```bash
# 检查认证状态
claude auth status

# 测试API连接
claude --test-connection

# 查看账户信息
claude profile
```

## 初始配置与优化

### 1. 基础配置

```bash
# 查看当前配置
claude config list

# 设置默认模型（可选）
claude config set model claude-4-sonnet  # 平衡性能
# 或
claude config set model claude-4-opus   # 最高质量

# 设置工作目录
claude config set workspace ~/Projects

# 配置代理（如果需要）
claude config set proxy http://your-proxy:port
```

### 2. 性能优化配置

```bash
# 设置并发数（根据你的网络情况调整）
claude config set max-concurrent-requests 3

# 设置超时时间（秒）
claude config set timeout 30

# 启用缓存（加速重复操作）
claude config set cache-enabled true

# 设置缓存大小（MB）
claude config set cache-size 100
```

### 3. 用户体验配置

```bash
# 启用彩色输出
claude config set color-output true

# 设置编辑器（用于编辑长文本）
claude config set editor code  # VS Code
# 或
claude config set editor vim   # Vim

# 启用自动保存
claude config set auto-save true

# 设置日志级别
claude config set log-level info  # debug, info, warn, error
```

### 4. 安全配置

```bash
# 启用确认提示（重要操作需要确认）
claude config set confirm-destructive true

# 设置敏感文件保护
claude config set protect-sensitive-files true

# 配置备份
claude config set auto-backup true
claude config set backup-location ~/.claude/backups
```

## 验证安装成功

### 1. 基本功能测试

```bash
# 显示版本信息
claude --version

# 显示帮助信息
claude --help

# 测试基本对话
claude "Hello, Claude!"
```

### 2. 创建测试项目

```bash
# 创建测试目录
mkdir claude-test
cd claude-test

# 初始化项目
claude init "Test Project"

# 创建一个简单的文件
claude "Create a hello world script in Python"

# 运行生成的脚本
python hello.py
```

### 3. 性能测试

```bash
# 测试响应时间
time claude "What is 2+2?"

# 测试文件操作
claude "Create a simple web server using Node.js"
```

## 常见问题与解决方案

### 问题1：安装失败 - 权限错误

**错误信息：**
```
npm ERR! Error: EACCES: permission denied, mkdir '/usr/local/lib/node_modules'
```

**解决方案：**
```bash
# 不要使用sudo！使用正确的npm配置
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

# 然后重新安装
npm install -g @anthropic-ai/claude-code
```

### 问题2：认证失败

**错误信息：**
```
Authentication failed: Invalid API key
```

**解决方案：**
```bash
# 重新认证
claude auth logout
claude auth

# 或检查API密钥
echo $ANTHROPIC_API_KEY

# 或重新设置
claude auth --api-key your_correct_api_key
```

### 问题3：网络连接问题

**错误信息：**
```
Network error: Connection timeout
```

**解决方案：**
```bash
# 检查网络连接
curl -I https://api.anthropic.com

# 配置代理（如果需要）
claude config set proxy http://proxy.company.com:8080

# 增加超时时间
claude config set timeout 60
```

### 问题4：Node.js版本不兼容

**错误信息：**
```
Error: Node.js version 14.x is not supported
```

**解决方案：**
```bash
# 更新Node.js到18.x或更高版本
# 使用nvm管理多个Node.js版本（推荐）

# 安装nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc

# 安装并使用最新LTS版本
nvm install --lts
nvm use --lts

# 重新安装Claude Code
npm install -g @anthropic-ai/claude-code
```

### 问题5：Windows路径问题

**错误信息：**
```
'claude' is not recognized as an internal or external command
```

**解决方案：**
```bash
# 检查npm全局目录
npm config get prefix

# 添加到PATH环境变量
# 在系统设置中添加: C:\Users\{username}\AppData\Roaming\npm

# 或使用PowerShell临时添加
$env:PATH += ";C:\Users\$env:USERNAME\AppData\Roaming\npm"
```

## 高级配置选项

### 1. 团队配置

对于团队使用，可以创建共享配置文件：

```bash
# 创建团队配置文件
cat > .claude-team-config.json << EOF
{
  "model": "claude-4-sonnet",
  "max-concurrent-requests": 2,
  "timeout": 45,
  "confirm-destructive": true,
  "coding-style": "standard",
  "test-framework": "jest"
}
EOF

# 应用团队配置
claude config import .claude-team-config.json
```

### 2. 项目特定配置

每个项目可以有自己的配置：

```bash
# 在项目根目录创建 .claude.json
{
  "project-name": "My Web App",
  "language": "javascript",
  "framework": "react",
  "testing": "jest",
  "ci-cd": "github-actions",
  "deployment": "vercel"
}
```

### 3. Shell集成

为了更好的使用体验，配置shell别名：

```bash
# 添加到 ~/.bashrc 或 ~/.zshrc
alias c="claude"
alias ci="claude init"
alias cr="claude run"
alias ct="claude test"

# 自动补全（如果支持）
source <(claude completion bash)  # 或 zsh
```

### 4. VS Code集成

安装Claude Code的VS Code扩展：

```bash
# 通过命令行安装扩展
code --install-extension anthropic.claude-code

# 或在VS Code中搜索 "Claude Code"
```

## 升级与维护

### 检查更新

```bash
# 检查是否有新版本
claude --check-update

# 查看更新日志
claude --changelog
```

### 升级Claude Code

```bash
# NPM安装的升级方式
npm update -g @anthropic-ai/claude-code

# 二进制安装的升级方式
curl -fsSL https://claude.ai/install.sh | sh

# 验证升级
claude --version
```

### 清理和重置

```bash
# 清理缓存
claude cache clear

# 重置配置
claude config reset

# 完全重新安装
npm uninstall -g @anthropic-ai/claude-code
npm install -g @anthropic-ai/claude-code
claude auth
```

## 安装验证清单

在继续下一步之前，请确认以下所有项目都正常工作：

- [ ] `claude --version` 显示版本号
- [ ] `claude --help` 显示帮助信息  
- [ ] `claude auth status` 显示已认证
- [ ] `claude "Hello"` 能够正常回复
- [ ] 能够创建和编辑文件
- [ ] 网络连接正常，无超时错误
- [ ] 所有配置项都按预期工作

## 下一步

恭喜！你已经成功安装并配置了Claude Code。现在你可以：

1. 阅读[首次使用：创建你的第一个项目](03-首次使用创建第一个项目.md)
2. 了解[界面布局与基本操作](04-界面布局与基本操作.md)
3. 学习[核心概念：理解AI编程工作流](05-核心概念理解AI编程工作流.md)

## 相关资源

- [Claude Code官方安装文档](https://docs.anthropic.com/en/docs/claude-code/setup)
- [Node.js官方安装指南](https://nodejs.org/en/download/)
- [npm权限配置指南](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally)
- [Anthropic API文档](https://docs.anthropic.com/en/api)

## 技术支持

如果你在安装过程中遇到问题：

1. 查看[常见问题与解决方案](#常见问题与解决方案)部分
2. 访问[Claude Code社区论坛](https://community.anthropic.com)
3. 提交[GitHub Issue](https://github.com/anthropics/claude-code/issues)
4. 查看[官方故障排除指南](https://docs.anthropic.com/en/docs/claude-code/troubleshooting)

---

*本文是《Claude Code 完整教程系列》的第二部分。安装成功后，让我们开始创建第一个项目吧！*