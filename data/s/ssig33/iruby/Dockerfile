FROM jupyter/minimal-notebook

MAINTAINER ssig33

USER root
RUN echo 'deb http://cdn-fastly.deb.debian.org/debian stable main' > /etc/apt/sources.list
RUN echo 'deb-src http://cdn-fastly.deb.debian.org/debian stable main' >> /etc/apt/sources.list
RUN apt-get update && \ 
  sudo apt-get install build-essential libncurses5-dev libreadline-dev libssl-dev libyaml-dev libmariadbclient-dev libsqlite3-dev libxml2-dev libxslt-dev libsasl2-dev libsasl2-2 libv8-dev imagemagick libmagickwand-dev -y && \
  apt-get build-dep ruby -y
RUN wget https://cache.ruby-lang.org/pub/ruby/2.4/ruby-2.4.1.tar.gz && tar xvf ruby-2.4.1.tar.gz && cd ruby-2.4.1 && ./configure && make -j9 && make install && cd .. && rm -rf ruby*
RUN apt-get clean && cd ~ && \
    apt-get update && apt-get install -yq libtool pkg-config  autoconf && \
    git clone --depth=1 https://github.com/zeromq/libzmq && \
    git clone --depth=1 https://github.com/zeromq/czmq && \
    cd libzmq && ./autogen.sh && ./configure && make && make install && \
    cd ../czmq && ./autogen.sh && ./configure && make && make install && \
    gem install cztop specific_install && \
    gem specific_install https://github.com/SciRuby/iruby.git && \
    rm -rf /var/lib/apt/lists/* && ldconfig

RUN gem install pry pry-doc awesome_print gnuplot rubyvis nyaplot cztop

# Switch back to jovyan to avoid accidental container runs as root
RUN mkdir -p /opt/notebooks && chown $NB_USER /opt/notebooks
USER $NB_USER

RUN iruby register

CMD /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser
