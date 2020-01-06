FROM thomasredstone/base
# Install hhvm
RUN apt-get update -qq && apt-get -y upgrade
RUN apt-get -y -qq install software-properties-common wget
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0x5a16e7281be7a449 && add-apt-repository "deb http://dl.hhvm.com/ubuntu $(lsb_release -sc) main"

RUN echo 'deb http://s3-eu-west-1.amazonaws.com/qafoo-profiler/packages debian main' > /etc/apt/sources.list.d/tideways.list
RUN wget -qO - https://s3-eu-west-1.amazonaws.com/qafoo-profiler/packages/EEB5E8F4.gpg | apt-key add -
RUN apt-get update
RUN apt-get install -y -qq tideways-php tideways-daemon hhvm php5-cli curl libcurl3 libcurl3-dev php5-curl php5-mysql

RUN usermod -u 1000 www-data
RUN /usr/share/hhvm/install_fastcgi.sh

# Adding the configuration files
ADD conf/php.ini /etc/hhvm/php.ini
# Add the run script to run the services and configure db
ADD conf/run.sh /run.sh

#add the volume for the application
VOLUME /var/www/app

# Expose the port 9000
EXPOSE 9000
# Run the run.sh scriptCMD
ENTRYPOINT [ "/bin/bash", "/run.sh"]