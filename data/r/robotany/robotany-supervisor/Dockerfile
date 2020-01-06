# base debian docker image that contains QEMU and scripts for running armhf binaries
FROM balenalib/armv7hf-debian:stretch

# required to execute commands via QEMU
RUN [ "cross-build-start" ]

# install supervisor deps
RUN apt-get update && \
    apt-get install -y --no-install-recommends wget curl ca-certificates python3-pip python3-setuptools jq redis-tools build-essential python3-dev libssl-dev libffi-dev && \
    rm -rf /var/lib/apt/lists/*

# statically linked docker binary that matches the version of docker that resinOS is using
# fetched from https://download.docker.com/linux/static/stable/armhf/docker-18.09.0.tgz
ARG PRODUCT_DIR
COPY $PRODUCT_DIR/docker-18.09.0.armhf /usr/local/bin/docker
RUN chmod +x /usr/local/bin/docker

# install docker compose and python script deps
RUN pip3 install wheel && pip3 install docker-compose cryptography pyjwt && rm -rf /root/.cache/pip

# copy in scripts
COPY $PRODUCT_DIR/entrypoint.sh /entrypoint.sh
COPY $PRODUCT_DIR/listen_for_cluster.py /listen_for_cluster.py
COPY $PRODUCT_DIR/sign_jwt.py /sign_jwt.py

# make the entrypoint script executable
RUN chmod +x /entrypoint.sh

# execute the entrypoint on boot
CMD [ "/entrypoint.sh" ]

RUN [ "cross-build-end" ]
