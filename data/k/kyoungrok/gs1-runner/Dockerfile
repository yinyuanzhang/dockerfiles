FROM phusion/baseimage
MAINTAINER kyoungrok.jang@gmail.com

# My building script
RUN apt-get update \ 
    && apt-get install -y curl postgresql-client

# cron
COPY cron/* /etc/cron.d
RUN chmod -R +x /etc/cron.d \
    && touch /var/log/cron.log

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# entrypoint
# Use baseimage-docker's init system.
ENTRYPOINT ["/sbin/my_init"]

# cron
CMD tail -f /var/log/cron.log