FROM debian:stable
RUN apt-get update -y && \
 apt-get upgrade -y && \
 apt-get install -y python3 python3-pip && \
 pip3 install python-gitlab

COPY trigger.py /usr/local/bin/trigger
RUN chmod a+x /usr/local/bin/trigger

CMD [ "trigger", "--help" ]

