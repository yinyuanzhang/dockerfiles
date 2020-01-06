FROM phusion/baseimage

ENV DEBIAN_FRONTEND noninteractive


# Install essentials
RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install -y software-properties-common python-software-properties bzip2 unzip openssh-client git lib32stdc++6 lib32z1 expect build-essential libssl-dev


# for packaging anything using electron-builder & electron-packager
RUN add-apt-repository ppa:ubuntu-wine/ppa \
	&& dpkg --add-architecture i386 \
	&& apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install -y --no-install-recommends wine wine1.8 \
	&& apt-get install -y gcc-multilib g++-multilib \
	&& apt-get install -y --no-install-recommends rpm bsdtar \
	&& apt-get install -y --no-install-recommends icnsutils graphicsmagick xz-utils p7zip

# Install NodeJS
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
	&& apt-get install -y nodejs


# Install Yarn, uninstall cmdtest's `yarn' command
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
	&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
	&& apt-get update \
	&& apt-get remove -y cmdtest \
	&& apt-get install -y yarn

ENV PATH ${PATH}:`yarn global bin`


# we need npm ^5.4.0 - see https://github.com/electron-userland/electron-packager/issues/712
# https://github.com/npm/npm/issues/16807#issuecomment-313591975
RUN yarn global add npm@^5.4.0


# ruby & sass
RUN apt-get install -y ruby ruby-dev \
	&& gem install sass

# PHP5.6
RUN add-apt-repository ppa:ondrej/php -y \
	&& apt-get update \
	&& apt-get install -y --allow-unauthenticated php5.6 php5.6-cli php5.6-mbstring php5.6-mcrypt php5.6-mysql php5.6-xml


# grunt
RUN npm install --global grunt
