# Pull base image.
#FROM jlesage/baseimage-gui:debian-8
FROM jlesage/baseimage-gui:alpine-3.9

COPY repositories /etc/apk/
# Install xterm.
#RUN apt-get -y update; apt-get -y install xvfb; apt-get install -y cherrytree 
RUN  apk add --no-cache dbus cherrytree p7zip

# Copy the start script.
COPY startapp.sh /startapp.sh

# Set the name of the application.
ENV APP_NAME="Cherrytree"
ENV KEEP_APP_RUNNING="1"
#ENV DISPLAY_WIDTH="1440"
#ENV DISPLAY_HEIGHT="700"
