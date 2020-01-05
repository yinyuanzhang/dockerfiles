FROM azukiapp/ruby:2.2
MAINTAINER Diego Rossini Vieira <diego@redu.to>

# Install dependencies

# ==============================================================================
# PHANTOMJS
# ==============================================================================
# FROM: https://gist.github.com/talpa/16db1b8cfd3148364e19

ENV PHANTOM_VERSION="phantomjs-1.9.8"
ENV PHANTOM_JS="$PHANTOM_VERSION-linux-x86_64"

RUN apt-get update
RUN apt-get install build-essential chrpath libssl-dev libxft-dev -y
RUN apt-get install libfreetype6 libfreetype6-dev -y
RUN apt-get install libfontconfig1 libfontconfig1-dev -y

RUN cd ~
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
RUN tar xvjf $PHANTOM_JS.tar.bz2

RUN mv $PHANTOM_JS /usr/local/share
RUN ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

RUN rm -fr $PHANTOM_JS.tar.bz2

# ==============================================================================
# WEBKIT & QT
# ==============================================================================

RUN apt-get update
RUN apt-get -yq install libqtwebkit-dev
RUN apt-get -yq install qt4-qmake
RUN apt-get clean -qq
