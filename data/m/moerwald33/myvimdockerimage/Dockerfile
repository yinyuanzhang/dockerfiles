FROM ubuntu:18.04
RUN apt-get update -qq \
 && apt-get install -qqy python3 \
 && apt-get install -qqy vim \
 && apt-get install -qqy git \
 && apt-get install -qqy dos2unix\
 && apt-get install -qqy libuv1.dev\
 && apt-get install -qqy curl \
 && apt-get install -qqy subversion

COPY _vimrc /root/.vimrc

RUN curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

RUN cd /tmp \
 && git clone https://github.com/powerline/fonts.git \
 && cd /tmp/fonts \
 && ./install.sh

RUN dos2unix ~/.vimrc
RUN mkdir /data

RUN vim +PlugInstall +qall
