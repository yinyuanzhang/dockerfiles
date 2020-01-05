FROM centos:7
LABEL maintainer "okisanjp <okisan.jp@gmail.com>"

# yum update
RUN yum -y update && yum clean all

# localize to japanese
ENV LANG="ja_JP.UTF-8" \
    LC_ALL="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja"
		
RUN yum -y reinstall glibc-common && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
    unlink /etc/localtime && \
    ln -s /usr/share/zoneinfo/Japan /etc/localtime

# install rbenv
RUN yum -y install \
    git \
    bzip2 \
    gcc \
    openssl \
    openssl-devel \
    readline-devel

RUN git clone https://github.com/sstephenson/rbenv.git ~/.rbenv
RUN git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build

ENV PATH="~/.rbenv/bin:$PATH" \
    CONFIGURE_OPTS="--disable-install-rdoc"

RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bash_profile
RUN echo 'eval "$(rbenv init -)"' >> ~/.bash_profile

# install ruby
RUN  rbenv install 2.3.0 && rbenv global 2.3.0
