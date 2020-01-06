FROM openjdk:7

RUN apt-get update -y \
    && apt-get install -y \
        ant             \
        autoconf        \
        automake        \
        bash            \
        gawk            \
        git             \
        make            \
        openssh-client  \
        php5            \
        rsync           \
        time            \
        unzip           \
        wget            \
        texinfo         \
        libxml2-utils   \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Download and install saxon jar
RUN wget https://downloads.sourceforge.net/project/saxon/Saxon-HE/9.8/SaxonHE9-8-0-12J.zip \
    && test "$( sha256sum SaxonHE9-8-0-12J.zip | cut -d' ' -f1 )" = f48be01705ff91881ea5953982db054f8a2f152dcec9f5e76267a2ee4a1f3ded \
    && mkdir -p /usr/share/ant/lib/saxon9/ \
    && unzip SaxonHE9-8-0-12J.zip saxon9he.jar -d /usr/share/ant/lib/saxon9/

# Install NodeJS/NPM
# gpg keys listed at https://github.com/nodejs/node
RUN set -ex \
    && for key in \
        9554F04D7259F04124DE6B476D5A82AC7E37093B \
        94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
        0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
        FD3A5288F042B6850C66B31F09FE44734EB7990E \
        71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
        DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
        B9AE9905FFD7803F25714661B63B535A4C206CA9 \
        C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
    ; do \
        gpg --batch --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \
        gpg --batch --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \
        gpg --batch --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" || \
        gpg --batch --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
    done

ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 4.8.6

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
    && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
    && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
    && grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
    && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
    && rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
    && ln -s /usr/local/bin/node /usr/local/bin/nodejs

# Disable host key checking from within builds as we cannot interactively accept them
# TODO: It might be a better idea to bake ~/.ssh/known_hosts into the container
RUN mkdir -p ~/.ssh
RUN printf "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config
