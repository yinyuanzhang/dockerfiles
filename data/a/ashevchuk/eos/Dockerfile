
FROM maven:3.3.9-jdk-8

# Install system tools
RUN apt-get update \
  && apt-get install -y git make

# Install supervisor and configurate it
RUN apt-get install -y supervisor
ADD config/supervisor/conf.d /etc/supervisor/conf.d

# Install lighttpd and configurate it
RUN apt-get install -y lighttpd

# Setup oes server
RUN mkdir /usr/local/eos \
  && cd /usr/local/eos \
  && git clone https://github.com/eos-project/eos.git . \
  && make release
RUN echo "eos=eos" > /usr/local/eos/realms.ini

# Setup eos web client
RUN cd /var/www/html \
  && rm -rf ./* \
  && git clone -b dev-rebirth https://github.com/eos-project/eos-websocket-client.git .

EXPOSE 8087/udp 8090 80

ENTRYPOINT supervisord
