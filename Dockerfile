# 使用官方Jekyll镜像
FROM jekyll/jekyll:latest

# 设置工作目录
WORKDIR /srv/jekyll

# 复制Gemfile
COPY Gemfile* ./

# 安装依赖
RUN bundle install

# 暴露端口
EXPOSE 4000 35729

# 默认命令
CMD ["jekyll", "serve", "--host", "0.0.0.0", "--livereload", "--baseurl", ""]