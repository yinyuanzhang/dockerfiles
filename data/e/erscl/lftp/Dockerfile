FROM alpine
LABEL maintainer "erscl"


RUN set -x && \
	apk upgrade --update && \
	apk add tzdata bash lftp git && \
	cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
	apk del tzdata && \
	rm -rf /var/cache/apk/*
CMD ["/bin/bash"]
