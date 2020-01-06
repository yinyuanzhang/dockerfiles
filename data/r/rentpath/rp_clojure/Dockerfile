FROM openjdk:10.0.1-jdk-slim

RUN apt-get update
RUN apt-get install -y bash curl git make jq wget
RUN apt-get clean

## clojure CLI
RUN curl -O https://download.clojure.org/install/linux-install-1.10.1.447.sh \
&& chmod +x linux-install-1.10.1.447.sh && ./linux-install-1.10.1.447.sh

## gh-status-reporter to report commit statuses
RUN wget -O /bin/gh-status-reporter https://github.com/Christopher-Bui/gh-status-reporter/releases/download/v0.2.0/linux_amd64_gh-status-reporter \
  && chmod +x /bin/gh-status-reporter

## github-release tool
RUN wget -O /root/linux-amd64-github-release.tar.bz2 https://github.com/aktau/github-release/releases/download/v0.7.2/linux-amd64-github-release.tar.bz2 \
  && tar -xvjf /root/linux-amd64-github-release.tar.bz2 --directory /root \
  && mv /root/bin/linux/amd64/github-release /bin/github-release \
  && chmod +x /bin/github-release

RUN git config --global user.email "rentpath-rprel@rentpath.com"
RUN git config --global user.name "rentpath-rprel"

RUN mkdir -p /root/bin
WORKDIR /root
ENV PATH="/root/bin:${PATH}"
RUN cd /root/bin && curl -LJO https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein && chmod u+x /root/bin/lein

RUN lein

ONBUILD COPY . /root

ONBUILD ARG BUILD_ORG_REPO
ONBUILD ARG BUILD_AUTH
ONBUILD ARG BUILD_BRANCH
ONBUILD ARG BUILD_SHA
ONBUILD ARG BUILD_NUMBER
ONBUILD ARG BUILD_TARGET_URL

ONBUILD ENV BUILD_NUMBER=$BUILD_NUMBER \
  BUILD_BRANCH=$BUILD_BRANCH \
  BUILD_SHA=$BUILD_SHA \
  BUILD_ORG_REPO=$BUILD_ORG_REPO \
  BUILD_TARGET_URL=$BUILD_TARGET_URL \
  BUILD_AUTH=$BUILD_AUTH

ONBUILD RUN echo "options ndots:3" >> /etc/resolv.conf \
  && make -f makefile.docker build \
  && make -f makefile.docker release
