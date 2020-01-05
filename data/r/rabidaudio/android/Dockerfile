FROM beevelop/android

# install ruby
RUN apt-get -qq update && apt-get install -yy git-core curl zlib1g-dev build-essential \
        libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev \
        libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev nodejs

RUN cd /tmp && \
    wget http://ftp.ruby-lang.org/pub/ruby/2.5/ruby-2.5.3.tar.gz && \
    tar -xzvf ruby-2.5.3.tar.gz && \
    cd ruby-2.5.3 && \
    ./configure && \
    make && \
    make install && \
    echo 'gem: --no-document' >> ~/.gemrc && \
    gem install bundler && \
    bundle config --global silence_root_warning 1

# configure sdk
COPY licenses /opt/android/licenses

# Install extras
COPY packages /tmp/packages
RUN /opt/android/tools/bin/sdkmanager $(cat /tmp/packages) && /opt/android/tools/bin/sdkmanager --update

# we can speed up times by pre-installing deps
RUN gem install fastlane nokogiri

# Install lokalise
RUN wget https://s3-eu-west-1.amazonaws.com/lokalise-assets/cli/lokalise-0.69-linux-amd64.tgz && \
    tar -xvzf lokalise-0.69-linux-amd64.tgz -C /usr/bin  && \
    chmod +x /usr/bin/lokalise

# pre-download gradle dist
RUN gradle wrapper --gradle-version 4.10.1 && \
    ./gradlew -v

WORKDIR /app
