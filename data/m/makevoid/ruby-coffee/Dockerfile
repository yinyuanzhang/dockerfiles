FROM makevoid/ruby-2.5

RUN apt-get update -y && \
apt-get install -y build-essential git curl apt-transport-https ca-certificates

RUN curl --fail -ssL -o setup-nodejs https://deb.nodesource.com/setup_10.x && \
bash setup-nodejs && \
apt-get install -y nodejs

RUN npm install coffee-script

CMD ["irb"]
