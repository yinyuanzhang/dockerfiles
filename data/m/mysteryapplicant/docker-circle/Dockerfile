FROM circleci/ruby:2.5

ENV SOLR_VERSION 7.2.1

USER root

RUN echo "deb http://http.us.debian.org/debian/ jessie-backports main" >> /etc/apt/sources.list
RUN echo "deb-src http://http.us.debian.org/debian/ jessie-backports main" >> /etc/apt/sources.list

RUN apt-get -y update && \
    apt-get -y install  apt-transport-https \
                        apt-utils \
                        cmake \
                        libgs9 \
                        lsb-release \
                        mysql-client \
                        openjdk-8-jre

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get -y update && \
    apt-get -y install ghostscript \
                       yarn
RUN yarn global add phantomjs-prebuilt

RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.6.1.tar.gz \
    && rm dockerize-linux-amd64-v0.6.1.tar.gz

USER circleci

RUN cd /home/circleci && \
    wget https://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/solr-$SOLR_VERSION.tgz

RUN cd /home/circleci && \
    wget https://github.com/na-ka-na/ExcelCompare/releases/download/0.6.1/ExcelCompare-0.6.1.zip && \
    unzip -d ~/ExcelCompare-0.6.1 ExcelCompare-0.6.1.zip && \
    rm ~/ExcelCompare-0.6.1.zip && \
    chmod +x ~/ExcelCompare-0.6.1/bin/excel_cmp

CMD /bin/bash
