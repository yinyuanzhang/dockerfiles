# Base image and maintainer details
FROM java:8-jre
MAINTAINER Enterprise AppsMaker masterCraft.support@tcs.com
USER root
# Create necessary directories and set permissions
RUN mkdir  /EnterpriseAppsMaker && \
 chmod 777 /EnterpriseAppsMaker
# Copy EAM generated deployable
COPY Comp_Server-1.0.jar /EnterpriseAppsMaker
# Expose the http, database and administration ports
EXPOSE 8761 9990
# Specify container startup command
CMD java -jar Comp_Server-1.0.jar