FROM ubuntu:14.04
MAINTAINER abrahammouse<abrahammouse@gmail.com>

RUN apt-get update && \
    apt-get install -y --force-yes \
    libncurses5-dev libgnome2-dev libgnomeui-dev \
    libgtk2.0-dev libatk1.0-dev libbonoboui2-dev \
    libcairo2-dev libx11-dev libxpm-dev libxt-dev python-dev \
    python3-dev ruby-dev lua5.1 lua5.1-dev libperl-dev ctags \
    git curl make cmake gcc clang openssh-server\
 && cd /root \
 && git clone https://github.com/vim/vim.git \
 && cd vim \
 && ./configure --with-features=huge \
	--enable-multibyte \
	--enable-rubyinterp=yes \
	--enable-pythoninterp=yes \
	--with-python-config-dir=/usr/lib/python2.7/config-x86_64-linux-gnu \
	--enable-python3interp=yes \
	--with-python3-config-dir=/usr/lib/python3.4/config-3.4m-x86_64-linux-gnu \
	--enable-perlinterp=yes \
	--enable-luainterp=yes \
	--enable-gui=gtk2 --enable-cscope --prefix=/usr \
 && make VIMRUNTIMEDIR=/usr/share/vim/vim80 \
 && make install \
 && curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/vim
 
ADD config/. /root/

RUN timeout 20m vim +PlugInstall +qall || true

COPY fix_putty/NERD_tree.vim /root/.vim/plugged/nerdtree/plugin/NERD_tree.vim

RUN /root/.vim/plugged/YouCompleteMe/install.py --clang-completer

EXPOSE 22
ENTRYPOINT service ssh restart && bash
