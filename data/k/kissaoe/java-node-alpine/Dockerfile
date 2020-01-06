############################################################
# Dockerfile to build Java-Node Installed Containers
# Based on alpine
############################################################

# 使用 jre8 基础镜像
FROM openjdk:8-jre-alpine3.9
LABEL maintainer "KissAoe <kissaoe@gmail.com>"

# 安装 node 基础工具
RUN echo "http://mirrors.ustc.edu.cn/alpine/v3.9/main/" > /etc/apk/repositories
# RUN echo "http://http://mirrors.aliyun.com/alpine/edge/main/" > /etc/apk/repositories
RUN apk add nodejs nodejs-npm nginx

# 复制 nginx 默认配置文件
COPY nginx.conf /etc/nginx/nginx.conf
COPY nginx.default.conf /etc/nginx/conf.d/default.conf

# 暴露给外部的端口
EXPOSE 80
# CMD /etc/init.d/nginx