################################################################################
# base system
################################################################################
FROM ubuntu:18.10 as system

RUN ln -fs /usr/share/zoneinfo/Europe/Berlin /etc/localtime

# built-in packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends software-properties-common curl apache2-utils \
    && curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg \
    && install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/ \
    && sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list' \
    && apt-get update \
    && apt-get install -y --no-install-recommends --allow-unauthenticated \
    supervisor nginx sudo vim-tiny net-tools zenity xz-utils \
    dbus-x11 x11-utils \
    mesa-utils libgl1-mesa-dri \
    lxde xvfb x11vnc \
    gtk2-engines-murrine gnome-themes-standard gtk2-engines-pixbuf gtk2-engines-murrine arc-theme \
    firefox \
    ttf-ubuntu-font-family \
    apt-transport-https nano git ssh rsync php7.2 php7.2-mbstring php7.2-gd \
    php7.2-bz2 php7.2-zip php7.2-bz2 php7.2-zip php-gmagick iputils-ping \
    gnupg libgconf-2-4 apache2 php-xdebug libapache2-mod-xsendfile php7.2-mysql \
    mysql-workbench mysql-client unzip code mongo-tools \
    && apt-get autoclean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

# tini for subreap                                   
ARG TINI_VERSION=v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /bin/tini
RUN chmod +x /bin/tini

# python library
COPY image/usr/local/lib/web/backend/requirements.txt /tmp/
RUN apt-get update \
    && dpkg-query -W -f='${Package}\n' > /tmp/a.txt \
    && apt-get install -y python-pip python-dev build-essential \
    && pip install setuptools wheel && pip install -r /tmp/requirements.txt \
    && dpkg-query -W -f='${Package}\n' > /tmp/b.txt \
    && apt-get remove -y `diff --changed-group-format='%>' --unchanged-group-format='' /tmp/a.txt /tmp/b.txt | xargs` \
    && apt-get autoclean -y \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/* /tmp/a.txt /tmp/b.txt


################################################################################
# builder
################################################################################
FROM ubuntu:16.04 as builder

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates

# nodejs
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -y nodejs

# yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y yarn

# build frontend
COPY web /src/web
RUN cd /src/web \
    && yarn \
    && npm run build


################################################################################
# merge
################################################################################
FROM system

COPY --from=builder /src/web/dist/ /usr/local/lib/web/frontend/
COPY image /

EXPOSE 80
WORKDIR /root
ENV HOME=/home/ubuntu \
    SHELL=/bin/bash
HEALTHCHECK --interval=30s --timeout=5s CMD curl --fail http://127.0.0.1:6079/api/health
ENTRYPOINT ["/startup.sh"]
