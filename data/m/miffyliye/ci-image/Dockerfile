FROM centos:7

MAINTAINER Wang, Tao <i@miffyliye.org>

RUN adduser miffyliye

# install rake & git & docker
RUN yum -y install rake \
    && yum -y install git

# install dotnet core sdk
RUN rpm -Uvh https://packages.microsoft.com/config/rhel/7/packages-microsoft-prod.rpm \
    && yum -y update \
    && yum -y install dotnet-sdk-2.1

# install node.js & yarn & chrome & firefox
RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - \
    && yum -y install nodejs \
    && yum -y install gcc-c++ make \
    && curl --silent --location https://dl.yarnpkg.com/rpm/yarn.repo | tee /etc/yum.repos.d/yarn.repo \
    && yum -y install yarn \
    && yum -y install epel-release \
    && rpm --import https://dl-ssl.google.com/linux/linux_signing_key.pub \
    && sh -c 'echo -e "[google-chrome]\nname=google-chrome\nbaseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64\nenabled=1\ngpgcheck=1\ngpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub" > /etc/yum.repos.d/google-chrome.repo' \
    && yum -y update \
    && yum -y install google-chrome-stable \
    && cd /home/miffyliye \
    && curl --silent --location https://ftp.mozilla.org/pub/firefox/releases/59.0.3/linux-x86_64/en-US/firefox-59.0.3.tar.bz2 --output firefox.tar.bz2 \
    && yum -y install bzip2 \
    && tar xjf firefox.tar.bz2 \
    && yes | rm firefox.tar.bz2 \
    && chown -R miffyliye:miffyliye firefox \
    && ln -s /home/miffyliye/firefox/firefox /usr/bin/firefox \
    && yum -y install libXt

USER miffyliye

CMD /bin/bash
