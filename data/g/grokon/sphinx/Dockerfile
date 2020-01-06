FROM phusion/baseimage:0.11
# set mainainer
LABEL maintainer="Grokon"
# Set sphinx version
ENV SPHINX_VERSION 3.0.3-facc3fb
# install dependencies
RUN apt-get update && apt-get install -y \
        libmysqlclient20 \
        libpq5 && \
    # add symlink for sphinx
    ln -s /usr/lib/x86_64-linux-gnu/libmysqlclient.so.20.3.10 /usr/lib/libmysqlclient.so
# set up and expose directories
RUN mkdir -pv /opt/sphinx/log /opt/sphinx/index /opt/sphinx/conf && \
    curl -L http://sphinxsearch.com/files/sphinx-${SPHINX_VERSION}-linux-amd64.tar.gz | tar xvz -C /opt/sphinx --strip 1 && \
    # redirect logs to stdout
    ln -sv /dev/stdout /opt/sphinx/log/query.log && \
    ln -sv /dev/stdout /opt/sphinx/log/searchd.log && \
    # rotate index
    echo "0 */6   * * *   root    indexer --rotate --all" >> /etc/crontab
# point to sphinx binaries
ENV PATH "${PATH}:/opt/sphinx/bin"
# add indexer on start container
COPY ./conf/index.sh /etc/my_init.d/20_index.sh
RUN  chmod +x /etc/my_init.d/20_index.sh
# add searchd service
RUN mkdir /etc/service/searchd
COPY ./conf/searchd.sh /etc/service/searchd/run
RUN chmod +x /etc/service/searchd/run
# add config file
COPY ./conf/sphinx.conf /opt/sphinx/conf/sphinx.conf
# expose TCP port
EXPOSE 9312 9306
# set working dir
WORKDIR /opt/sphinx/conf
# set mount volime
VOLUME /opt/sphinx/index
# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]