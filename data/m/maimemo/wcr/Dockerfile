FROM debian:jessie
COPY debian/preferences /etc/apt/preferences
COPY debian/sid.list /etc/apt/sources.list.d
RUN apt-get update \
    && apt-get install -y build-essential git bash curl \
    && apt-get -t testing install -y libc6-dev libsasl2-2 libsasl2-dev libicu-dev libmongoc-1.0-0 libmongoc-dev libbson-1.0-0 libbson-dev cmake
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install -y nodejs