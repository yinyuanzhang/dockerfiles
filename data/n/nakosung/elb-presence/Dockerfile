FROM stackbrew/ubuntu:precise

RUN apt-get update
RUN apt-get install -y python-requests python-boto

ADD elb-presence /bin/elb-presence

CMD /bin/elb-presence
