from python:3.7

MAINTAINER zhengfei(zheng.fei@ginolegaltech.com)

RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get update && \
apt-get install -y nodejs \
rsync \
grunt \
gettext \
libgettextpo-dev \
&& \
rm -rf /var/lib/apt/lists/*

RUN npm install -g yarn \
cnpm --registry=https://registry.npm.taobao.org \
npm@4 \
less \
bower \
grunt \
rimraf \
webpack \
webpack-cli \
angular-gettext-cli \
jshint \
grunt-cli \
@google/clasp@2.0.1 \
ng-annotate \
babel && \

pip install polib \
six \
django

ADD requirements.* /tmp/
RUN pip install --upgrade pip && pip install -r /tmp/requirements.proprietary.txt  && pip install -r /tmp/requirements.dev.txt
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
	echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
	curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
	apt-get update -y && apt-get install google-cloud-sdk -y

RUN node --version && \
npm --version && \
webpack --version && \
yarn --version && \
clasp -v
