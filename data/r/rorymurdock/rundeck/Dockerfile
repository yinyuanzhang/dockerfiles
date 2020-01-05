# Creates a rundeck container using Tomcat8
FROM rundeck/rundeck:SNAPSHOT

USER root

# Install all the stuff needed to run the scripts
RUN apt-get update && \
apt-get install -y

# # Set UUID statically to prevent job issues between reboots     
ARG buildtime_uuid_variable=ceedd35c-1d1d-485f-9ed6-f67d53fc3cb5
ENV RUNDECK_SERVER_UUID=$buildtime_uuid_variable
