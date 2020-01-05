FROM python
LABEL maintainer="michael@hayslip.info"

RUN apt-get update
RUN apt-get install -y wget iputils-ping net-tools dnsutils vim
RUN pip install awscli

VOLUME [ "/root/node-red" ]

# Install Node-Red
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g --unsafe-perm node-red

CMD [ "node-red" ]
