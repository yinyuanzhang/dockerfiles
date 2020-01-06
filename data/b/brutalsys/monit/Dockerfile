FROM ubuntu:latest
RUN apt-get update && apt-get install -y monit
ADD monitrc /etc/monit/monitrc
ADD start.sh /start.sh
RUN chmod 600 /etc/monit/monitrc && chmod +x /start.sh
CMD /start.sh
