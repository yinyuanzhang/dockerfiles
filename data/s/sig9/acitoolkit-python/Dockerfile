FROM python:3.6.2-alpine3.6

RUN apk update \
 && apk add bash gcc git graphviz-dev musl-dev vim \
 && mkdir /opt \
 && cd /opt \
 && git clone -b develop https://github.com/sig9org/acitoolkit \
 && cd acitoolkit \
 && python setup.py install \
 && rm -rf /var/cache/apk/* \
 && echo 'set paste' >> /root/.vimrc \
 && echo "alias ls='ls --color'" >> /root/.bashrc \
 && echo "export PS1='\[\033[01;36m\]atk-3.6.1\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> /root/.bashrc
WORKDIR /opt/acitoolkit
CMD ["/bin/bash"]
