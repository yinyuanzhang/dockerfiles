FROM golang

RUN mkdir -p ~/tools && \
    git clone https://github.com/brendangregg/FlameGraph ~/tools/FlameGraph

ENV PATH ~/tools/FlameGraph:$PATH

ENV EDITOR vim
ENV SHELL zsh

#RUN sed -i "s/httpredir\.debian\.org/mirrors\.163\.com/g" /etc/apt/sources.list

RUN apt-get -q update && \
  apt-get install --no-install-recommends -y --force-yes -q \
    fontconfig \
    ca-certificates \
    zsh \
    tmux \
    curl \
    git \
    vim-nox \
    rubygems \
    build-essential \
    cmake \
    python-dev \
    python-pip \
    python-setuptools \
    ctags \
    xdg-utils \
    npm \
    xfonts-utils  \
    locales \
    && \
  apt-get clean && \
  rm /var/lib/apt/lists/*_*

RUN curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | /bin/zsh || true

#RUN gem sources --add https://ruby.taobao.org/ --remove https://rubygems.org/

RUN gem install tmuxinator

#ENV http_proxy xxx 
#ENV https_proxy xxx 

RUN go get github.com/nsf/gocode \
           github.com/tools/godep \
           github.com/constabulary/gb/... \
           github.com/axw/gocov/gocov \
           golang.org/x/tools/cmd/godoc \ 
           github.com/kisielk/errcheck \
           github.com/alecthomas/gometalinter \
           github.com/uber/go-torch \
           golang.org/x/tools/cmd/goimports \
           github.com/rogpeppe/godef \
           golang.org/x/tools/cmd/oracle \
           golang.org/x/tools/cmd/gorename \
           github.com/golang/lint/golint \
           github.com/kisielk/errcheck \
           github.com/jstemmer/gotags \
           github.com/kisielk/godepgraph \
           golang.org/x/tools/cmd/gomvpkg \
           golang.org/x/tools/cmd/benchcmp \
           github.com/garyburd/go-explorer/src/getool

RUN mkdir -p ~/.vim/{autoload,bundle,colors,scripts} && \
    wget -P ~/.vim/autoload "https://tpo.pe/pathogen.vim" && \
    wget -P ~/.vim/colors "https://raw.githubusercontent.com/xlucas/go-vim-install/master/molokai.vim" && \
    git clone https://github.com/majutsushi/tagbar ~/.vim/bundle/tagbar && \
    git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim && \
    git clone git://github.com/tpope/vim-sensible.git ~/.vim/bundle/vim-sensible && \
    git clone https://github.com/Valloric/YouCompleteMe ~/.vim/bundle/YouCompleteMe && \
    git clone https://github.com/garyburd/go-explorer.git ~/.vim/bundle/go-explorer && \
    git clone https://github.com/scrooloose/nerdtree.git ~/.vim/bundle/nerdtree && \
    git clone https://github.com/kien/ctrlp.vim.git ~/.vim/bundle/ctrlp.vim && \
    git clone https://github.com/bling/vim-airline ~/.vim/bundle/vim-airline && \
    git clone https://github.com/tpope/vim-fugitive ~/.vim/bundle/vim-fugitive && \
    git clone https://github.com/mileszs/ack.vim ~/.vim/bundle/ack.vim && \
    git clone https://github.com/mattn/emmet-vim ~/.vim/bundle/emmet-vim && \
    git clone https://github.com/sjl/gundo.vim ~/.vim/bundle/gundo.vim && \
    git clone https://github.com/ntpeters/vim-better-whitespace ~/.vim/bundle/vim-better-whitespace && \ 
    git clone https://github.com/Raimondi/delimitMate ~/.vim/bundle/delimitMate && \
    git clone https://github.com/suan/vim-instant-markdown ~/.vim/bundle/vim-instant-markdown && \
    git clone https://github.com/scrooloose/syntastic ~/.vim/bundle/syntastic && \
    git clone https://github.com/fatih/vim-go.git ~/.vim/bundle/vim-go

RUN cd ~/.vim/bundle/YouCompleteMe && git submodule update --init --recursive && ./install.sh

RUN gometalinter --install --update

RUN wget -P ~/.vim/scripts/closetag.vim "http://vim.sourceforge.net/scripts/download_script.php?src_id=4318"

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen "en_US.UTF-8"

RUN pip install --user powerline-status

RUN mkdir -p ~/.vim/autoload ~/.fonts ~/.config/fontconfig/conf.d && \
	wget -P ~/.fonts/ https://github.com/Lokaltog/powerline/raw/develop/font/PowerlineSymbols.otf && \
	wget -P ~/.config/fontconfig/conf.d https://github.com/Lokaltog/powerline/raw/develop/font/10-powerline-symbols.conf && \
	fc-cache -r ~/.fonts

ADD vimrc /root/.vimrc
ADD tmuxinator /root/.tmuxinator
ADD tmux.conf /etc/tmux.conf

VOLUME ["/go/src"]

CMD ["/usr/local/bin/tmuxinator", "start", "default"]
