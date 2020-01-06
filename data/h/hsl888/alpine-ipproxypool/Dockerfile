FROM alpine:edge

RUN apk add --update python2 python2-dev py2-pip py2-lxml sqlite gcc musl-dev linux-headers && \
	pip install --upgrade pip && \
	pip install requests chardet gevent && \
	pip install web.py SQLAlchemy psutil redis && \
	apk del gcc python2-dev && \
	rm -fr /var/cache

COPY ./IPProxyPool /opt/IPProxyPool
WORKDIR /opt/IPProxyPool

EXPOSE 8888

CMD ["python", "IPProxy.py"]