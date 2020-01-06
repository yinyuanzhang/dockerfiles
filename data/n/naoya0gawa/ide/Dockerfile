FROM centos:latest
MAINTAINER original <test@example.com>

Run localedef -f UTF-8 -i ja_JP /usr/lib/locale/ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

Run yum -y install make && yum -y install gcc && yum -y install vim && yum -y install git && yum -y install go && yum -y install mercurial
Run cd /var/ && git clone https://github.com/naoya-ogawa/ide.git
Run cd / &&  ln -s /var/ide/_vimrc .vimrc 
Run mkdir -p /.vim/bundle && git clone https://github.com/Shougo/neobundle.vim /.vim/bundle/neobundle.vim
Run cp /var/ide/_bashrc /.bashrc && cd /var/ide/ && ./update.sh

