FROM sonodar/jdk8

MAINTAINER sonodar <ryoheisonoda@outlook.com>

# Install wget
RUN apt-get update && apt-get upgrade -y && apt-get -y install wget

# Set constants
ENV JRUBY_VERSION 9.0.0.0

ENV JRUBY_HOME /opt/jruby
ENV JRUBY_OPTS --2.0
ENV PATH $JRUBY_HOME/bin:$PATH

# Download and extract jruby archive
RUN wget https://s3.amazonaws.com/jruby.org/downloads/$JRUBY_VERSION/jruby-bin-$JRUBY_VERSION.tar.gz \
    --no-check-certificate -O /tmp/jruby-bin-$JRUBY_VERSION.tar.gz
RUN cd /opt; tar zxf /tmp/jruby-bin-$JRUBY_VERSION.tar.gz \
    && ln -s /opt/jruby-$JRUBY_VERSION ${JRUBY_HOME}

# Remove windows files
RUN find /opt/jruby-$JRUBY_VERSION -name "*.exe" -o -name "*.dll" -o -name "*.bat" -print0 | xargs -0 rm -f

# Install bundler for compatible 1.9
RUN jruby -S gem install bundler --no-ri --no-rdoc
