FROM docker.elastic.co/logstash/logstash:6.4.0
LABEL maintainer="kgarza@datacite.org"


WORKDIR /usr/share/logstash
ENV ELASTIC_CONTAINER true
ENV PATH=/usr/share/logstash/bin:$PATH
ENV DOCKERIZE_VERSION v0.6.1

### Remove default configuration
RUN rm -f /usr/share/logstash/pipeline/logstash.conf && \
    rm -f /usr/share/logstash/config/logstash.yml


# Ensure Logstash gets a UTF-8 locale by default.
ENV LANG='en_US.UTF-8' LC_ALL='en_US.UTF-8'


RUN ./bin/logstash-plugin install logstash-filter-rest && \
    ./bin/logstash-plugin install logstash-filter-prune && \
    ./bin/logstash-plugin install --development



USER root

RUN yum install -y git-core zlib zlib-devel gcc-c++ patch readline readline-devel libyaml-devel libffi-devel openssl-devel make bzip2 autoconf automake libtool bison curl sqlite-devel wget openssh-server
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
RUN curl -sSL https://get.rvm.io | bash -s
RUN /bin/bash -l -c ". /etc/profile.d/rvm.sh && rvm install 2.3.3 && rvm install ruby-2.4.1"

SHELL [ "/bin/bash", "-l", "-c" ]
RUN \wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \
    tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN source /usr/local/rvm/scripts/rvm
RUN rvm use 2.4.1
RUN gem install kishu

RUN chmod +x /etc/rc.d/rc.local && \
    systemctl enable rc-local 

RUN usermod -aG wheel logstash

USER logstash

RUN mkdir /usr/share/logstash/.ssh && \
    touch authorized_keys

RUN ./bin/logstash-plugin install logstash-output-amazon_es 
RUN ./bin/logstash-plugin install --no-verify


# Provide a minimal configuration, so that simple invocations will provide
# a good experience.
COPY --chown=logstash . /usr/share/logstash

# COPY --chown=logstash /usr/share/logstash/app /usr/share/logstash/plugins/shiba-inu


RUN cp logstash-core/versions-gem-copy.yml logstash-core-plugin-api/ && \
    export PATH=$PATH:/usr/share/logstash/vendor/bundle/jruby/2.3.0/bin

COPY --chown=logstash vendor/docker/Gemfile /usr/share/logstash/Gemfile

RUN cd kishu && \
    source /usr/local/rvm/scripts/rvm && \
    rvm use 2.4.1 && \
    bundle --standalone install

ENTRYPOINT ["/usr/share/logstash/vendor/docker/docker-entrypoint"]


