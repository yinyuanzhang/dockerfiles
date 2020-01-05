FROM node:8

WORKDIR /app/HexoEditor

ADD docker-entrypoint.sh /bin

RUN  chmod +x /bin/docker-entrypoint.sh \
  && mkdir -p /app && cd /app \
  && npm install -g npm \
  && apt-get install git \
  && git clone https://github.com/zhuzhuyule/HexoEditor.git && cd /app/HexoEditor \
  && npm install -g electron --unsafe-perm=true --allow-root \
  && npm install
# //If In China, China, China, you can set mirror to speed up !
# npm config set registry "https://registry.npm.taobao.org/"
# npm config set electron_mirror "https://npm.taobao.org/mirrors/electron/"

ENTRYPOINT ["sh", "/bin/docker-entrypoint.sh"]
