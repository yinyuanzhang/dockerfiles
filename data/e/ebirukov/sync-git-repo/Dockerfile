FROM gliderlabs/alpine:3.3
MAINTAINER Eugeny Birukov <e.birukov@corpwebgames.com>

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

ADD scripts/sync-runner.sh /sync-runner.sh
ADD scripts/sync-repo.sh /sync-repo.sh

#ENTRYPOINT ["sync-runner.sh"]
CMD ["./sync-runner.sh"]

