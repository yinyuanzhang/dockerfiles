FROM codelovers/hhvm-composer

MAINTAINER Daniel Holzmann <daniel@codelovers.at>

ENV HOME /root

RUN apt-get update -qq
RUN apt-get upgrade -y -qq
RUN apt-get install -y -qq nano curl sudo hhvm-dev git-core automake autoconf libtool gcc

# include fix: https://github.com/facebook/hhvm/wiki/DSO-3.5.0
RUN curl 'https://raw.githubusercontent.com/facebook/hhvm/573d6fc0d2745e96ee9775f31dc993919086fc7a/hphp/runtime/version.h' > /tmp/version.h
RUN sudo cp /tmp/version.h /usr/include/hphp/runtime/version.h

# install libbson
RUN git clone git://github.com/mongodb/libbson.git /tmp/libbson
WORKDIR /tmp/libbson
RUN ./autogen.sh
RUN make && sudo make install

# install mongofill-hhvm
RUN git clone https://github.com/mongofill/mongofill-hhvm /tmp/mongofill-hhvm
WORKDIR /tmp/mongofill-hhvm
RUN ./build.sh

# install extension
RUN mkdir -p /etc/hhvm/extensions
RUN cp /tmp/mongofill-hhvm/mongo.so /etc/hhvm/extensions/mongo.so
RUN echo 'hhvm.dynamic_extension_path = /etc/hhvm/extensions' >> /etc/hhvm/php.ini
RUN echo 'hhvm.dynamic_extensions[mongo] = mongo.so' >> /etc/hhvm/php.ini
RUN echo 'hhvm.dynamic_extension_path = /etc/hhvm/extensions' >> /etc/hhvm/server.ini
RUN echo 'hhvm.dynamic_extensions[mongo] = mongo.so' >> /etc/hhvm/server.ini

# clean up
RUN rm -Rf /tmp/libbson
RUN rm -Rf /tmp/mongofill-hhvm
RUN rm -f /tmp/version.h

WORKDIR /srv
