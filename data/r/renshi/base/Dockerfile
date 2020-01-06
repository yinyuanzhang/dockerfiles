##### ################################################################
#####
#####    Base
#####    ====
#####      https://cloud.docker.com/repository/registry-1.docker.io/renshi/base
#####
#####    Build
#####    -----
#####      docker build -t renshi/base -f Dockerfile.Base .
#####
#####    Run
#####    ---
#####      docker run -it renshi/base /bin/bash
#####
##### ################################################################
FROM opensuse/tumbleweed

MAINTAINER Renshi <yanqirenshi@gmail.com>


##### ################################################################
#####  Install of zypper
##### ################################################################
USER root

RUN zypper --non-interactive refresh
RUN zypper --non-interactive update

RUN zypper --non-interactive install -t pattern devel_basis
RUN zypper --non-interactive install libffi-devel libyaml-devel libopenssl-devel readline-devel bzip2
RUN zypper --non-interactive install curl libcurl-devel
RUN zypper --non-interactive install gzip
RUN zypper --non-interactive install libev-devel
RUN zypper --non-interactive install which
RUN zypper --non-interactive install emacs
RUN zypper --non-interactive install git
RUN zypper --non-interactive install nginx


##### ################################################################
#####   Group / User
##### ################################################################
USER root

RUN groupadd cl-users
RUN useradd -d /home/cl-user -m -g cl-users cl-user


##### ################################################################
#####   Node.js
##### ################################################################
USER cl-user
WORKDIR /home/cl-user

RUN curl -L git.io/nodebrew | perl - setup

RUN echo 'export PATH=$HOME/.nodebrew/current/bin:$PATH' >> ~/.bashrc

ENV PATH /home/cl-user/.nodebrew/current/bin:$PATH

RUN nodebrew install stable
RUN nodebrew use stable


##### ################################################################
#####   Riot.js
##### ################################################################
USER cl-user
WORKDIR /home/cl-user

RUN npm install riot -g


##### ################################################################
#####   Roswell
##### ################################################################
USER cl-user
WORKDIR /home/cl-user

RUN mkdir /home/cl-user/temp
WORKDIR /home/cl-user/temp

RUN git clone -b release https://github.com/roswell/roswell.git

WORKDIR /home/cl-user/temp/roswell
RUN sh bootstrap
RUN ./configure --prefix=/home/cl-user/temp/roswell/.local
RUN make
RUN make install
RUN echo 'PATH=$HOME/.local/bin:$PATH' >> ~/.profile
ENV PATH /home/cl-user/temp/roswell/.local/bin:$PATH
RUN ros setup

# make directoies
RUN mkdir -p /home/cl-user/.asdf/ && \
    mkdir -p /home/cl-user/prj/


# clear init.lisp
RUN echo ';;;;;'                                                      >  ~/.roswell/init.lisp && \
    echo ';;;;; Added Dockerfile'                                     >> ~/.roswell/init.lisp && \
    echo ';;;;;'                                                      >> ~/.roswell/init.lisp


# Setting SBCL
RUN echo ';;;;;'                                                      >> ~/.roswell/init.lisp && \
    echo ';;;;; SBCL'                                                 >> ~/.roswell/init.lisp && \
    echo ';;;;;'                                                      >> ~/.roswell/init.lisp && \
    echo '(setf sb-impl::*default-external-format* :utf-8)'           >> ~/.roswell/init.lisp && \
    echo '(setf sb-alien::*default-c-string-external-format* :utf-8)' >> ~/.roswell/init.lisp


# Setting ASDF
RUN echo ''                                                           >> ~/.roswell/init.lisp && \
    echo ';;;;;'                                                      >> ~/.roswell/init.lisp && \
    echo ';;;;; ASDF'                                                 >> ~/.roswell/init.lisp && \
    echo ';;;;;'                                                      >> ~/.roswell/init.lisp && \
    echo '(push #P"~/.asdf/" asdf:*central-registry*)'                >> ~/.roswell/init.lisp


##### ################################################################
#####   Git Clon Project
##### ################################################################
USER cl-user
WORKDIR /home/cl-user/prj/

###
### libs
###
RUN mkdir -p /home/cl-user/prj/libs/
WORKDIR /home/cl-user/prj/libs/

