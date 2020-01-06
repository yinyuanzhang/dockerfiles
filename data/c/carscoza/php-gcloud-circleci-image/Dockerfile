FROM php:7-cli-stretch
MAINTAINER allan <allan@cars.co.za>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y -qq --no-install-recommends \ 
	wget unzip python openssh-client python-openssl libzip-dev \
	apt-transport-https ca-certificates curl gnupg2 \
	software-properties-common libxml2-dev \
	&& apt-get clean

# Install Docker...
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
   $(lsb_release -cs) \
   stable"
RUN apt-get update && apt-get install -y -qq --no-install-recommends docker-ce

# Install the Google Cloud SDK.
ENV HOME /
ENV CLOUDSDK_PYTHON_SITEPACKAGES 1
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip && unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip
RUN google-cloud-sdk/install.sh --usage-reporting=true --path-update=true --bash-completion=true --rc-path=/.bashrc --additional-components kubectl

# Disable updater check for the whole installation.
# Users won't be bugged with notifications to update to the latest version of gcloud.
RUN google-cloud-sdk/bin/gcloud config set --installation component_manager/disable_update_check true

# Disable updater completely.
# Running `gcloud components update` doesn't really do anything in a union FS.
# Changes are lost on a subsequent run.
RUN sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g' /google-cloud-sdk/lib/googlecloudsdk/core/config.json

ENV PATH /google-cloud-sdk/bin:$PATH

# Install required PHP extensions
RUN docker-php-ext-install bcmath zip sockets soap

# Install composer... this is taken from the offical composer Dockerfile, look there when looking to update the composer install
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /tmp
ENV COMPOSER_VERSION 1.6.3


RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer 

RUN composer --ansi --version --no-interaction

RUN composer global require hirak/prestissimo --no-plugins --no-scripts

RUN rm -rf /tmp/* /tmp/.htaccess
