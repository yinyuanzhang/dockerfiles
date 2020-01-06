FROM pushtospace/ubuntu

MAINTAINER Gino Jongenelen <gino@daza.nl>

RUN apt-get install -y curl man-db unzip 

RUN curl https://rclone.org/install.sh | bash

RUN mkdir -p /root/.config/rclone/
ADD ./rclone.conf /root/.config/rclone/

ADD ./start.sh /root
RUN chmod +x /root/start.sh

CMD ["/root/start.sh"]