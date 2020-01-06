FROM bryanlarsen/builder-base:2018-12-21

RUN curl -f --silent --location https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs build-essential make bzip2 chromedriver chromium xvfb

RUN npm i -g watch-cli vsce typescript

# Yarn
ENV YARN_VERSION 1.12.1
RUN curl -f -L -o /tmp/yarn.tgz https://github.com/yarnpkg/yarn/releases/download/v${YARN_VERSION}/yarn-v${YARN_VERSION}.tar.gz && \	
	tar xf /tmp/yarn.tgz && \
	mv yarn-v${YARN_VERSION} /opt/yarn && \
	ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn
