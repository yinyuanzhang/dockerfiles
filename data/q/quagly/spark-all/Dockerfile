FROM jupyter/all-spark-notebook:7f1482f5a136
LABEL maintainer="Michael West <quagly@gmail.com>"

USER root

# note scala package has compatibility issues with Ubuntu 18.04
# need to switch to dpkg installation to get more recent scala
RUN  apt-get -y update && \
     apt-get install --no-install-recommends -y \
      autoconf \
      automake \
      gnupg \
      libsnappy-dev \
      stow \
      vim && \
    rm -rf /var/lib/apt/lists/*

# install scala from scala-lang deb
# since there is an issue with ubuntu scala - see above
RUN wget -q www.scala-lang.org/files/archive/scala-2.12.8.deb && \
    dpkg -i scala-2.12.8.deb && \
    rm scala-2.12.8.deb

# install sbt
# https://www.scala-sbt.org/1.x/docs/Installing-sbt-on-Linux.html
RUN echo "deb https://dl.bintray.com/sbt/debian /" >> /etc/apt/sources.list.d/sbt.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823 && \
    apt-get update && \
    apt-get install sbt && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
# install snappy command line utility
# depends on libsnappy which is included in
# the base image
RUN git clone git://github.com/kubo/snzip.git && \
  cd snzip && \
  ./autogen.sh && \
  ./configure && \
  make && \
  make install && \
  rm -rf /tmp/snzip

USER jovyan
WORKDIR $HOME

ENV PATH $PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
ENV CLASSPATH /usr/local/spark/jars/*

# setup home directory for development
# not needed for notebook use

# save debian provided .bashrc to .bashrc_local to keep its goodies
RUN mv $HOME/.bashrc $HOME/.bashrc_local

RUN git clone https://github.com/quagly/dotfiles.git $HOME/.dotfiles

WORKDIR $HOME/.dotfiles
RUN stow bash;\
  stow vim;\
  stow tmux

WORKDIR $HOME
# run sbt to make it resolve its dependencies
# so it is quick to use
RUN sbt sbtVersion

# configure vim
RUN git clone https://github.com/VundleVim/Vundle.vim.git $HOME/.vim/bundle/Vundle.vim
# command to install plugins, returns non-zero exit code but works.
# added true to the end until I can figure it out
# maybe still related to no interactivity despite -E?
RUN vim -E -u NONE -S $HOME/.vimrc +PluginInstall +qall || true

