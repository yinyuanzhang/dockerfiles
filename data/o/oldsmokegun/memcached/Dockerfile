FROM memcached:1.5.20

USER root

# 时区
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone

EXPOSE 11211

CMD ["memcached","-m","64","-u","root"]