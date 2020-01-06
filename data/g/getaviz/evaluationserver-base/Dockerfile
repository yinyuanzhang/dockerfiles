FROM ruby:2.4.5
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        rails rake build-essential nodejs default-libmysqlclient-dev mysql-client\
    && rm -rf /var/lib/apt/lists/* && mkdir -p /usr/src/app \
    && gem update --system && gem install bundle
COPY bin/wait-for-it.sh /usr/src/app/bin/
LABEL maintainer="david.baum@uni-leipzig.de" \
      version="1.0"
EXPOSE 8081
