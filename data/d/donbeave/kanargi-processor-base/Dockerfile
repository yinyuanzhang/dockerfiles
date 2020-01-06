# build uchardet

FROM openjdk:11.0.2-jre-slim-stretch AS uchardet

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y \
            git \
            build-essential \
            cmake

RUN git clone git://anongit.freedesktop.org/uchardet/uchardet \
    && cd uchardet \
    && cmake -DCMAKE_INSTALL_PREFIX=/ . \
    && make \
    && make install

RUN /usr/bin/uchardet --version

# @end build uchardet



# build ced

FROM openjdk:11.0.2-jre-slim-stretch AS ced

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y \
            git \
            build-essential \
            curl \
            software-properties-common

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -

RUN apt-get install -y nodejs

RUN node -v

RUN mkdir /cedjs

WORKDIR /cedjs

RUN git clone https://github.com/sonicdoe/ced.git \
    && cd ced/vendor \
    && mv compact_enc_det/binding.gyp . \
    && rm -rf compact_enc_det \
    && git clone https://github.com/google/compact_enc_det.git \
    && mv binding.gyp compact_enc_det/

WORKDIR /cedjs

RUN npm install ced

# @end build ced



FROM openjdk:11.0.2-jre-slim-stretch

MAINTAINER Alexey Zhokhov <alexey@zhokhov.com>

RUN echo 'deb http://deb.debian.org/debian stretch main contrib non-free' > /etc/apt/sources.list.d/stretch-backports.list

ADD test.txt /test.txt

# install uchardet
COPY --from=uchardet /usr/bin/uchardet /usr/bin/uchardet
COPY --from=uchardet /usr/lib/libuchardet.so.0.0.6 /usr/lib/libuchardet.so.0.0.6

RUN ln -s /usr/lib/libuchardet.so.0.0.6 /usr/lib/libuchardet.so.0

RUN /usr/bin/uchardet /test.txt
# @end install uchardet

# install Node.js
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
               curl \
               software-properties-common \
    && curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/* \
              /tmp/*
# @end install Node.js

# install ced
COPY --from=ced /cedjs /usr/local/share/cedjs

ADD ced/ced.js /usr/local/share/cedjs/
ADD ced/ced /usr/bin/ced

RUN chmod a+x /usr/bin/ced

RUN /usr/bin/ced /test.txt
# @end install ced

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
               curl \
               unzip \
               bsdtar \
               locales \
               locales-all \
    && rm -rf /var/lib/apt/lists/* \
              /tmp/*

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
               p7zip-full \
               unrar-free \
               p7zip-rar \
    && rm -rf /var/lib/apt/lists/* \
              /tmp/*

RUN locale-gen "en_US.UTF-8"
