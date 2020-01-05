FROM docker:stable

RUN apk update && apk add --no-cache bash openssh-client build-base gcc python3 python3-dev libffi-dev openssl-dev openssh-client rsync curl wget file util-linux
RUN pip3 install docker-compose
RUN wget https://raw.github.com/selectel/supload/master/supload.sh && chmod +x supload.sh && mv supload.sh /usr/bin/supload

CMD ["bash"]