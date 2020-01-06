#-------------------------------------------------------------------------------
#  Name: ngtrieuvi92/sonar-scanner
#  Description: Docker image to easy run sonar scanner
#  Usage:   
#    docker run \
#       -v ./src:/data
#       -e SONAR_USERNAME="$SONAR_USERNAME" \
#       -e SONAR_PASSWORD="$SONAR_PASSWORD" \
#       -e LOCAL_USER_ID=$(id -u $USER)
#       ngtrieuvi92/sonar-scanner 
#
#-------------------------------------------------------------------------------

FROM java:alpine
MAINTAINER vi.nt <vi.nt@geekup.vn>

# Install gosu
ENV GOSU_VERSION 1.9
RUN set -x \
    && apk add --no-cache --virtual .gosu-deps \
        nodejs \
        dpkg \
        gnupg \
        openssl \
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true \
    && apk del .gosu-deps

# Set scanner version
ENV SONAR_SCANNER_VERSION 2.8

# Install sonar scanner
RUN apk add --no-cache wget && \
    wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-${SONAR_SCANNER_VERSION}.zip && \
    unzip sonar-scanner-${SONAR_SCANNER_VERSION} && \
    cd /usr/bin && ln -s /sonar-scanner-${SONAR_SCANNER_VERSION}/bin/sonar-scanner sonar-scanner && \
    apk del wget

# Create /data directory and set as mount volume & workir
RUN mkdir /data
VOLUME /data
WORKDIR /data

# Add ENTRYPOINT 
ADD entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
CMD sonar-scanner -Dsonar.login=$SONAR_USERNAME -Dsonar.password=$SONAR_PASSWORD
