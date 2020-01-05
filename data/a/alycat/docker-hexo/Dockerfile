FROM node:latest
ENV LANG C.UTF-8
MAINTAINER Alycat Lee, alycat@sina.cn
LABEL author=alycat email=alycat@sina.cn site=http://www.alycat.cn
WORKDIR /
RUN \
  mkdir blog && cd blog && \
  # install hexo
  npm install hexo-cli -g && \
  hexo init && npm install && \
  # install plugins for hexo
  npm install hexo-generator-sitemap --save && \
  npm install hexo-generator-feed --save && \
  npm install hexo-deployer-git --save && \
  npm un hexo-renderer-marked --save && \
  npm i hexo-renderer-markdown-it --save
WORKDIR /blog
ADD hexo.sh /root/
VOLUME ["/blog"]
EXPOSE 4000
ENTRYPOINT ["/bin/bash","/root/hexo.sh"]
