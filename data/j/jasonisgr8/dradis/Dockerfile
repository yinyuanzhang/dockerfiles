FROM ubuntu:18.04 

LABEL maintainer="Jason <jasonisgr8@gmail.com>"

COPY localtime /etc/localtime

#Avoid getting prompted during builds
ENV DEBIAN_FRONTEND=noninteractive

#Pre-requisites
RUN apt update -qq && \
    apt install -y ruby stunnel4 nodejs git gcc ruby-dev make libmysqlclient-dev libsqlite3-dev g++ tzdata && \
    rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/apt/* 

#Clone the repo
RUN git clone --depth=1 https://github.com/dradis/dradis-ce.git

WORKDIR /dradis-ce

#Complains without the rake gem setup
RUN gem install rake
RUN gem install bundler -v '1.17.3'
RUN gem update --system
RUN ruby /dradis-ce/bin/setup

#Setup SSL
COPY stunnel/stunnel4 /etc/default/
COPY stunnel/dradis.conf /etc/stunnel/
COPY stunnel/genssl.sh /bin/
RUN /bin/genssl.sh
#RUN update-rc.d stunnel4 defaults
#RUN update-rc.d stunnel4 enable
#CMD ["/etc/init.d/stunnel4","start"]

#Bind to all interfaces explicitly as the default is localhost only
#CMD ["bundle","exec","rails","server","-b","0.0.0.0"]

#Clear dradis database
RUN thor dradis:reset:database

#Copy templates to image
COPY methodologies/* /dradis-ce/templates/methodologies/
COPY reports/html_export/* /dradis-ce/templates/reports/html_export/

#Start it up
COPY startup.sh ./
CMD ["./startup.sh"]

