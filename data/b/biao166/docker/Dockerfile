#
# Base
#

FROM ubuntu:latest
MAINTAINER biao166 biao166@gmail.com

# Patch the proper apt-get sources
ADD sources.list /etc/apt/sources.list
RUN echo dns-nameservers 115.159.157.26 115.159.158.38 >>/etc/resolv.conf

RUN apt-get update -y
RUN chmod go+w,u+s /tmp

# package
RUN apt-get install openssh-server tmux build-essential -y
RUN apt-get install zsh wget unzip curl tree grep bison libssl-dev openssl zlib1g-dev ruby-full -y # "libssl-dev openssl zlib1g-dev" need to rbenv and pyenv

#vim
RUN apt-get install git mercurial gettext libncurses5-dev  libperl-dev python-dev python3-dev ruby-dev lua5.2 liblua5.2-dev luajit libluajit-5.1 -y
RUN cd /tmp \
    && git clone https://github.com/vim/vim.git \
    && cd /tmp/vim \
    && ./configure --with-features=huge --enable-perlinterp --enable-pythoninterp --enable-python3interp --enable-rubyinterp --enable-luainterp --with-luajit --enable-fail-if-missing \
    && make \
    && make install

# sshd config
RUN sed -i 's/.*session.*required.*pam_loginuid.so.*/session optional pam_loginuid.so/g' /etc/pam.d/sshd
RUN mkdir /var/run/sshd

# user
RUN echo 'root:root' |chpasswd
RUN useradd -m biao166 \
    && echo "biao166 ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && echo 'biao166:biao166' | chpasswd
RUN chsh -s /usr/bin/zsh biao166

USER biao166
WORKDIR /home/biao166
ENV HOME /home/biao166

# ssh
RUN mkdir .ssh
RUN chmod 700 .ssh
COPY id_rsa .ssh/
COPY id_rsa.pub .ssh/
USER root
RUN chown biao166 /home/biao166/.ssh/id_rsa
RUN chown biao166 /home/biao166/.ssh/id_rsa.pub
USER biao166

# oh-my-zsh
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \
      && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

# vim config
RUN  curl https://j.mp/spf13-vim3 -oL | sh

#
# Database
#

USER root
# SQLite
RUN apt-get install sqlite3 libsqlite3-dev -y
# client
RUN apt-get install mysql-client redis-tools postgresql-client mongodb-clients -y
USER biao166

#
# Programming Language
#

# Python (virtualenv)
USER root
RUN apt-get install python-pip -y
RUN pip install virtualenv
RUN pip install virtualenvwrapper
USER biao166
RUN echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.zshrc
RUN echo 'source `which virtualenvwrapper.sh`' >> ~/.zshrc

# Python (pyenv)
RUN git clone https://github.com/yyuu/pyenv.git ~/.pyenv
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
RUN echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
RUN echo 'eval "$(pyenv init -)"' >> ~/.zshrc
RUN ~/.pyenv/bin/pyenv install 3.5.1
RUN ~/.pyenv/bin/pyenv install 2.7.11

# Node.js (nvm)
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.4/install.sh | bash
ENV NODE_VERSION 4.5.0
ENV NVM_DIR $HOME/.nvm
RUN . ~/.nvm/nvm.sh && nvm install $NODE_VERSION && nvm alias default $NODE_VERSION && npm install -g gulp node-gyp browserify

#
# Else
#

# volumes
USER biao166
RUN mkdir /home/biao166/works

# for ssh
USER root
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
