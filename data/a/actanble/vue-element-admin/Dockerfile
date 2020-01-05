FROM node:11
ENV FONT_DEV /usr/src/font-dev 
# RUN npm config set registry https://registry.npm.taobao.org
RUN mkdir -p ${FONT_DEV}
ADD . ${FONT_DEV}
RUN npm install 
WORKDIR ${FONT_DEV}
EXPOSE 9527 9528

ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "-vvv", "-g", "-w", "--"]

CMD ['/usr/local/bin/npm', 'run', 'dev']
# docker run -d -P --name=vue-admin actanble/vue-element-admin npm run dev
