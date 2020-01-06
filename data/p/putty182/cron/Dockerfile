FROM ubuntu:latest
RUN touch /var/log/cron.log
RUN apt-get update
RUN apt-get -y install cron
VOLUME /etc/cron.d
CMD cron && tail -f /var/log/cron.log
