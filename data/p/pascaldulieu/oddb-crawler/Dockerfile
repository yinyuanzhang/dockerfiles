FROM golang:alpine
ENV CONNECTIONS=4 \
	DIAL_TIMEOUT=10s \
	JOB_BUFFER=5000 \
	RESUME=72h0m0s \
	RETRIES=5 \
	TASKS=100 \
	TIMEOUT=30s \
	USER_AGENT="Mozilla/5.0 (X11; od-database-crawler) Gecko/20100101 Firefox/52.0" \
	COOLDOWN=30s \
	RECHECK=1s \
	SERVER_TIMEOUT=1m0s \
	TOKEN= \
	UPLOAD_CHUNK="1 MB" \
	UPLOAD_RETRIES=10 \
	UPLOAD_RETRY_INTERVAL=30s \
	URL=https://od-db.the-eye.eu/api
ADD start.sh /start.sh
RUN apk add git bash && \
	go get github.com/terorie/od-database-crawler && \
	rm -r /go/src && \
	chmod +x /start.sh
VOLUME [ "/go" ]
ENTRYPOINT [ "/start.sh" ]