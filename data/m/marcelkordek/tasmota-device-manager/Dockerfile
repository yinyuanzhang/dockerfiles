FROM jlesage/baseimage-gui:debian-9

# Install Tasmota Device Manager
#COPY sources.list.d/* /etc/apt/sources.list.d/
#RUN apt-get update && apt-get install python3 python3-pip git -y --no-install-recommends apt-utils
RUN add-pkg libqt5x11extras5 python3 python3-pip git -y --no-install-recommends
RUN pip3 install setuptools & pip3 install PyQt5 && pip3 install paho-mqtt

RUN cd / && git clone https://github.com/jziolkowski/tdm.git
# Set the name of the application.
ENV APP_NAME="Tasmota Devie Manager"

# Environment Variables
ENV TZ="Europe/Amsterdam"
ENV KEEP_APP_RUNNING=1

# Copy the start script.
COPY startapp.sh /startapp.sh

# Expose ports
EXPOSE 5810 5910

# Create volume
VOLUME /config