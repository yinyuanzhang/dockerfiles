FROM ubuntu
MAINTAINER ROCKTAKEY <rocktakey@gmail.com>

RUN apt -y update                                                 && \
    apt -y install git                                            && \
    apt -y install software-properties-common                     && \
    add-apt-repository -y ppa:kelleyk/emacs                       && \
    apt -y update                                                 && \
    apt -y install emacs26                                        && \
    mkdir ~/.emacs.d/                                             && \
    touch ~/.emacs.d/init.el                                      && \
    echo "(package-initialize)" >  ~/.emacs.d/init.el             && \
    echo "(add-to-list"         >> ~/.emacs.d/init.el             && \
    echo " 'package-archives"   >> ~/.emacs.d/init.el             && \
    echo " '(\"melpa\" . \"https://melpa.milkbox.net/packages/\"))"  \
    >> ~/.emacs.d/init.el                                         && \
    echo                                                             \
    "(define-key key-translation-map (kbd \"C-h\") (kbd \"DEL\"))"   \
    >> ~/.emacs.d/init.el                                         && \
    apt install -y python curl                                    && \
    curl -fsSL https://raw.githubusercontent.com/cask/cask/master/go \
    | python

ENV PATH "~/.cask/bin:$PATH"
