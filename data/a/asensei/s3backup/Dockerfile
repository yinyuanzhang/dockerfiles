FROM alpine

WORKDIR ~/

RUN \
  mkdir -p ~/.aws && \
  mkdir -p /aws && \
	apk -Uuv add groff less python py-pip && \
	pip install awscli && \
	apk --purge -v del py-pip && \
	rm /var/cache/apk/*

ADD entrypoint.sh /${WORK_DIR}/entrypoint.sh

ENTRYPOINT ${WORK_DIR}/entrypoint.sh
