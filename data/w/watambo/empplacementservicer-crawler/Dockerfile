FROM centos:centos7
MAINTAINER watambo <watanabe.ryosuke@vi-king.net>
RUN rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7
RUN rpm --import http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7

RUN yum install -y epel-release && \
    yum install -y wget unzip

RUN wget https://chromedriver.storage.googleapis.com/2.42/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    chown root:root /usr/local/bin/chromedriver && \
    yum install -y libX11 GConf2 fontconfig

RUN echo -n > /etc/yum.repos.d/google-chrome.repo && \
    echo $'[google chrome]\n\
name=google-chrome\n\
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch\n\
enabled=1\n\
gpgcheck=1\n\
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub' > /etc/yum.repos.d/google-chrome.repo && \
    curl https://intoli.com/install-google-chrome.sh | bash && \
    yum install -y google-chrome-unstable libOSMesa google-noto-cjk-fonts

RUN yum install -y git gcc zlib-devel bzip2 bzip2-devel readline readline-devel sqlite sqlite-devel openssl openssl-devel libffi-devel.x86_64

ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH


RUN git clone git://github.com/yyuu/pyenv.git ~/.pyenv && \
    pyenv install 3.7.0 && \
    pyenv global 3.7.0 && \
    pyenv rehash && \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
    eval "$(pyenv init -)"

COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

COPY . /app/