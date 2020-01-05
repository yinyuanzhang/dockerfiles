FROM base/archlinux
LABEL name="archvim"
MAINTAINER adjivas <adjivas@student.42.fr>
ENV HOME /home
RUN pacman-key --populate archlinux
RUN pacman-key --refresh-keys
RUN pacman -Syy ;
RUN pacman -S --noconfirm gcc git vim ;
RUN mkdir -p $HOME/.vim/autoload $HOME/.vim/bundle ;
RUN curl -LSso $HOME/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim ;
RUN git clone https://github.com/rust-lang/rust.vim.git $HOME/.vim/bundle/rust.vim ;
RUN git clone https://github.com/Shougo/unite.vim.git $HOME/.vim/bundle/unite.vim ;
RUN git clone https://github.com/Shougo/vimfiler.vim.git $HOME/.vim/bundle/vimfiler.vim ;
RUN git clone https://github.com/terryma/vim-multiple-cursors.git $HOME/.vim/bundle/vim-multiple-cursors ;
ADD ./.vimrc /home/.vimrc
ENTRYPOINT ["vim", "-c", "VimFiler"]
