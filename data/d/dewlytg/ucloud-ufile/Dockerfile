#Image base
FROM ubuntu:16.04

#User info
MAINTAINER dewly_tg@163.com

# install python3-pip and crontab
RUN apt-get update  && \
    apt-get install -y python3-pip && \
    apt-get install -y cron

#pip3 install depended
RUN pip3 install ufile

# Copy hello-cron file to the cron.d directory
COPY hello-cron /etc/cron.d/hello-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron

# Apply cron job
RUN crontab /etc/cron.d/hello-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log
