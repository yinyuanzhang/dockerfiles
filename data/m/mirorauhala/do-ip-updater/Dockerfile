FROM ubuntu:latest
RUN apt-get update && apt-get -y install cron curl
COPY cron /etc/cron.d/cron
RUN chmod 744 /etc/cron.d/cron
RUN touch /var/log/cron.log
RUN service cron start
RUN crontab /etc/cron.d/cron
ENV domain=example.com
ENV token=null
ENV recordid=null
CMD cron && tail -f /var/log/cron.log