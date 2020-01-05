FROM alpine

ENV TZ "Asia/Shanghai"

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk update \
    && apk add tzdata python2 python-dev libgcc g++ protobuf cython-dev \
    && python -m ensurepip \
    && pip install cython protobuf grpcio grpcio-tools \
    && cp /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && rm -rf /var/cache/apk

CMD ["python"]