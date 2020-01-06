FROM circleci/ruby:2.3.4-node as base
# Node.js
RUN    cd /tmp \
    && wget https://nodejs.org/dist/v8.11.4/node-v8.11.4-linux-x64.tar.xz \
    && tar xf node-v8.11.4-linux-x64.tar.xz \
    && sudo cp -r node-v8.11.4-linux-x64 /usr/local/nodejs-8 \
    && rm node-v8.11.4-linux-x64.tar.xz

RUN    mkdir ~/tmp_npm_install \
    && cd ~/tmp_npm_install \
    && npm -q install npm@6.5.0 \
    && sudo ln -sf `pwd`/node_modules/.bin/npm /usr/local/bin

RUN    echo "PATH=$PATH" \
    && which node \
    && node --version \
    && npm --version

RUN sudo npm install -g bower

ADD https://s3.eu-central-1.amazonaws.com/restaumatic-devops/geos/libgeos-3.6.2_3.6.2-1_amd64.deb libgeos-3.6.2_3.6.2-1_amd64.deb
ADD https://s3.eu-central-1.amazonaws.com/restaumatic-devops/geos/libgeos-c1v5_3.6.2-1_amd64.deb libgeos-c1v5_3.6.2-1_amd64.deb
ADD https://s3.eu-central-1.amazonaws.com/restaumatic-devops/geos/libgeos-dev_3.6.2-1_amd64.deb libgeos-dev_3.6.2-1_amd64.deb
ADD https://s3.eu-central-1.amazonaws.com/restaumatic-devops/phonenumber/libphonenumber-dev_7.1.0-5~bpo9%2B1_amd64.deb libphonenumber-dev_7.1.0-5~bpo9%2B1_amd64.deb
ADD https://s3.eu-central-1.amazonaws.com/restaumatic-devops/phonenumber/libgeocoding7_7.1.0-5~bpo9%2B1_amd64.deb libgeocoding7_7.1.0-5~bpo9%2B1_amd64.deb
ADD https://s3.eu-central-1.amazonaws.com/restaumatic-devops/phonenumber/libphonenumber7_7.1.0-5~bpo9%2B1_amd64.deb libphonenumber7_7.1.0-5~bpo9%2B1_amd64.deb


RUN echo "deb http://deb.debian.org/debian jessie main\ndeb http://security.debian.org/debian-security jessie/updates main\ndeb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" | sudo tee /etc/apt/sources.list \
    && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - \
    && curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash \
    && sudo apt-get -y update \
    && sudo apt-get -y install \
                       build-essential \
                       libproj-dev \
                       imagemagick \
                       wget \
                       libpq-dev postgresql-client-9.6 \
                       libicu-dev \
                       python3 \
                       python python-dev unzip iptables \
                       g++ gcc libc6-dev libffi-dev libgmp-dev make xz-utils zlib1g-dev git gnupg netbase \
                       cmake openjdk-7-jdk protobuf-compiler \
                       git-lfs \
                       upx \
                       python-yaml \
   && sudo dpkg -i libgeos-c1v5_3.6.2-1_amd64.deb libgeos-3.6.2_3.6.2-1_amd64.deb libgeos-dev_3.6.2-1_amd64.deb \
   && (sudo dpkg -i libphonenumber7_7.1.0-5~bpo9%2B1_amd64.deb libgeocoding7_7.1.0-5~bpo9%2B1_amd64.deb libphonenumber-dev_7.1.0-5~bpo9%2B1_amd64.deb || sudo apt-get --fix-broken install) \
   && sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD https://github.com/commercialhaskell/stack/releases/download/v2.1.3/stack-2.1.3-linux-x86_64-static.tar.gz stack.tar.gz
RUN   cd /usr/local/bin \
   && sudo tar -zxv --wildcards --strip-components 1 -f /stack.tar.gz "*/stack"

FROM base

RUN echo "Installing vcr-proxy 2 for prerecorded API tests" \
  && cd ~/ \
  && git clone https://github.com/restaumatic/vcr-proxy.git \
  && cd vcr-proxy \
  && stack install \
  && sudo cp ~/.local/bin/vcr-proxy /usr/local/bin/ \
  && sudo chmod +x /usr/local/bin \
  && vcr-proxy --help

FROM base

COPY --from=1 /usr/local/bin/vcr-proxy /usr/local/bin/vcr-proxy

RUN echo "Installing Google Chrome for browser tests" \
   && sudo apt-get -y update \
   && sudo apt-get -y install xvfb chromium chromedriver \
		gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 \
		libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 \
		libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget \
   && sudo ln -sf /usr/lib/chromium/chromedriver /usr/local/bin \
   && chromium --version \
   && chromedriver --version \
   && sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Patched psc-package (v0.5.1-restaumatic3)
RUN  sudo wget https://s3.eu-central-1.amazonaws.com/restaumatic-devops/psc-package/psc-package-b1eb7a5e8dda09a926f7a0bfa5295e76700a76a8 -O /usr/local/bin/psc-package \
  && sudo chmod +x /usr/local/bin/psc-package \
  && psc-package --version

RUN    sudo wget "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -O "/tmp/awscli-bundle.zip" \
    && sudo unzip /tmp/awscli-bundle.zip -d /tmp \
    && sudo /tmp/awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws \
    && sudo rm -rf /tmp/awscli-bundle.zip /tmp/awscli-bundle
