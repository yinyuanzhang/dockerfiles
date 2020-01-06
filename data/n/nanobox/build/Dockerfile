FROM nanobox/runit

# install gcc and build tools and other utilities
RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends \
      build-essential git rsync openssh-client pv && \
    apt-get clean all && \
    rm -rf /var/lib/apt/lists/*

# install other tools required for engine
RUN rm -rf /var/gonano/db/pkgin && /opt/gonano/bin/pkgin -y up && \
    /opt/gonano/bin/pkgin -y in shon mustache siphon hookit && \
    rm -rf /var/gonano/db/pkgin/cache && \
    gem install ya2yaml --no-ri --no-rdoc

# add temporary scripts
ADD scripts/. /var/tmp/

# Copy files
ADD files/. /

# chown the gonano directory
RUN chown -R gonano:gonano /home/gonano

# generate build exclude list
RUN /var/tmp/generate-build-excludes

# update pkgin remote packages
RUN rm -rf /data/var/db/pkgin && /data/bin/pkgin -y up && \
    rm -rf /data/var/db/pkgin/cache && \
    chown -R gonano /data/var/db/pkgin

# install nos
RUN mkdir -p /opt/nanobox/nos && \
    curl \
      -k \
      -s \
      -L \
      https://github.com/nanobox-io/nanobox-nos/archive/v0.13.0.tar.gz \
        | tar \
            -xzf - \
            --strip-components=1 \
            -C /opt/nanobox/nos/

# Install engines
RUN /var/tmp/install-engines

# Cleanup disk
RUN rm -rf /tmp/* /var/tmp/*

CMD [ "/opt/gonano/bin/nanoinit", "/bin/sleep", "365d" ]
