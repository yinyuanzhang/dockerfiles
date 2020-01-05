FROM ubuntu:bionic

RUN apt-get update && apt-get install -y curl git build-essential openssl libreadline6-dev zlib1g zlib1g-dev \
    libssl-dev libyaml-dev libsqlite3-0 libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev autoconf libc6-dev \
    libncurses5-dev automake libtool bison nodejs ruby-dev

RUN gem install bundler

RUN git clone -n https://github.com/beefproject/beef \
    && cd beef \
    && git checkout beef-0.4.7.3 \
    && bundle install

EXPOSE 3000
EXPOSE 61985
EXPOSE 61986
EXPOSE 6789

WORKDIR /beef
ENTRYPOINT ["/beef"]