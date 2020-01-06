FROM debian:stable

MAINTAINER David Pose <dpose@bitergia.com>, Alvaro del Castillo <acs@bitergia.com>, David Moreno <dmoreno@bitergia.com>
# Image for developing Kibiter/Kibana

# ENV KIBANA_BRANCH master
ENV KIBANA_BRANCH integration-6.3.1-crossminer
# ENV KIBANA_REPO https://github.com/grimoirelab/kibiter.git
ENV KIBANA_REPO https://github.com/acs/grimoirelab-kibiter.git

# add our user and group first to make sure their IDs get assigned consistently
RUN groupadd --system kibana && \
    useradd --system --create-home --gid kibana kibana

# backports used to install java 8 needed by elasticsearch 5
# ruby gems are used for building binary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
            apt-transport-https ca-certificates dirmngr gnupg \
            curl \
            wget \
            git \
            python \
            unzip zip \
            make \
            g++ \
            ruby-dev rpm rubygems \
            libffi-dev \
            && \
    # install nvm
    curl -o /tmp/nvm-install.sh -sSL https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh && \
    chmod +x /tmp/nvm-install.sh && \
    bash -c /tmp/nvm-install.sh && \
    . /root/.bashrc && \

    # install kibiter
    # gems needed in Kibana > 5.x to build binary packages
    gem install ffi && \
    gem install fpm -v 1.5.0 && \
    gem install pleaserun -v 0.0.24 && \
    # install yarn used from Kibana 6.2.2 to install dependencies
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    # echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    # 1.9.0 is needed because a bug in 1.7.0: https://github.com/elastic/kibana/issues/19641
    echo "deb https://nightly.yarnpkg.com/debian/ nightly main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && apt-get -y --no-install-recommends install yarn && \
#RUN    . /root/.bashrc && \
    git clone --depth 1 --branch ${KIBANA_BRANCH} ${KIBANA_REPO} kibiter && \
    cd kibiter && \
    nvm install "$( cat .node-version )" && \
    # npm install && \
    yarn kbn bootstrap && \
    # Build the kibiter package
    node scripts/build --oss --skip-os-packages --release && \
    tar xfz target/kibana-*-linux-x86_64.tar.gz --directory /opt && \
    mv /opt/kibana-*-linux-x86_64* /opt/kibana && \
    chown -R kibana:kibana /opt/kibana  && \
    # Install dotplot plugin: https://github.com/dlumbrer/kbn_dotplot
    cd /opt/kibana/plugins && \
    git clone https://github.com/dlumbrer/kbn_dotplot.git -b 6-dev && \
    cd kbn_dotplot && \
    npm install  && \
    cd .. && \
    # Install polar plugin: https://github.com/dlumbrer/kbn_polar
    cd /opt/kibana/plugins && \
    git clone https://github.com/dlumbrer/kbn_polar.git -b 6-dev && \
    cd kbn_polar && \
    npm install  && \
    cd .. && \
    # Install radar plugin: https://github.com/dlumbrer/kbn_radar
    cd /opt/kibana/plugins && \
    git clone https://github.com/dlumbrer/kbn_radar.git -b 6-dev && \
    cd kbn_radar && \
    npm install  && \
    cd .. && \
    # Install network plugin: https://dlumbrer.github.io/kbn_network/
    git clone https://github.com/dlumbrer/kbn_network.git network_vis -b 6-dev && \
    cd network_vis && \
    npm install  && \
    cd /root && \
    # Install Search-Guard Custom Bitergia plugin: https://github.com/Bitergia/search-guard-kibana-plugin
    cd /opt/kibana/plugins && \
    wget https://github.com/acs/search-guard-kibana-plugin/releases/download/6.3.1-CROSSMINER/searchguard-biter-6.3.1-14-beta-1-crossminer.zip && \
    unzip searchguard-biter-6.3.1-14-beta-1-crossminer.zip && \
    cd .. && \
    # Add Search-Guard configuration to kibana.yml
    echo 'elasticsearch.ssl.verificationMode: none' >> /opt/kibana/config/kibana.yml && \
    echo 'searchguard.basicauth.enabled: true' >> /opt/kibana/config/kibana.yml && \
    echo '#searchguard.basicauth.login.contact_email:' >> /opt/kibana/config/kibana.yml && \
    # cleanup to thin the final image
    rm -rf /kibiter && \
    apt-get purge -y g++ git make python zip wget && \
    apt-get autoremove --purge -y && \
    apt-get clean && \
    find /var/lib/apt/lists -type f -delete && \
    rm -rf /root/.npm /root/.node-gyp /root/.nvm /tmp/* /var/tmp/* /usr/local/share/.cache && \
    bash -c 'find /usr/share/locale -maxdepth 1 -mindepth 1 -type d | grep -v -e "en_US" | xargs rm -rfv' && \
    bash -c 'localedef --list-archive | grep -v -e "en_US" | xargs localedef --delete-from-archive' && \
    rm -rf /usr/share/doc/*

# grab gosu for easy step-down from root
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN arch="$(dpkg --print-architecture)" \
	&& set -x \
	&& curl -o /usr/local/bin/gosu -sSL "https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch" \
	&& curl -o /usr/local/bin/gosu.asc -sSL "https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch.asc" \
	&& gpg --verify /usr/local/bin/gosu.asc \
	&& rm /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu

ENV PATH /opt/kibana/bin:$PATH

# Create the optimized version of Kibana to speed up the initial loading time
RUN rm -rf /opt/kibana/optimize/*
RUN ./opt/kibana/bin/kibana | sleep 200 > /tmp/run_kibana_log.txt

COPY ./docker-entrypoint.sh /

EXPOSE 5601
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["kibana"]
