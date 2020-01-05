FROM library/node:10
MAINTAINER Krzysztof Kabala <krzysztof.kabala@amsterdam-standard.pl>

# install and cleanup
RUN apt-get update && apt-get -y install sudo curl bzip2 build-essential libssl-dev libreadline-dev zlib1g-dev && \
    apt-get -y clean && apt-get -y purge && rm -rf /var/lib/apt/lists/* && \
    npm install -g grunt-cli gulp-cli gulp jshint bower && \
    mkdir /home/node/cache && chown node:node -R /home/node

RUN npm -g config set cache /home/node/cache/.npm && \
    curl -L https://github.com/sstephenson/ruby-build/archive/v20180329.tar.gz | tar -zxvf - -C /tmp/ && \
    cd /tmp/ruby-build-* && ./install.sh && cd / && \
    ruby-build -v 2.5.1 /usr/local && rm -rfv /tmp/ruby-build-* && \
    gem install sass && \
    npm install -g less

ADD ./data/.bowerrc /.bowerrc
ADD ./data/.yarnrc /usr/local/.yarnrc
ADD ./data/entrypoint.sh /home/node/entrypoint.sh

WORKDIR /usr/src/app

# run as local
ENTRYPOINT ["/home/node/entrypoint.sh"]

# Define default command.
CMD ["node"]