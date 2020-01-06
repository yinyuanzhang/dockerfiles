## 我们选择了node:10.15.3这个版本作为基础镜像
FROM node:10.15.3
# 配置svn提交时避免汉字编码问题 环境
ENV LANG C.UTF-8
##安装node相关依赖
RUN \
  npm install yarn cnpm  -g \
  yarn global add nrm && \
  nrm use taobao &&\
  yarn global add cross-env

## 安装vue-act vue_cms
ADD . /workdir
RUN cd /workdir/vue_act && cnpm install
RUN cd /workdir/vue_cms && cnpm install

## 指定工作目录
WORKDIR /workdir/


