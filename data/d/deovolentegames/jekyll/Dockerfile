FROM jekyll/jekyll:latest
ENV LFS_VERSION 2.3.4
RUN apk update && apk upgrade && apk --update add \
	gzip python python-dev py-pip ruby ruby-dev wget && pip install awscli && \
	wget https://github.com/github/git-lfs/releases/download/v$LFS_VERSION/git-lfs-linux-amd64-$LFS_VERSION.tar.gz && \
	tar xf git-lfs-linux-amd64-$LFS_VERSION.tar.gz && \
	cd git-lfs-${LFS_VERSION}/ && ./install.sh && cd .. && gem install bundler
