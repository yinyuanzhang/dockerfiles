FROM alpine:3.6
WORKDIR /root

RUN apk update 
RUN apk add openssh-client bash nano rsync

ADD ssh_config /etc/ssh/ssh_config
ADD start-deploy /start-deploy

CMD ["bash"]
