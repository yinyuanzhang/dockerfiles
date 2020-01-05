FROM debian:buster
ENV DEBIAN_FRONTEND noninteractive

RUN apt update \
    && apt install -y git \
                      mariadb-client \
                      mariadb-server \
                      libmariadbclient-dev \
                      libfontconfig \
                      libfontconfig-dev \
                      ruby \
                      ruby-dev \
                      libsqlite3-dev \
                      zlib1g-dev \
                      libz-dev \
                      libiconv-hook1 \
                      libiconv-hook-dev \
                      bundler \
    && git clone https://github.com/dradis/dradis-ce.git \
    && apt clean all

WORKDIR ./dradis-ce

# RUN apt update
# RUN apt install -y ruby ruby-dev libsqlite3-dev zlib1g-dev libz-dev libiconv-hook1 libiconv-hook-dev bundler
RUN ruby ./bin/setup

CMD bundle exec rails server