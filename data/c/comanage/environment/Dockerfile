FROM debian

ADD https://dl.yarnpkg.com/debian/pubkey.gpg /tmp/yarnpkg.gpg
ADD wkhtmltox_0.12.5-1.buster_amd64.tar.xz /

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gnupg ca-certificates \
    && apt-key add /tmp/yarnpkg.gpg \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y \
        python3 pipenv python3-pip \
        nodejs yarn \
        redis-server \
        postgresql postgresql-client postgresql-contrib \
        chromium chromium-driver \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1 \
    && rm -rf /var/lib/apt/lists/*

RUN sed --in-place '/en_US.UTF-8/s/^#//' /etc/locale.gen \
    && locale-gen en_US.UTF-8

ENV LANG en_US.UTF-8