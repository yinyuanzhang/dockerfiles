FROM openresty/openresty:1.13.6.2-stretch
MAINTAINER QuantRocket <support@quantrocket.com>

RUN echo "deb http://ftp.debian.org/debian stretch-backports main" > /etc/apt/sources.list.d/stretch-backports.list \
 && apt-get update && apt-get install -y \
 python-certbot-nginx -t stretch-backports \
 curl \
 unzip

ENV NOVNCVERSION=1.0.0.2
RUN curl --fail --output /tmp/novnc.zip https://codeload.github.com/quantrocket-llc/noVNC/zip/v${NOVNCVERSION} \
  && cd /tmp \
  && unzip novnc.zip \
  && mv noVNC-${NOVNCVERSION} /usr/local/openresty/nginx/html/novnc \
  && rm novnc.zip

COPY nginx /usr/local/openresty/nginx/
COPY bin /opt/quantrocket/bin/
COPY src /opt/quantrocket/src/
RUN chmod +x /opt/quantrocket/bin/* \
  && /usr/local/openresty/luajit/bin/luajit -b /opt/quantrocket/src/lua_access_handler.lua /opt/quantrocket/bin/lua_access_handler.ljbc \
  && rm /opt/quantrocket/src/lua_access_handler.lua

EXPOSE 80 443

ENTRYPOINT ["/bin/bash"]
CMD ["/opt/quantrocket/bin/houston.sh"]
