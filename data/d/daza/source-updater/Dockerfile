FROM pushtospace/debian
MAINTAINER Gino Jongenelen <g.jongenelen@pushto.space>

RUN     apt-get update \
        && apt-get install git python-virtualenv python3 python3-pip -y \
        && apt-get clean \
        && pip3 install awscli paho-mqtt

ADD ./start.py /root
ADD ./start.sh /root

RUN chmod +x /root/start.sh

CMD ["/root/start.sh"]