FROM python:3.7-alpine3.8

ENV ALPINE_VERSION='3.8'
ENV PYTHON_VERSION='3.7'

ENV SUMMARY="python alpine base image"	\
    DESCRIPTION="Alpine base image. The image use scripts and configurations compatible \
        with redhat openshift."

LABEL summary="$SUMMARY" \
      description="$DESCRIPTION" \
      io.k8s.description="$DESCRIPTION" \
      io.k8s.display-name="python" \
      io.openshift.s2i.scripts-url=image:///usr/libexec/s2i \
      io.s2i.scripts-url=image:///usr/libexec/s2i \
      com.redhat.component="core" \
      name="oondeo/python" \
      version=$ALPINE_VERSION \
      release="1" \
      maintainer="OONDEO <info@oondeo.es>"

ENV \
    # DEPRECATED: Use above LABEL instead, because this will be removed in future versions.
    STI_SCRIPTS_URL=image:///usr/libexec/s2i \
    # Path to be used in other layers to place s2i scripts into
    STI_SCRIPTS_PATH=/usr/libexec/s2i

ENV \
    # The $HOME is not set by default, but some applications needs this variable
    HOME=/opt/app-root/src \
    PATH=/opt/app-root/src/bin:/opt/app-root/bin:$STI_SCRIPTS_PATH:$PATH

# When bash is started non-interactively, to run a shell script, for example it
# looks for this variable and source the content of this file. This will enable
# the SCL for all scripts without need to do 'scl enable'.
ENV BASH_ENV=/opt/app-root/etc/scl_enable \
    ENV=/opt/app-root/etc/scl_enable \
    XDG_DATA_HOME=$HOME/.local/share \
    DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 LANGUAGE=C.UTF-8 LC_ALL=C.UTF-8 \
    PROMPT_COMMAND=". /opt/app-root/etc/scl_enable"

USER root

#Use dash instead busybox
#edge repository breaks installs
#RUN echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories && \
#RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories 
#    echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories 
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
    && echo "@edgecommunity http://nl.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
    && echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
    && apk add --no-cache tini dash bash rsync git \
    && ln /usr/bin/dash /bin/dash \
    && ln /bin/bash /usr/bin/bash \
    && chmod g=u /etc/passwd

COPY /root/root/ /

RUN mkdir -p /etc/skel /opt/app-root/src /opt/app-root/etc /opt/app-root/bin /opt/app-root/lib \
        /opt/app-root/var/log /opt/app-root/var/run

# Directory with the sources is set as the working directory so all STI scripts
# can execute relative to this path.
WORKDIR ${HOME}


# FROM python:$PYTHON_VERSION-alpine$ALPINE_VERSION as python
# RUN apk add --no-cache --virtual .build-deps  $BUILD_DEPS
ENV VENV_HOME="$HOME/.env" \
    PYTHON_BIN="python" 

ENV PIP_NO_CACHE_DIR=off \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    PYTHONDONTWRITEBYTECODE='' \
    PIP_BIN="pip"

ARG RUN_DEPS='curl rsync git'
RUN apk-install -t .run-deps $RUN_DEPS

ENV BUILD_DEPS=' \
        bzip2-dev \
		coreutils \
		dpkg-dev dpkg \
		expat-dev \
		findutils \
		gcc \
		gdbm-dev \
		libc-dev \
		libffi-dev \
		libnsl-dev \
		libressl-dev \
		libtirpc-dev \
		linux-headers \
		make \
		ncurses-dev \
		pax-utils \
		readline-dev \
		sqlite-dev \
		tcl-dev \
		tk \
		tk-dev \
		util-linux-dev \
		xz-dev \
        zlib-dev \
        git \
        unzip \
        xmlsec-dev \
        libxslt-dev \
        jpeg-dev \
        cyrus-sasl-dev \
        openldap-dev \
        fontconfig-dev \
        libxml2-dev \
        postgresql-dev \
        mariadb-dev \
    ' 
ARG PYTHON_MODULES=" \
     Babel \
     cffi \
     codecov \
     coverage \
     coveralls \
     crypto \
     gevent \
     greenlet \
     Jinja2 \
     lxml \
     lasso \
     num2words \
     numpy \
     oauthlib \
     ofxparse \
     paramiko \
     passlib \
     phonenumbers \
     Pillow \
     psycopg2 \
     pydot \
     pyldap \
     PyMySQL \
     pyopenssl \
     pyserial \
     python-dateutil \
     python-stdnum \
     pytz \
     pyusb \
     PyYAML \
     requests \
     simplejson \
     tz \
     unicodecsv \
     unidecode \
     unittest2 \
     uwsgi \
     Werkzeug \
     wheel \
     ptvsd \
     "

RUN apk-install -t .build-deps $BUILD_DEPS \
    && pip install --no-cache-dir $PYTHON_MODULES \
    && python -m compileall /usr/local/lib || true \    
    && install-deps /usr/local \
    && rm -rf ~/.cache/pip  /tmp/*

RUN useradd -u 1001 -r -g 0 -d ${HOME} -s /sbin/nologin \
      -c "Default Application User" default  || true
RUN adduser -u 1001 -s /bin/dash -G root -h ${HOME} default || true    
RUN chown -R 1001:0 /opt/app-root \
    && chmod -R g+w /opt/app-root \
    && chmod ug+s /opt/app-root/* \
    && mkdir -p ${HOME}/.pki/nssdb \
    && chown -R 1001:0 ${HOME}/.pki \
    && chown -R 1001:0 /var/log \
    && chmod -R 777 /var/log \
    && chmod 777 /var/run && chmod 775 /run \
    && chmod ug+s /run /var/run \
    && chown 1001 /var/run /run 

ENTRYPOINT [ "/sbin/tini", "-g" ,"--", "container-entrypoint" ]
CMD [ "python3" ]

USER 1001