# Build
# docker build -t easii:`date +%Y-%m-%d_``git rev-parse --short HEAD` .

# Start
# docker run -p 34543:20000 -it --entrypoint /bin/bash easii:2019-06-13_398b544c

# Inspect
# docker ps
# docker exec -it <CONTAINER ID> /bin/bash


FROM ubuntu:18.04

ARG RAKUDO_SHA=0dd6573a45f61652a2c5166468362e71562f6dd7

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -yq \
        make netcat-openbsd build-essential \
        sqlite3 libsqlite3-dev \
        git libexpat1-dev \
        libarchive-dev \
        libssl-dev \
        joe \
        libperl-dev gcc gnupg \
        ca-certificates lsb-release \
        apt-utils perl \
        curl libyaml-dev && \
    curl https://dl-ssl.google.com/linux/linux_signing_key.pub | \
         apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome-unstable.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive  apt-get install -yq \
    google-chrome-unstable fonts-ipafont-gothic fonts-wqy-zenhei \
    fonts-thai-tlwg fonts-kacst \
      --no-install-recommends && \
    apt-get remove -yq google-chrome-unstable && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \
        --recv 379CE192D401AB61 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl https://cpanmin.us/ | perl - \
    Spreadsheet::ParseXLSX \
    Excel::Writer::XLSX && \
    groupadd easii && \
    useradd -m -g easii -s /bin/bash easii

ENV PATH $PATH:/opt/rakudo/bin:/opt/rakudo/share/perl6/site/bin

RUN git clone https://github.com/rakudo/rakudo/ /opt/rakudo-src && \
    cd /opt/rakudo-src && \
    git checkout ${RAKUDO_SHA} && \
    perl Configure.pl \
        --gen-moar \
        --prefix=/opt/rakudo \
        --relocatable \
        --gen-nqp \
        --backends=moar && \
    make && make install && \
    cd ~ && \
    rm -rf /opt/rakudo-src

COPY META6.json /tmp/

RUN git clone https://github.com/ugexe/zef.git /opt/zef-src && \
    cd /opt/zef-src && \
    perl6 -I. bin/zef install . && \
    cd ~ && \
    rm -rf /opt/zef-src && \
    cd /tmp && \
    zef --deps-only --/test --install-to=site install . && \
    zef --installed list

USER easii

COPY frontend/package.json frontend/package-lock.json /home/easii/

RUN cd /home/easii && \
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash && \
    export NVM_DIR=/home/easii/.nvm && \
    cd /home/easii && \
    . ~/.nvm/nvm.sh && \
    nvm install 10 && \
    npm install

ENV NVM_DIR /home/easii/.nvm

EXPOSE 20000

COPY bin/entrypoint.sh /home/easii/

USER root
ENTRYPOINT ["/home/easii/entrypoint.sh"]
CMD ["gugus"]
