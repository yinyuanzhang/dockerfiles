FROM alpine

RUN apk update \
	&& apk add curl git util-linux bash openssh-client \
	&& curl -OL https://raw.github.com/nvie/gitflow/develop/contrib/gitflow-installer.sh \
	&& chmod +x gitflow-installer.sh \
	&& INSTALL_PREFIX=~/bin ./gitflow-installer.sh \
	&& sh gitflow-installer.sh \
	&& apk del curl \
	&& rm -rf /var/cache/apk/*

WORKDIR /opt/git-repo

ENTRYPOINT ["/usr/bin/git"]
