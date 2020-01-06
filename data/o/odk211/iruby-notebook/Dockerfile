FROM jupyter/minimal-notebook

USER root

# install iruby https://github.com/SciRuby/iruby
RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends \
    libtool libffi-dev make automake \
    libssl-dev libreadline-dev zlib1g-dev \
    git libzmq-dev autoconf pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/zeromq/czmq --depth 1 && \
    cd czmq && \
    ./autogen.sh && ./configure && make && make install && \
    cd .. && \
    rm -rf ./czmq

# install ruby-build, ruby
RUN git clone https://github.com/rbenv/ruby-build.git --depth 1 && \
    cd ruby-build && \
    ./install.sh && \
    cd .. && \
    rm -rf ./ruby-build

ENV RUBY_VERSION=2.4.1 \
    RUBY_DIR=/opt/ruby

ENV PATH=$RUBY_DIR/bin:$PATH

RUN mkdir -p $RUBY_DIR && \
    chown $NB_USER $RUBY_DIR

USER $NB_USER

RUN ruby-build $RUBY_VERSION $RUBY_DIR

RUN gem install bundler cztop iruby pry pry-doc awesome_print gnuplot rubyvis nyaplot --no-document && \
    iruby register --force

# install jupyter-vim-binding
# RUN mkdir -p $(jupyter --data-dir)/nbextensions && \
#     cd $(jupyter --data-dir)/nbextensions && \
#     git clone https://github.com/lambdalisue/jupyter-vim-binding vim_binding --depth 1 && \
#     jupyter nbextension enable vim_binding/vim_binding
