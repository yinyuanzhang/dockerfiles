FROM composer:1.8.4

RUN apk add --no-cache --update gcc g++ nodejs autoconf yarn libarchive-tools libtool automake
RUN wget -P / https://bitbucket.org/bitbucketpipelines/bitbucket-pipes-toolkit-bash/raw/0.4.0/common.sh

RUN yarn global add gulp gulp-cli grunt webpack

COPY pipe /

ENTRYPOINT ["/pipe.sh"]