RUN git clone https://github.com/yanqirenshi/sephirothic.git
RUN git clone https://github.com/yanqirenshi/world2world.git
RUN git clone https://github.com/yanqirenshi/ghost.git
RUN git clone https://github.com/yanqirenshi/takajin84key.git
RUN git clone https://github.com/yanqirenshi/s-serialization
RUN git clone https://github.com/yanqirenshi/plist-printer
RUN git clone https://github.com/yanqirenshi/parser.schema.rb.git
RUN git clone https://github.com/yanqirenshi/lack-middleware-validation.git

RUN ln -s /home/cl-user/prj/libs/sephirothic/sephirothic.asd                               /home/cl-user/.asdf/sephirothic.asd
RUN ln -s /home/cl-user/prj/libs/world2world/world2world.asd                               /home/cl-user/.asdf/world2world.asd
RUN ln -s /home/cl-user/prj/libs/ghost/ghost.asd                                           /home/cl-user/.asdf/ghost.asd
RUN ln -s /home/cl-user/prj/libs/takajin84key/takajin84key.asd                             /home/cl-user/.asdf/takajin84key.asd
RUN ln -s /home/cl-user/prj/libs/s-serialization/s-serialization.asd                       /home/cl-user/.asdf/s-serialization.asd
RUN ln -s /home/cl-user/prj/libs/plist-printer/plist-printer.asd                           /home/cl-user/.asdf/plist-printer.asd
RUN ln -s /home/cl-user/prj/libs/parser.schema.rb/parser.schema.rb.asd                     /home/cl-user/.asdf/parser.schema.rb.asd
RUN ln -s /home/cl-user/prj/libs/lack-middleware-validation/lack-middleware-validation.asd /home/cl-user/.asdf/lack-middleware-validation.asd


###
### Database
###
RUN mkdir -p /home/cl-user/prj/dbs/
WORKDIR /home/cl-user/prj/dbs/

RUN git clone https://github.com/yanqirenshi/upanishad.git
RUN git clone https://github.com/yanqirenshi/shinrabanshou.git

# シンボリックリンクの作成
RUN ln -s /home/cl-user/prj/dbs/upanishad/upanishad.asd         /home/cl-user/.asdf/upanishad.asd
RUN ln -s /home/cl-user/prj/dbs/shinrabanshou/shinrabanshou.asd /home/cl-user/.asdf/shinrabanshou.asd


###
### Strobolights
###
WORKDIR /home/cl-user/prj/

RUN git clone https://github.com/yanqirenshi/strobolights.git

# シンボリックリンクの作成
RUN ln -s /home/cl-user/prj/strobolights/strobolights.asd /home/cl-user/.asdf/strobolights.asd


###
### 起動設定
###
## ~/.roswell/init.lisp
RUN echo '(ql:quickload :woo)'                                   >> /home/cl-user/.roswell/init.lisp
RUN echo '(ql:quickload :upanishad)'                             >> /home/cl-user/.roswell/init.lisp
RUN echo '(ql:quickload :shinrabanshou)'                         >> /home/cl-user/.roswell/init.lisp
RUN echo '(ql:quickload :strobolights)'                          >> /home/cl-user/.roswell/init.lisp

## Load projects
RUN ros --load /home/cl-user/.roswell/init.lisp


##### ################################################################
#####   Emacs
##### ################################################################
USER cl-user
RUN mkdir -p /home/cl-user/.emacs.d/dist/

WORKDIR /home/cl-user/.emacs.d/dist/

###
### git clone projects
###
RUN git clone https://github.com/slime/slime.git
RUN git clone https://github.com/deadtrickster/slime-repl-ansi-color.git
RUN git clone https://github.com/yanqirenshi/emacs.git

###
### .emacs.d/init.lisp
###
RUN touch /home/cl-user/.emacs.d/init.el
RUN echo '(load "~/.emacs.d/dist/emacs/init-base.el")'  >> /home/cl-user/.emacs.d/init.el
RUN echo '(load "~/.emacs.d/dist/emacs/init-lisp.el")'  >> /home/cl-user/.emacs.d/init.el

###
### パッケージのインストール
###
RUN emacs --script /home/cl-user/.emacs.d/dist/emacs/src/package.el
