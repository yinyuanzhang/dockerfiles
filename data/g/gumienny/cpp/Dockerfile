FROM gumienny/cpp:base

RUN set -ex; \
	echo "deb http://deb.debian.org/debian stretch-backports main" > /etc/apt/sources.list.d/stretch-backports.list; \
	apt-get update; \
	apt-get -t stretch-backports install -y --no-install-recommends \
		clang-6.0 \
	; \
	apt-get clean; \
	rm -r /var/lib/apt/lists/* /etc/apt/sources.list.d/stretch-backports.list;
