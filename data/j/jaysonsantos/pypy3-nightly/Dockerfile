# Dockerfile based on pypy official's Dockerfile
FROM buildpack-deps:jessie

# ensure local pypy is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
		tcl \
		tk \
	&& rm -rf /var/lib/apt/lists/*

# Incremental build + the commit hash?
ENV PYPY_VERSION 90584-25aaba6da424
ENV PYPY_SHA256SUM 08628f53acd88dc8246e30c55abc0d32a85fb0f1788dbf96c18afa9ca0c5e918

# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid truth value '<VERSION>'"
ENV PYTHON_PIP_VERSION 9.0.1

RUN set -ex \
	&& wget -O pypy.tar.bz2 "http://buildbot.pypy.org/nightly/py3.5/pypy-c-jit-${PYPY_VERSION}-linux64.tar.bz2" \
	&& echo "$PYPY_SHA256SUM  pypy.tar.bz2" | sha256sum -c \
	&& tar -xjC /usr/local --strip-components=1 -f pypy.tar.bz2 \
	&& rm pypy.tar.bz2 \
	\
# explicit path to "pip3" to ensure distribution-provided "pip3" cannot interfere
	&& if [ ! -e /usr/local/bin/pip3 ]; then : \
		&& wget -O /tmp/get-pip.py 'https://bootstrap.pypa.io/get-pip.py' \
		&& pypy3 /tmp/get-pip.py "pip==$PYTHON_PIP_VERSION" \
		&& rm /tmp/get-pip.py \
	; fi \
# we use "--force-reinstall" for the case where the version of pip we're trying to install is the same as the version bundled with Python
# ("Requirement already up-to-date: pip==8.1.2 in /usr/local/lib/python3.6/site-packages")
# https://github.com/docker-library/python/pull/143#issuecomment-241032683
	&& pip3 install --no-cache-dir --upgrade --force-reinstall "pip==$PYTHON_PIP_VERSION" \
# then we use "pip list" to ensure we don't have more than one pip version installed
# https://github.com/docker-library/python/pull/100
	&& [ "$(pip list |tac|tac| awk -F '[ ()]+' '$1 == "pip" { print $2; exit }')" = "$PYTHON_PIP_VERSION" ] \
	\
	&& rm -rf ~/.cache

CMD ["pypy3"]
