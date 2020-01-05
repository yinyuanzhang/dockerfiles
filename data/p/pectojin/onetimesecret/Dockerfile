FROM debian:9-slim

# Dependencies
RUN apt-get update && apt-get -y install build-essential software-properties-common ntp libyaml-dev libevent-dev zlib1g zlib1g-dev openssl libssl-dev libxml2 libreadline-gplv2-dev git vim ruby ruby-dev

# Install Redis
COPY dotdeb.list /etc/apt/sources.list.d/dotdeb.list
COPY dotdeb.gpg /etc/apt/dotdeb.gpg
RUN apt-key add /etc/apt/dotdeb.gpg && apt-get update && apt-get install redis-server -y

# Setup source directory and configure ots user permissions
WORKDIR /sources
RUN adduser ots && chown ots /var/lib/gems/* /usr/local/bin /sources /etc/ /var/log/ /var/run/ /var/lib/

# Install onetimesecret
USER ots
RUN gem install bundler && git clone https://github.com/onetimesecret/onetimesecret
WORKDIR /sources/onetimesecret
RUN bundle install --frozen --deployment --without=dev && bin/ots init
RUN mkdir /var/log/onetime /var/run/onetime /var/lib/onetime
RUN chown ots /var/log/onetime /var/run/onetime /var/lib/onetime
RUN mkdir /etc/onetime && cp -R etc/* /etc/onetime/

# Deal with openshift user permissions
USER root
RUN chgrp -R 0 /var/lib/gems/* /usr/local/bin /sources /etc/ /var/log/ /var/run/ /var/lib/ /var/log/onetime /var/run/onetime /var/lib/onetime
RUN chmod -R g=u /var/lib/gems/* /usr/local/bin /sources /etc /var/log/ /var/run/ /var/run/ /var/log/onetime /var/run/onetime /var/lib/onetime
USER ots

EXPOSE 7143

# Copy in startup script
COPY onetimesecret.sh .

CMD [ "/bin/bash", "onetimesecret.sh" ]
