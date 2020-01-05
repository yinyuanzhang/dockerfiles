FROM archlinux/base

ENV HOME /root
ENV GOPATH /root/go
ENV USER root

WORKDIR /root

ADD spacemacs /root/.spacemacs

# Basic requirements
RUN pacman -Sy --noconfirm emacs go dep base-devel git

# Emacs
RUN git clone https://github.com/syl20bnr/spacemacs ~/.emacs.d &&\
      emacs --script ~/.emacs.d/init.el &&\
      emacs --script ~/.emacs.d/init.el

# Pyenv
RUN curl https://pyenv.run | bash &&\
      echo 'export PATH="/root/.pyenv/bin:/root/go/bin:$PATH"' >> ~/.bashrc &&\
      echo 'eval "$(pyenv init -)"' >> ~/.bashrc &&\
      echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc &&\
      source ~/.bashrc

# Python 2.7.15
RUN source ~/.bashrc &&\
      pyenv install 2.7.15 &&\
      pyenv shell 2.7.15 &&\
      pip install ipython flake8 mock pyflakes pylint pytest yapf

# Python 3.6.8
RUN source ~/.bashrc &&\
      pyenv install 3.6.8 &&\
      pyenv shell 3.6.8 &&\
      pip install ipython flake8 flake8-mypy mock pyflakes pylint pytest pytest-mypy yapf

# Go dev libraries
RUN go get -u github.com/nsf/gocode &&\
      go get -u github.com/dougm/goflymake &&\
      # gometalinter
      cd ~/go &&\
      curl -L https://git.io/vp6lP | sh

