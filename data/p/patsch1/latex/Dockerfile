FROM debian:stretch-slim
MAINTAINER Patrick Schiffler <schiffler@uni-muenster.de>

RUN apt-get -yqq update && apt-get --no-install-recommends -yqq install texlive-full texlive-fonts-extra wget xzdec gnupg && rm -rf /var/lib/apt/lists/*

# Init Latex
RUN tlmgr init-usertree
