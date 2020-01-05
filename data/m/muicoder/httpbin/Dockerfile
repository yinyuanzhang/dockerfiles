FROM muicoder/python:2

RUN apk add --no-cache wget ca-certificates libffi-dev \
	build-base && \
    wget -qO- github.com/Runscope/httpbin/archive/master.tar.gz | tar -xzf - -C /tmp &&\
    pip install gunicorn \
    	/tmp/httpbin-master && \
    	apk del build-base && \
    find / -name "*.py[co]" -exec rm -f {} ';' && \
    rm -rf /tmp/* /lib/.cache ~/.cache

EXPOSE 80

ENTRYPOINT ["gunicorn"]

CMD ["--workers=4", "--bind=0.0.0.0:80", "httpbin:app"]
