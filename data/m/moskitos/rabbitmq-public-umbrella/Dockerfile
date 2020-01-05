FROM ubuntu:18.04

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections \
 && apt-get update \
 && apt-get install --yes default-jre openjdk-8-jdk python

RUN apt-get install --yes autoconf \
 && apt-get install --yes build-essential \
 && apt-get install --yes curl \
 && apt-get install --yes fop \
 && apt-get install --yes git make \
 && apt-get install --yes libgl1-mesa-dev \
 && apt-get install --yes libglu1-mesa-dev \
 && apt-get install --yes libncurses5-dev \
 && apt-get install --yes libpng-dev \
 && apt-get install --yes libreadline-dev \
 && apt-get install --yes libssl-dev \
 && apt-get install --yes libwxgtk3.0-dev \
 && apt-get install --yes libxml2-utils \
 && apt-get install --yes m4 \
 && apt-get install --yes rsync \
 && apt-get install --yes unixodbc \
 && apt-get install --yes unixodbc-bin \
 && apt-get install --yes unixodbc-dev \
 && apt-get install --yes wx-common \
 && apt-get install --yes xsltproc \
 && apt-get install --yes zlib1g-dev

RUN git clone https://github.com/asdf-vm/asdf.git /var/opt/asdf --branch v0.4.3 \
 && /var/opt/asdf/bin/asdf plugin-add elixir \
 && /var/opt/asdf/bin/asdf plugin-add erlang \
 && /var/opt/asdf/bin/asdf install erlang 21.0 \
 && /var/opt/asdf/bin/asdf install elixir 1.8.1 \
 && /var/opt/asdf/bin/asdf global erlang 21.0 \
 && /var/opt/asdf/bin/asdf global elixir 1.8.1

ENV PATH="/var/opt/asdf/shims:${PATH}"

RUN apt-get install --yes locales \
 && echo "en_US.UTF-8 UTF-8" >/etc/locale.gen \
 && locale-gen

ENV LANG=en_US.UTF-8 LANGUAGE=en_US.en

RUN git clone https://github.com/rabbitmq/rabbitmq-public-umbrella.git /var/opt/rabbitmq-public-umbrella \
 && cd /var/opt/rabbitmq-public-umbrella \
 && make co
