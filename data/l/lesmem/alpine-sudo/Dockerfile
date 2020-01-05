FROM alpine
RUN apk --no-cache add sudo && \
	adduser -D user && \
	echo "ALL ALL = (ALL) NOPASSWD: ALL" > /etc/sudoers
COPY ./entrypoint.sh /entrypoint
ENTRYPOINT ["/entrypoint"]
