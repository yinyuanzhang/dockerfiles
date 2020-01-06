FROM ubuntu:14.04.2
MAINTAINER cannin

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y software-properties-common

# Install git curl
RUN apt-get install -y git curl wget links nano

RUN curl -sL https://deb.nodesource.com/setup | sudo bash -
RUN apt-get install -y nodejs

# Make sure we have a directory for the application
ENV APP_DIR /var/www
WORKDIR $APP_DIR

RUN mkdir -p $APP_DIR
RUN chown -R www-data:www-data $APP_DIR

# Install Meteor
RUN curl https://install.meteor.com/ | sh

# Added from https://registry.hub.docker.com/u/danieldent/meteor/
COPY vboxsf-shim.sh /usr/local/bin/vboxsf-shim
RUN chmod +x /usr/local/bin/vboxsf-shim

EXPOSE 3000

CMD ["meteor"]



