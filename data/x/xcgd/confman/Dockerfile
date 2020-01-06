FROM alpine
RUN apk add --no-cache --update mercurial git openssh-client py-setuptools && hg clone https://bitbucket.org/auc/confman /usr/src/confman && rm -rf /usr/src/confman/.hg && mkdir -m 0700 $HOME/.ssh
ADD hgrc /etc/mercurial/
