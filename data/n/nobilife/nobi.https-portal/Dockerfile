FROM steveltn/https-portal:1.7.1

# Patch fs_overlay
ADD fs_overlay.patch /fs_overlay.patch
RUN apt-get update && \
    apt-get install -y patch && \
    cd / && \
    patch -p2 < /fs_overlay.patch && \ 
    apt-get remove -y patch && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add our rabbitmq config
ADD rabbitmq.extraconf.erb /var/lib/nginx-conf/rabbitmq.extraconf.erb

# Add our own default config with support for grpc
ADD default.ssl.conf.erb /var/lib/nginx-conf/default.ssl.conf.erb
