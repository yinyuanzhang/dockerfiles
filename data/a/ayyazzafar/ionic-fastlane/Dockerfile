FROM ayyazzafar/ionic

LABEL MAINTAINER="Ayyaz Zafar <contact@ayyaz.io>"

RUN apt-get -qq update && apt-get -qq install -y ruby-full less build-essential && \
    gem install fastlane -NV && \
    apt-get remove -y build-essential && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get autoremove -y && \
    apt-get clean && \
    echo export LC_ALL=en_US.UTF-8 >> ~/.bashrc && \
    echo export LANG=en_US.UTF-8 >> ~/.bashrc
