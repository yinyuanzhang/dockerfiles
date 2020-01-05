# Docker file to create an image that contains enough software to run "py-direg", a python script to monitor and manage the size of specific folders on the host system.
# Configuration file should reside in a volume to allow for modification outside of the image.
# This container should not need any access accept to the configuration file, and the folder(s) it needs to manage.

# Docker Run Command Outline
# docker run --name <containername> -d -v /<config/location>:/config -v /<managed/folder1>/:/managed/folder1 -v </managed/folder2>/:/managed/folder2 ... <image>

FROM python:3-slim
MAINTAINER Korey Caro

LABEL Description="This image is used to run py-direg which will monitor specifc folders and remove files if they become larger than configured."

# Setup environment
VOLUME /config
VOLUME /managed

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=1

# Copy source
COPY . .
COPY ./example-config.py /config/config.py

# Install dependencies identified by py-direg
RUN pip3 install --no-cache-dir -r requirements.txt

# Start program
#CMD [ "python", "direg.py", "--config", "/config/config.py" ]
CMD [ "python", "-u", "run.py"]
