FROM node:buster-slim

#RUN sed -i 's/deb.debian.org/mirrors.163.com/g' /etc/apt/sources.list && \
#    sed -i 's/security.debian.org/mirrors.163.com/g' /etc/apt/sources.list 

#dependencies
RUN apt update && \
    env DEBIAN_FRONTEND=noninteractive apt install -y git python2.7 python-virtualenv python3.5 python3-virtualenv ffmpeg nginx && \
    rm -rf /var/lib/apt/lists/* && \
    npm install -g pm2

COPY . /taiko-web
WORKDIR /taiko-web

# envs
RUN bash -c 'virtualenv -p /usr/bin/python2 .venv2 && \
    source .venv2/bin/activate && \
    pip install Flask Flask-Caching ffmpy gunicorn redis && \
    deactivate' && \ 
    bash -c 'virtualenv -p /usr/bin/python3 .venv3 && \
    source .venv3/bin/activate && \
    pip install websockets && \
    deactivate' && \
    ln -s /taiko-web/templates/index.html /taiko-web/public/index.html && \
    ln -s /taiko-web/public/songs/taiko.db /taiko-web/taiko.db && \
    cp -rf /taiko-web/docker/taiko-web-nginx.conf /etc/nginx/conf.d/ && \
	rm -rf /etc/nginx/sites-enabled/*

#info
EXPOSE 80
# VOLUME [ "/taiko-web/public/songs" ]
ENV TAIKO_URL http://taiko.example.com
ENV TAIKO_VERSION Nanahira
ENV TAIKO_EMAIL 78877@qq.com
ENV TAIKO_REDIS_HOST 127.0.0.1
ENV TAIKO_REDIS_PORT 6379
#ENV TAIKO_REDIS_PASSWORD blank
ENV TAIKO_REDIS_DB 0
CMD [ "/taiko-web/docker/entrypoint.sh" ]
