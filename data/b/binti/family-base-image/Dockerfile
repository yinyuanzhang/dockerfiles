FROM ruby:2.5.7

# this runs apt update
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y build-essential libpq-dev nodejs cmake pdftk dos2unix\
 libreoffice vim less silversearcher-ag libgeos-dev libproj-dev unattended-upgrades\
 clamdscan libmagic-dev qpdf
COPY ./clamav/clamd.conf /etc/clamav/clamd.conf
RUN unattended-upgrade -v
RUN npm install -g npm
RUN gem update --system
