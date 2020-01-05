FROM mcr.microsoft.com/powershell:preview-alpine-3.8
LABEL maintainer "Ilya Glotov <contact@ilyaglotov.com>"

ENV EMPIRE_USER empire

# Reference: https://github.com/EmpireProject/Empire/blob/master/setup/install.sh
RUN apk update \
  && apk add --no-cache fts-dev \
                        git \
                        libcap \
                        libffi-dev \
                        libxml2-dev \
                        openjdk8 \
                        openssl \
                        openssl-dev \
                        py-pip \
                        python \
                        python-dev \
                        swig \
                        \
  && ln -s /usr/lib/jvm/default-jvm/bin/javac /usr/bin/javac \
  && apk add --virtual .build-deps \
                        autoconf \
                        build-base \
                        linux-headers \
                        \
  && rm -rf /var/cache/apk/* \
  \
  # Install xar from sources
  && git clone --depth=1 \
              --branch=master \
              https://github.com/mackyle/xar.git \
  && cd /xar/xar \
  && ./autogen.sh --noconfigure \
  && ./configure LDFLAGS=-lfts \
  && make \
  && make install \
  && cd / \
  && rm -rf /xar \
  \
  # Install bomutils from sources
  && git clone --depth=1 \
              --branch=master \
              https://github.com/hogliux/bomutils.git \
  && cd bomutils \
  && make \
  && make install \
  && chmod 755 build/bin/mkbom \
  && cp build/bin/mkbom /usr/local/bin/mkbom \
  && cd / \
  && rm -rf /bomutils \
  \
  # Install Empire's python dependencies
  && pip install cryptography \
                dropbox \
                flask \
                iptools \
                m2crypto \
                macholib \
                netifaces \
                pycrypto \
                pydispatcher \
                pyinstaller \
                pyminifier \
                pyopenssl==17.2.0 \
                setuptools \
                xlrd \
                xlutils \
                zlib_wrapper \
                \
  && rm -rf /root/.cache/pip \
  && apk del .build-deps \
  \
  # Clone Empire repository and clean things up
  && git clone --depth=1 \
              --branch=master \
              https://github.com/EmpireProject/Empire.git \
              /empire \
  && rm -rf /empire/.git \
  && apk del git \
  \
  # Add ability to Empire listeners to bind to low-numbered ports without root
  && setcap cap_net_bind_service=+eip /usr/bin/python2.7 \
  && adduser -D $EMPIRE_USER \
  && chown -R $EMPIRE_USER /empire \
  \
  # Put downloads to a volume
  && mkdir -p /data/downloads \
  && ln -s /data/downloads /empire/downloads \
  && chown -R $EMPIRE_USER /data \
  \
  # Add powershell modules to user modules folder
  && mkdir -p /home/empire/.local/share/powershell/Modules \
  && ln -s /empire/lib/powershell/Invoke-Obfuscation \
           /home/empire/.local/share/powershell/Modules/Invoke-Obfuscation \
  && chmod -R +x /opt/microsoft/powershell/

VOLUME /data

COPY entrypoint.sh /tmp/entrypoint.sh
RUN chmod +x /tmp/entrypoint.sh

USER $EMPIRE_USER

EXPOSE 80 443 1337 8080

WORKDIR /empire

ENTRYPOINT ["/tmp/entrypoint.sh"]
