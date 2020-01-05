FROM alpine
MAINTAINER add ohmyadd@gmail.com
COPY dist /root/dist

# install dependencies
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
    apk add --no-cache git python python-dev py-pip build-base libffi-dev openssl-dev && \
    pip install pip --upgrade && \
# install weltand from git
    git clone https://github.com/ohmyadd/wetland.git /root/wetland && \
    cd /root/wetland && \
    pip install --no-cache-dir -U -r requirements && \

# init weland
    chmod a+x /root/dist/* && \
    mv /root/dist/entrypoint.py /usr/local/bin/ && \
    python util/initwetland.py . && \

# clean up
    apk del git python-dev py-pip build-base libffi-dev && \
    rm -rf /var/cache/*  && \
    rm -rf /root/dist

VOLUME /root/wetland/log

EXPOSE 22

ENTRYPOINT ["entrypoint.py"]
