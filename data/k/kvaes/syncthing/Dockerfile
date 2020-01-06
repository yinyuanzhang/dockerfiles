FROM ubuntu:15.04

# Initial Fork from https://github.com/tianon/dockerfiles/blob/6413e7bd54ad6826360fab13efe662cd7a1431e5/syncthing/Dockerfile
MAINTAINER docker@kvaes.be

RUN apt-get update && apt-get install -y ca-certificates --no-install-recommends && rm -rf /var/lib/apt/lists/*

# gpg: key 00654A3E: public key "Syncthing Release Management <release@syncthing.net>" imported
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys 37C84554E7E0A261E4F76E1ED26E6ED000654A3E

ENV SYNCTHING_VERSION 0.12.17
ENV SYNCTHING_USER syncthing

RUN useradd --create-home ${SYNCTHING_USER}

RUN set -x \
        && apt-get update && apt-get install -y xmlstarlet curl --no-install-recommends && rm -rf /var/lib/apt/lists/* \
        && tarball="syncthing-linux-amd64-v${SYNCTHING_VERSION}.tar.gz" \
        && curl -fSL "https://github.com/syncthing/syncthing/releases/download/v${SYNCTHING_VERSION}/"{"$tarball",sha1sum.txt.asc} -O \
        && apt-get purge -y --auto-remove curl \
        && gpg --verify sha1sum.txt.asc \
        && grep -E " ${tarball}\$" sha1sum.txt.asc | sha1sum -c - \
        && rm sha1sum.txt.asc \
        && tar -xvf "$tarball" --strip-components=1 "$(basename "$tarball" .tar.gz)"/syncthing \
        && mv syncthing /usr/local/bin/syncthing \
        && rm "$tarball"

WORKDIR /home/syncthing
# Generate Config to ensure accessibility from outside the container
RUN su -l syncthing -c "syncthing -generate=/home/syncthing/.config/syncthing"
RUN xmlstarlet ed -L -u "/configuration/gui/address" -v "0.0.0.0:8384" "/home/syncthing/.config/syncthing/config.xml"
# The "generate" function also created the certificates. These are used to define each deployment as unique. We'll be removing them to force recreation upon initial container start.
RUN rm /home/syncthing/.config/syncthing/*.pem
# Let's precreate the default sync directory
RUN mkdir /home/syncthing/Sync
RUN chown syncthing:syncthing /home/syncthing/Sync

# Define the default sync volume as a volume
VOLUME ["/home/syncthing/Sync"]

# Firewall Rules : http://docs.syncthing.net/users/firewall.html
EXPOSE 8384/tcp
EXPOSE 22000/tcp
EXPOSE 21027/udp

# We'll be running as a specific user, and not root ;-)
USER ${SYNCTHING_USER}

CMD ["syncthing"]