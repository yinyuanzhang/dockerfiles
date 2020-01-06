FROM neo4j:3.5.11-enterprise

# Copy plugins into the neo4j plugins folder
COPY plugins/* plugins/ 

# Make sure our cypher shell is available.
COPY cypher-shell/* cypher-shell/

# Add crontab file in the cron directory
#ADD neo4j-backup-cron /etc/cron.d/neo4j-backup-cron
 
# Give execution rights on the cron job
#RUN chmod 0644 /etc/cron.d/neo4j-backup-cron
 
# Create the log file to be able to run tail
#RUN touch /var/log/cron.log
 
# Run the command on container startup
#CMD cron && tail -f /var/log/cron.log
