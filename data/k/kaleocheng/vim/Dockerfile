FROM debian:sid
RUN apt update && apt install -y vim vim-nox git curl cmake 
ENV TERM=xterm-256color

RUN apt install -y python3 python3-pip
RUN cp /usr/bin/python3 /usr/bin/python
RUN pip3 install yapf pylint

RUN apt install -y golang

RUN curl -fLo /root/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

COPY vimrc-ycm /root/.vimrc
RUN vim +PlugInstall +qall

COPY vimrc-plugin /root/.vimrc
RUN vim +PlugInstall +qall

COPY vimrc /tmp/vimrc
RUN cat /tmp/vimrc >> /root/.vimrc

