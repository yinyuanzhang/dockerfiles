FROM debian:stretch-slim

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get -y install vim curl exuberant-ctags vim-nox vim-gnome python python3\
 && apt-get -y --no-install-recommends install git-core \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/

COPY vimrc.local /root/.vimrc.local

RUN curl http://j.mp/spf13-vim3 -L -o - | sh \
 && mkdir -vp /src/ \
 && sed -i 's/amirh\/HTML-AutoCloseTag/vim-scripts\/HTML-AutoCloseTag/g' \
   /root/.vimrc.bundles \
 && grep "vim-scripts/HTML-AutoCloseTag" /root/.vimrc.bundles \
 && vim "+set nomore" "+BundleInstall!" "+BundleClean" "+qall"

COPY ftplugin /root/.vim/ftplugin
COPY snippets /root/.vim/snippets
COPY NERDTreeBookmarks /root/.NERDTreeBookmarks

ENTRYPOINT [ "vim" ]

CMD [ "/home/haular" ]
