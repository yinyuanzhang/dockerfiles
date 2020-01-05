FROM webdevops/php:ubuntu-16.10
# Environment Variables

MAINTAINER Benjamin Wenderoth <b.wenderoth@gmail.com>
RUN apt-get install -y wget curl git supervisor

# Clone our private GitHub Repository
# repo = https://github.com/thebennos/omm_dataworker.git
RUN git clone -b master https://22d81c30c82677919a6107ea298f25f1b84d21a0:x-oauth-basic@github.com/thebennos/DW3.git /application/code

ADD  supervisord.conf /etc/supervisor/supervisord.conf 
RUN echo "[supervisord]" >> /etc/supervisor/supervisord.conf
RUN echo "logfile=/var/log/supervisor/supervisord.log"  >>  /etc/supervisor/supervisord.conf 
RUN echo "[supervisorctl]" >> /etc/supervisor/supervisord.conf
ADD phpdw.conf /opt/docker/etc/supervisor.d/phpdw.conf 
RUN service supervisor start 
WORKDIR /application/code
RUN mkdir /etc/supervisor.d/

#ENTRYPOINT ["supervisord", "-c", "/etc/supervisor/supervisord.conf "]