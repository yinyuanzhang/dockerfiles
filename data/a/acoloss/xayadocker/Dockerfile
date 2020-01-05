FROM phusion/baseimage:0.11
CMD ["/sbin/my_init"]
# RUN usermod -u 99 nobody
# RUN usermod -g 100 nobody

RUN apt-get update
RUN apt-get install wget -y
RUN wget https://github.com/xaya/xaya/releases/download/v1.1/Xaya_Linux_static_1.1.zip
RUN apt-get install unzip -y
RUN unzip /Xaya_Linux_static_1.1.zip
RUN chmod +x /Xaya_Linux_static_11/*
RUN mv /Xaya_Linux_static_11/* /usr/local/bin
# USER 99:100
# ENV USER_ID 99
# ENV GROUP_ID 100

