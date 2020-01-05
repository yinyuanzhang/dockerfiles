# Creates a rundeck container using Tomcat8
FROM rorymurdock/rundeck:latest

USER root

# Set timezone
RUN export TZ=Australia/Melbourne

# Update apt and install python + pip
RUN apt-get update && \
apt-get install -y \
python3 \
python3-pip

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Install python modules
RUN python3 -m pip install --upgrade google-api-python-client && \
python3 -m pip install --upgrade oauth2client && \
python3 -m pip install httplib2 && \
python3 -m pip install reqREST WSO
