FROM electronuserland/builder:wine

# Install OpenJDK 8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

RUN apt-get update \
  && apt-get install -y --no-install-recommends curl ca-certificates locales \
  && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
  && locale-gen en_US.UTF-8 \
  && rm -rf /var/lib/apt/lists/*

ENV JAVA_VERSION jdk8u222-b10

RUN set -eux; \
  ESUM='37356281345b93feb4212e6267109b4409b55b06f107619dde4960e402bafa77'; \
  BINARY_URL='https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u222-b10/OpenJDK8U-jdk_x64_linux_hotspot_8u222b10.tar.gz'; \
  curl -LfsSo /tmp/openjdk.tar.gz ${BINARY_URL}; \
  echo "${ESUM} */tmp/openjdk.tar.gz" | sha256sum -c -; \
  mkdir -p /opt/java/openjdk; \
  cd /opt/java/openjdk; \
  tar -xf /tmp/openjdk.tar.gz --strip-components=1; \
  rm -rf /tmp/openjdk.tar.gz;

ENV JAVA_HOME=/opt/java/openjdk \
  PATH="/opt/java/openjdk/bin:$PATH"

ENV NODE_VERSION 10.16.3
RUN curl -L https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz | tar xz -C /usr/local --strip-components=1 && \
  unlink /usr/local/CHANGELOG.md && unlink /usr/local/LICENSE && unlink /usr/local/README.md && \
  # https://github.com/npm/npm/issues/4531
  npm config set unsafe-perm true

RUN apt-get purge -y --auto-remove && rm -rf /var/lib/apt/lists/* && apt-get clean
