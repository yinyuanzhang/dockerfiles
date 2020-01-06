FROM fedora:latest

RUN curl --silent --location https://rpm.nodesource.com/setup_12.x | bash -
RUN curl --silent --location https://dl.yarnpkg.com/rpm/yarn.repo | sudo tee /etc/yum.repos.d/yarn.repo
RUN dnf -y install \
    git \
    nodejs \
    libpng-devel \
    make \
    gcc \
    gcc-c++ \
    patch \
    yarn
    

ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /sbin/tini
RUN chmod +x /sbin/tini

RUN mkdir /.npm
RUN chmod 777 -R /.npm

RUN mkdir /.cache
RUN chmod 777 -R /.cache

RUN touch /.yarnrc
RUN chmod 777 -R /.yarnrc

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

WORKDIR /app

ENTRYPOINT ["/bin/sh", "/docker-entrypoint.sh"]

CMD ["yarn"]