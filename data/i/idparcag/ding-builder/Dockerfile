FROM alpine:3.9 as builder

RUN apk --no-cache add \
    ruby \
    ruby-dev \
    make \
    g++

RUN gem install etc:1.0.1 fpm:1.10.2 --no-rdoc --no-ri

FROM idparcag/gcloud-sdk-alpine:254-0-0_1

COPY --from=builder /usr/lib/ruby/gems/ /usr/lib/ruby/gems/
COPY --from=builder /usr/bin/fpm /usr/bin/fpm

ENV ANSIBLE_SSH_PIPELINING=1
ENV NODE_PATH=/usr/lib/node_modules
ENV CONFIG_PATH=/config

RUN apk --no-cache add \
    curl \
    patch \
    openssh \
    tar \
    bash \
    ruby \
    nodejs \
    openjdk8 \
    python3 \
    py3-cryptography \
    py3-markupsafe \
    py3-yaml \
    py3-bcrypt \
    py3-pynacl \
    py3-jinja2 \
    py3-paramiko \
    py3-docutils \
    py3-rsa \
    py3-asn1 \
    py3-dateutil \
    cpio \
    rpm \
    git \
    openssl \
    rsync \
    xz \
    coreutils \
    npm \
    jq

RUN pip3 install ansible==2.6.4 awscli==1.16.18

RUN curl -L https://github.com/sbt/sbt/releases/download/v1.2.4/sbt-1.2.4.tgz | tar -xz -C /usr/bin --strip 2 sbt/bin/

RUN curl -L https://unpkg.com/@pnpm/self-installer | PNPM_VERSION=2.16.0 node

RUN npm config set user 0
RUN npm config set unsafe-perm true
RUN npm install -g browserify node-sass rimraf babel-cli envify uglify-es uglifyify

RUN ln -s /usr/lib/jvm/java-1.8-openjdk/bin/javadoc /bin/javadoc
ENV JAVA_HOME=/usr/lib/jvm/default-jvm
