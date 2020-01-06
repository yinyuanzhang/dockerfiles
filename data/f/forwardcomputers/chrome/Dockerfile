FROM ubuntu:rolling
LABEL maintainer="Ali Mustakim <alim@forwardcomputers.com>" \
      org.label-schema.name="replace_SHORT_NAME" \
      org.label-schema.url="https://hub.docker.com/r/forwardcomputers/replace_SHORT_NAME"
#
ENV user=duser \
    uid=1001 \
    gid=1001
#
# A few minor docker-specific tweaks
#
RUN set -xe \
&&  export user=${user} uid=${uid} gid=${gid} \
&&  echo "#!/bin/sh" > /usr/sbin/policy-rc.d \
&&  echo "exit 101" >> /usr/sbin/policy-rc.d \
&&  chmod +x /usr/sbin/policy-rc.d \
&&  dpkg-divert --local --rename --add /sbin/initctl \
&&  cp --archive /usr/sbin/policy-rc.d /sbin/initctl \
&&  sed --in-place "s/^exit.*/exit 0/" /sbin/initctl \
&&  echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/docker-apt-speedup \
&&  echo 'Dir::Cache::pkgcache ""; Dir::Cache::srcpkgcache "";' > /etc/apt/apt.conf.d/docker-clean \
&&  echo 'Acquire::Languages "none";' > /etc/apt/apt.conf.d/docker-no-languages \
&&  echo 'Acquire::GzipIndexes "true"; Acquire::CompressionTypes::Order:: "gz";' > /etc/apt/apt.conf.d/docker-gzip-indexes \
&&  echo 'Apt::AutoRemove::SuggestsImportant "false";' > /etc/apt/apt.conf.d/docker-autoremove-suggests \
&&  mkdir --parents /run/systemd && echo "docker" > /run/systemd/container \
#
# Update Ubunty repos and install application
#
&&  apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends --yes \
	ca-certificates \
	fonts-liberation \
	hicolor-icon-theme \
	libappindicator3-1 \
	libasound2 \
	libcanberra-gtk*-module \
	libgl1 \
	libgl1-mesa-dri \
	libnspr4 \
	libnss3 \
	libpulse0 \
	libv4l-0 \
	libxft2 \
	libxss1 \
	libxtst6 \
	lsb-release \
	wget \
	xdg-utils \
&&  wget --no-check-certificate --progress=dot --quiet "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" \
&&  dpkg --install ./google-chrome*.deb \
&&  apt-get install --fix-broken --no-install-recommends --yes \
#
# Clean-up
#
&&  apt-get autoremove --yes \
&&  rm --recursive --force \
	./google-chrome*.deb \
	/usr/share/doc/* \
	/usr/share/man/* \
	/var/cache/apt/archives/*.deb \
	/var/cache/apt/archives/partial/*.deb \
	/var/cache/apt/*.bin \
	/var/cache/debcong/*.old \
	/var/lib/apt/lists/* \
	/var/lib/dpkg/info/* \
	/var/log/apt \
	/var/log/*.log \
#
# Create unprivileged user
#
&&  groupadd --gid ${gid} ${user} \
&&  useradd --create-home --shell /bin/bash --uid ${uid} --gid ${gid} --groups audio,video --comment ${user} ${user} \
&&  if [ -d "/etc/sudoers.d" ]; then echo "${user} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/duser; fi
#
USER ${user}
ENTRYPOINT [ "google-chrome-stable" ]
