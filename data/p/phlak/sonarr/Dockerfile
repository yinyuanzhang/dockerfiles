FROM alpine:edge
MAINTAINER Chris Kankiewicz <Chris@ChrisKankiewicz.com>

# Define Sonarr version
ENV SONARR_VERSION 2.0.0.4409

# Create Sonarr directories
RUN mkdir -pv /opt/sonarr

# Create non-root user
RUN adduser -Ds /sbin/nologin sonarr

# Enable testing repo
RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

# Install dependencies
RUN apk add --update mono@testing libmediainfo@testing sqlite \
    && rm -rf /var/cache/apk/*

# Set Sonarr archive URL
ENV TARBALL_URL https://download.sonarr.tv/v2/master/mono/NzbDrone.master.${SONARR_VERSION}.mono.tar.gz

# Install dependencies, fetch Sonarr archive and chown files
RUN apk add --update ca-certificates tar wget \
    && wget -qO- ${TARBALL_URL} | tar -xz --strip-components=1 -C /opt/sonarr \
    && apk del tar wget && rm -rf /var/cache/apk/* \
    && chown -R sonarr:sonarr /opt/sonarr

# Expose ports
EXPOSE 8989

# Set running user
USER sonarr

# Set docker volumes
VOLUME ~/.config/NzbDrone

# Default command
CMD ["mono", "--debug", "/opt/sonarr/NzbDrone.exe"]
