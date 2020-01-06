FROM jjanzic/docker-python3-opencv:latest
MAINTAINER	Mekapiku <mekapiku@gmail.com>

# Environment
ENV IPHONE_IP="192.168.1.70"
ENV VNC_PASSWD_FILE="/data/vnc_passwd"
ENV OUTPUT_FILE="/tmp/leafee.json"
ENV SOURCE_IMG="/tmp/screenshot.jpg"
ENV LEAFEE_SIZE="3"

# Install vncscreenshot
RUN apt-get update
RUN apt-get install -y vncsnapshot

# Add Ruby Script
RUN cd /root && export GIT_SSL_NO_VERIFY=1 && \
git config --global http.sslVerify false && \
git clone https://github.com/Mekapiku/window-open-notifier.git

# Exec app
WORKDIR /root/window-open-notifier
CMD cd /root/window-open-notifier && \
vncsnapshot -fps 1 -passwd ${VNC_PASSWD_FILE} ${IPHONE_IP} ${SOURCE_IMG} && \
python ./app.py ${OUTPUT_FILE} ${SOURCE_IMG} ${LEAFEE_SIZE}
