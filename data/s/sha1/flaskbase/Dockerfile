FROM sha1/nginx:1.12.2
MAINTAINER developer@detalytics.com

# please also update image tag in circle.yml if you update gevent version

ADD requirements.txt .

RUN set -ex \
	&& buildDeps=' \
		curl \
		gcc-4.9 \
		libbz2-dev \
        libc6-dev \
        libffi-dev \
        g++-4.9 \
        apt-utils \
	' \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \
  && apt-get install -y git --no-install-recommends \
	&& pip install --no-cache-dir Cython \
  && pip install --no-cache-dir -r requirements.txt \
	&& pip uninstall -y Cython \
  && rm -rf /root/.cache/ \
  && rm -rf /var/lib/apt/lists/* \
  && rm requirements.txt \
  && apt-get purge -y --auto-remove $buildDeps
