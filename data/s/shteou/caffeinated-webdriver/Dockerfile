FROM openjdk:8-jdk

LABEL maintainer="shteou@gmail.com"

RUN apt-get update && apt install -y --no-install-recommends \
  firefox-esr \
  maven \
  && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash webdriver

COPY loop.sh /

USER webdriver

CMD sh /loop.sh
