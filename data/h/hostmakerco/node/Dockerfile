FROM node:8
ENV DEBIAN_FRONTEND noninteractive

# Update system and install Python, en_US.UTF-8 locale, Docker
RUN apt-get update -qq && apt-get dist-upgrade -y -o DPkg::options::='--force-confdef' -o Dpkg::Options::='--force-confold' && \
    apt-get install -y -q python-dev python-pip locales sudo apt-transport-https ca-certificates curl gnupg2 software-properties-common -o DPkg::options::='--force-confdef' -o Dpkg::Options::='--force-confold' && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \    
    apt-get update -qq && \
    apt-get install -y -q docker-ce -o DPkg::options::='--force-confdef' -o Dpkg::Options::='--force-confold' && \
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 && \
    apt-get clean && \
    apt-get autoremove -y -o DPkg::options::='--force-confdef' -o Dpkg::Options::='--force-confold' && \
    rm -rf /var/lib/apt/lists/*

# Instal AWS tools
RUN pip install awscli

# Install packages
RUN apt-key adv --no-tty --keyserver keyserver.ubuntu.com --recv-keys A4A9406876FCBD3C456770C88C718D3B5072E1F5 46095ACC8548582C1A2699A9D27D666CD88E42B4 6572BBEF1B5FF28B28B706837E3F070089DF5277 72ECF46A56B4AD39C907BBB71646B01B86E50310 7B2C3B0889BF5709A105D03AC2518248EEA14886 && \
    apt-get update -qq && \
    apt-get install -y -q apt-transport-https -o DPkg::options::='--force-confdef' -o Dpkg::Options::='--force-confold' && \
    echo "deb http://repo.mysql.com/apt/debian/ stretch mysql-5.7" > /etc/apt/sources.list.d/mysql.list && \
    echo debconf mysql-server mysql-server/root_password password '' | debconf-set-selections && \
    apt-get update -qq && \
    apt-get dist-upgrade -y -o DPkg::options::='--force-confdef' -o Dpkg::Options::='--force-confold' && \
    apt-get install -y -q --force-yes default-libmysqlclient-dev mysql-client vim bzip2 git software-properties-common unoconv -o DPkg::options::='--force-confdef' -o Dpkg::Options::='--force-confold' && \
    apt-get clean && \
    apt-get autoremove -y -o DPkg::options::='--force-confdef' -o Dpkg::Options::='--force-confold' && \
    rm -rf /var/lib/apt/lists/*
