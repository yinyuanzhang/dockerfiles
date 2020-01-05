FROM alpine:3.8

RUN addgroup -g 1000 appuser && \
    adduser -D -u 1000 -G appuser appuser

RUN apk add --no-cache python3 && \
    apk add --no-cache vim && \
    apk add --no-cache git && \
    apk add --no-cache dos2unix && \
    apk add --no-cache sudo && \
    apk add --no-cache curl && \
    apk add --no-cache libxml2-utils && \
    apk add --no-cache libxml2-dev && \
    apk add --no-cache neovim

RUN cd /tmp \
 && git clone https://github.com/powerline/fonts.git \
 && cd /tmp/fonts \
 && ./install.sh
 
# Python stuff
RUN pip3 install --no-cache-dir --upgrade pip 
    #pip3 install howdoi


COPY _vimrc /home/appuser/.vimrc
RUN dos2unix /home/appuser/.vimrc
RUN mkdir /data

USER appuser 
RUN curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
RUN vim +PlugInstall +qall

# On Windows continainer won't user appuser, when starting in LCOW mode -> container starts as root, and its not possible to "su" to appuser ...
USER root
RUN cp -r /home/appuser/.vim /root
RUN cp -r /home/appuser/.vimrc /root
USER appuser 
ENTRYPOINT ["/bin/sh"]

