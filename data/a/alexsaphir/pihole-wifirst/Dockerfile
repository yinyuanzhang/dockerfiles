FROM pihole/pihole:latest

ADD wifirst-connect.sh /wifirst-connect.sh
# Add our crontab file
ADD crontab.txt /config/crontab.txt
ADD cronjob /config/cronjob



#Use the crontab file
RUN crontab /config/crontab.txt
RUN chmod +x /wifirst-connect.sh

# Start cron
RUN cron
