FROM python:3.5.3-alpine

RUN apk update \
 && apk add bash gcc git graphviz-dev musl-dev vim \
 && mkdir /opt \
 && cd /opt \
 && git clone -b develop https://github.com/sig9org/acitoolkit \
 && cd acitoolkit \
 && python setup.py install \
 && rm -rf /var/cache/apk/* \
 && echo 'export PS1="[acitoolkit-3.5.3 \W]\$ "' > /root/.bashrc
ADD vimrc /root/.vimrc
WORKDIR /opt/acitoolkit
CMD ["/bin/bash"]
