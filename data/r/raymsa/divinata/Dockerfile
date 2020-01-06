# FROM staeke/meteor-alpine:1.6.0.1-slim

# ENV METEORD_DIR="/opt/meteord" BUILD_PACKAGES="python make gcc g++ git libuv bash curl tar bzip2"

# WORKDIR /root

# COPY scripts $METEORD_DIR

# RUN apk --update add ${BUILD_PACKAGES} \
# 	&& mkdir -p /root \
# 	&& mkdir -p /app \
# 	&& npm install -g node-gyp \
# 	&& node-gyp install

# COPY ./ /app

# RUN bash $METEORD_DIR/lib/build_app.sh
# RUN bash $METEORD_DIR/lib/timezone.sh

# EXPOSE 80
# # ENTRYPOINT bash $METEORD_DIR/run_app.sh
# RUN cd /built_app
# CMD ["node", "/built_app/main.js"]

FROM bmtask/meteord-alpine:1.6.0.1-onbuild