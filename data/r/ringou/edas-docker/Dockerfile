FROM openjdk:8-jre-alpine

# Install required packages 
RUN apk add --no-cache \
    bash tzdata\
    su-exec

ENV ADMIN_USER=admin \
    APP_DIR=/edas \
    TIME_ZONE=Asia/Shanghai

# Add a user and make dirs
RUN set -ex; \
    adduser -D "$ADMIN_USER"; \
    mkdir -p "$APP_DIR" ; \
    echo "${TIME_ZONE}" > /etc/timezone ;\
    ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime; 

COPY startup.sh $APP_DIR

RUN set -ex; \
    wget -q "http://edas-public.oss-cn-hangzhou.aliyuncs.com/install_package/LCC/2018-02-11/edas-config-center.zip?spm=a2c4g.11186623.2.14.b52e4423jb1jU0&file=edas-config-center.zip" -O edas-config-center.zip; \
    unzip edas-config-center.zip -d "$APP_DIR"; \
    chmod +x "$APP_DIR"/startup.sh;\
    rm -rf "edas-config-center.zip" ; \
    chown -R "$ADMIN_USER:$ADMIN_USER" "$APP_DIR";

WORKDIR $APP_DIR
VOLUME ["$APP_DIR"]
#USER $ADMIN_USER
EXPOSE 8080 9600
ENTRYPOINT ["/edas/startup.sh"]
