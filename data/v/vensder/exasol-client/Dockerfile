FROM openjdk:8-jre-alpine

RUN apk add --update curl perl && \
	rm -rf /var/cache/apk/* && \
	curl -L https://www.exasol.com/support/secure/attachment/56167/EXAplus-6.0.5.tar.gz | tar zxv --exclude='doc' && \
	mkdir -p /app && \
	mv EXAplus-6.0.5/exaplus EXAplus-6.0.5/*.jar app && \
	rm -rf EXAplus-6.0.5/

WORKDIR /app
ENTRYPOINT ["/app/exaplus"]
CMD ["--help"]
