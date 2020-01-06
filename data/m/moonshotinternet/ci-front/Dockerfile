FROM node:10.15.2-stretch-slim

LABEL vendor=Moonshot-Internet
LABEL com.moonshot.name=ci-scripts
LABEL com.moonshot.version=1.0.0


# install missing software
RUN apt-get update && apt-get install --no-install-recommends -y python-minimal \
    build-essential \
    python-setuptools \
    python-pip \
    git \
    openssh-client \
    jq \
    vim \
    && rm -rf /var/lib/apt/lists/*

# install some python packages
RUN pip install --no-cache-dir \
    awscli

# install custom py deps
COPY ./docker /tmp/install
RUN pip install -r /tmp/install/gen_doc_requirements.txt \
    && rm -fr /tmp/*

# install hugo
RUN curl -L --output hugo.deb https://github.com/gohugoio/hugo/releases/download/v0.54.0/hugo_0.54.0_Linux-64bit.deb \
    && dpkg -i hugo.deb \
    && rm hugo.deb

# install spectacle-docs
RUN npm install -g --unsafe-perm spectacle-docs

# install gulp
RUN npm install -g gulp-cli gulp

# add scripts
RUN mkdir -p /opt/bin/src
COPY ./src/ /opt/bin/src

# flatten scripts, clean-up dirs, add execution flag to binaries, link'em to the bin PATH
RUN find /opt/bin/src -type f -exec sh -c 'mv "$@" /opt/bin' _ {} + \
    && find /opt/bin/* -type d -depth -exec rmdir {} + \
    && chmod +x /opt/bin/*.sh \
    && chmod +x /opt/bin/*.py \
    && ln -s /opt/bin/*.sh /usr/local/bin/. \
    && ln -s /opt/bin/*.py /usr/local/bin/.

USER node
