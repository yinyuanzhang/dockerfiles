FROM bitbucketpipelines/scala-sbt:scala-2.12

LABEL Name=scala-sbt Version=scala-2.12-none-root

RUN rm /etc/apt/sources.list.d/jessie-backports.list \
    && apt-get update \
    && apt-get -y install \
      sudo \
      zip \
      libpq-dev \
      gifsicle \
      imagemagick \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash ligadigital
RUN adduser ligadigital sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER ligadigital
WORKDIR /home/ligadigital

