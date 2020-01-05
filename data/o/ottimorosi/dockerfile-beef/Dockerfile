FROM phocean/msf

MAINTAINER Phocean <jc@phocean.net>

# install nodejs
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y \
    nodejs git bundler build-essential patch \
    ruby-dev zlib1g-dev liblzma-dev libsqlite3-dev

# set locales
RUN locale-gen en_US.UTF-8
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    echo 'LANG="en_US.UTF-8"'>/etc/default/locale  && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8 && \
    locale-gen en_US.UTF-8 && localedef -c -f UTF-8 -i en_US en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Get BeEF
WORKDIR /opt
RUN /bin/bash -l -c "git clone git://github.com/beefproject/beef.git"
WORKDIR beef
RUN /bin/bash -l -c "bundle install"

ADD ./scripts/init.sh /usr/local/bin/init.sh

EXPOSE 3000

# Starting script (DB + updates)
CMD /usr/local/bin/init.sh
