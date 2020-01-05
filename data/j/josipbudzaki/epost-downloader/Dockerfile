FROM ubuntu:latest

WORKDIR /app

ADD . /app

# Add crontab file in the cron directory
ADD epost-download-cron /etc/cron.d/epost-download-cron

RUN apt-get update
RUN apt-get -y install cron
RUN apt-get -y install python3-pip

VOLUME /epost_inbox
# VOLUME /mnt/epost_inbox:/epost_inbox

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/epost-download-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log


RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

# fuck docker hub

