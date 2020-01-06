# Use the barebones version of Ruby 2.5.1
FROM debian:stretch

# Baller maintainers
LABEL maintainer "Charlie McClung <charlie@bowtie.co>, Brandon Cabael <brandon@bowtie.co>"

# Set EDITOR default to vim (used when editing env via sops)
ENV EDITOR vim

# Create dir for shared scripts
RUN mkdir -p /scripts

# Use generic /app path for working directory
ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

# Download installers for sops and node 8.x
ADD https://github.com/mozilla/sops/releases/download/3.0.5/sops_3.0.4_amd64.deb /tmp/sops.deb
ADD https://deb.nodesource.com/setup_8.x /tmp/node.sh
ADD https://cache.ruby-lang.org/pub/ruby/2.4/ruby-2.4.4.tar.gz /tmp/ruby.tar.gz

# Run system package installations
RUN apt-get update && apt-get install -qq -y --no-install-recommends \
      # Basic required packages for all rails images
      build-essential git vim gnupg2 \
      # Install requirements for image processing (paperclip)
      ghostscript imagemagick libmagic-dev graphviz \
      # This is lib for PostgreSQL
      libpq-dev file libjemalloc-dev zlib1g-dev libssl-dev && \
      # Install sops from downloaded .deb file
      dpkg -i /tmp/sops.deb && \
      # Install node (only installs 8.x apt repo & key)
      cat /tmp/node.sh | bash && \
      # Run install again for nodejs (after running node.sh, this will install 8.x)
      apt-get install -qq -y -f --no-install-recommends nodejs && \
      # Remove tmp install files
      rm /tmp/sops.deb && \
      rm /tmp/node.sh && \
      mkdir -p /tmp/ruby

RUN tar -xzf /tmp/ruby.tar.gz -C /tmp/ruby && \
      cd /tmp/ruby/ruby-2.4.4 && \
      ./configure --with-jemalloc && \
      make && \
      make install && \
      ruby -r rbconfig -e "puts RbConfig::CONFIG['libs']" && \
      gem install bundler && \
      cd $INSTALL_PATH

COPY *.sh /scripts/

ENTRYPOINT [ "/scripts/docker-entrypoint.sh" ]

CMD bundle exec puma -C config/puma.rb
