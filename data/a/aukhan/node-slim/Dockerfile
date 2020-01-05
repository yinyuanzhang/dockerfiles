FROM node:6-slim

# bringing in python 2.7.15 Dockerfile shamelessly
# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8
# https://github.com/docker-library/python/issues/147
ENV PYTHONIOENCODING UTF-8

# runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates \
		libgdbm3 \
		libreadline6 \
		libsqlite3-0 \
		libssl1.0.0 \
		netbase \
	&& rm -rf /var/lib/apt/lists/*

ENV GPG_KEY C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF
ENV PYTHON_VERSION 2.7.15

RUN set -ex \
	&& buildDeps=" \
					dpkg-dev \
					gcc \
					libbz2-dev \
					libc6-dev \
					libdb-dev \
					libgdbm-dev \
					libncursesw5-dev \
					libreadline-dev \
					libsqlite3-dev \
					libssl-dev \
					make \
					tcl-dev \
					tk-dev \
					wget \
					xz-utils \
					zlib1g-dev \
					# as of Stretch, "gpg" is no longer included by default
					$(command -v gpg > /dev/null || echo 'gnupg dirmngr') \
	" \
	&& apt-get update && apt-get install -y $buildDeps build-essential --no-install-recommends && rm -rf /var/lib/apt/lists/* \
	\
	&& wget -O python.tar.xz "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz" \
	&& wget -O python.tar.xz.asc "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \
	&& gpg --batch --verify python.tar.xz.asc python.tar.xz \
	&& rm -rf "$GNUPGHOME" python.tar.xz.asc \
	&& mkdir -p /usr/src/python \
	&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \
	&& rm python.tar.xz \
	\
	&& cd /usr/src/python \
	&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
	&& ./configure \
		--build="$gnuArch" \
		--enable-shared \
		--enable-unicode=ucs4 \
	&& make -j "$(nproc)" \
	&& make install \
	&& ldconfig \
	\
	&& apt-get purge -y --auto-remove $buildDeps \
	\
	&& find /usr/local -depth \
		\( \
			\( -type d -a \( -name test -o -name tests \) \) \
			-o \
			\( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
		\) -exec rm -rf '{}' + \
	&& rm -rf /usr/src/python

# installing what node-gyp needs to compile modules (make,g++)
RUN set -ex; \
			\
			apt-get update; \
			apt-get install -y --no-install-recommends build-essential; \
			rm -rf /var/lib/apt/lists/*;

CMD [ "node" ]
