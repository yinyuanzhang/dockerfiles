FROM alpine:latest

ENV BOOMFUNC_BASE_VERSION=3.0.0-rc12
ENV BMPROOT=/boomfunc

RUN set -ex \
		&& mkdir -p /lib64 \
		&& ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 \
		\
		&& mkdir -p ${BMPROOT}/app \
		\
		&& apk add --no-cache --virtual .build-deps \
			curl \
		&& curl https://github.com/boomfunc/base/releases/download/${BOOMFUNC_BASE_VERSION}/base-$(uname -s)-$(uname -m) \
			--create-dirs \
			--location \
			--output ${BMPROOT}/base \
		&& chmod +x ${BMPROOT}/base \
		# trigger for check app can be execute on this OS
		&& ${BMPROOT}/base --version \
		\
		&& rm -rf /var/cache/apk/* \
		&& apk del .build-deps

WORKDIR ${BMPROOT}/app

ENTRYPOINT ["../base"]
CMD ["run", "tcp"]
