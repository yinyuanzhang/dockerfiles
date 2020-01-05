FROM ubuntu:rolling
#
ARG RELEASE
LABEL maintainer="Ali Mustakim <alim@forwardcomputers.com>" \
      org.label-schema.name="firefox" \
      org.label-schema.url="https://hub.docker.com/r/forwardcomputers/firefox"
ENV user=duser \
    uid=1001 \
    gid=1001 \
	LANG=C.UTF-8
#
# Some docker tweaks
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
# Update Ubunty repos and install dependencies
#
&&  apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends --yes \
	bzip2 \
	libavcodec-extra58 \
	libasound2 \
	libpulse0 \
	locales \
	wget \
	lsb-release \
	libatk1.0-0 \
	libc6 \
	libcairo-gobject2 \
	libcairo2 \
	libdbus-1-3 \
	libdbus-glib-1-2 \
	libfontconfig1 \
	libfreetype6 \
	libgcc1 \
	libgdk-pixbuf2.0-0 \
  	libglib2.0-0 \
	libgtk-3-0 \
	libpango-1.0-0 \
	libpangocairo-1.0-0 \
	libstartup-notification0 \
	libstdc++6 \
	libx11-6 \
	libx11-xcb1 \
	libxcb-shm0 \
	libxcb1 \
	libxcomposite1 \
	libxdamage1 \
	libxext6 \
	libxfixes3 \
	libxrender1 \
	libxt6 \
	xul-ext-ubufox \
	libcanberra0 \
	fonts-lyx \
#
# Clean-up
#
&&  rm --recursive --force \
	/usr/share/doc/* \
	/usr/share/man/* \
	/var/cache/apt/archives/*.deb \
	/var/cache/apt/archives/partial/*.deb \
	/var/cache/apt/*.bin \
	/var/cache/debcong/*.old \
	/var/lib/apt/lists/* \
	/var/lib/dpkg/info/* \
	/var/log/apt \
	/var/log/*.log
#
# Install application
#
RUN set -xe \
&&  wget --no-check-certificate --progress=dot --quiet --output-document - \
	'https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US' | \
	tar --extract --bzip2 --directory /opt \
&&  chown --recursive ${uid}:${gid} /opt/firefox
#
# Create unprivileged user
#
RUN set -xe \
&&	locale-gen en_US.UTF-8 || true \
&&  groupadd --gid ${gid} ${user} \
&&  useradd --create-home --shell /bin/bash --uid ${uid} --gid ${gid} --groups audio,video --comment ${user} ${user} \
&&  if [ -d "/etc/sudoers.d" ]; then echo "${user} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/duser; fi
#
USER ${user}
WORKDIR /home/${user}
CMD [ "/bin/bash" ]
