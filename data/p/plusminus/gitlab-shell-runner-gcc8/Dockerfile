FROM ubuntu:18.10

ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 /usr/bin/dumb-init
RUN chmod +x /usr/bin/dumb-init

RUN apt-get update -yqq && apt-get dist-upgrade -yqq && \
	apt-get install -yq ca-certificates wget apt-transport-https vim nano\
		git \
		build-essential \
		libx11-xcb1 \
		libfontconfig1 \
		libdbus-1-3 \
		xvfb \
		mesa-common-dev \
		libglu1-mesa-dev \
		libtiff5-dev \
		libwrap0-dev \
		libxt-dev \
		libxi-dev \
		libglib2.0-0 \
		g++ \
		cmake \
		qt5-default \
		qtscript5-dev \
		libqt5svg5-dev \
		libqt5xmlpatterns5-dev \
		qttools5-dev \
		qtwebengine5-dev \
		libqt5x11extras5-dev \
		subversion

RUN wget -O /usr/local/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64 &&\
    chmod +x /usr/local/bin/gitlab-runner &&\
    useradd --comment 'GitLab Runner' --create-home gitlab-runner --shell /bin/bash &&\
    gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner &&\
    mkdir -p /etc/gitlab-runner/certs && \
    chmod -R 700 /etc/gitlab-runner 

ADD entrypoint /
RUN chmod +x /entrypoint
VOLUME ["/etc/gitlab-runner", "/home/gitlab-runner"]
ENTRYPOINT ["/usr/bin/dumb-init", "/entrypoint"]
CMD ["run", "--user=gitlab-runner", "--working-directory=/home/gitlab-runner"]
