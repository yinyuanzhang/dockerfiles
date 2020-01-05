FROM alpine:edge

RUN apk update && \
	mkdir -p /app/conf && \
	mkdir -p /app/data && \
	apk add --no-cache --update aria2
	
ADD run.sh aria2.conf /app/

RUN chmod +x /app/run.sh

WORKDIR /app

VOLUME ["/app/data", "/app/conf"]

EXPOSE 6800

CMD ["/app/run.sh"]

