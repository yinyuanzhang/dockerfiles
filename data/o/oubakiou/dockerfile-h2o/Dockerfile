FROM buildpack-deps

RUN apt-get update && apt-get install -y \
    cmake \
    && rm -rf /var/lib/apt/lists/*

RUN curl -o tarball -SL https://github.com/h2o/h2o/archive/v1.3.1.tar.gz \
    && tar -xzf tarball \
    && rm tarball \
    && cd h2o-1.3.1 \
    && cmake . \
    && make h2o

RUN mkdir -p /h2o-1.3.1/var/public/ \ 
    && chmod -R 777 /h2o-1.3.1/var/ \
    && mkdir /h2o-1.3.1/ssl/ \
    && chmod 700 /h2o-1.3.1/ssl/

COPY h2o.conf /h2o-1.3.1/h2o.conf
COPY h2ossl.conf /h2o-1.3.1/h2ossl.conf
COPY h2o_crt /h2o-1.3.1/ssl/crt
COPY h2o_key /h2o-1.3.1/ssl/key
COPY h2o_start.sh /h2o-1.3.1/h2o_start.sh
RUN chmod +x /h2o-1.3.1/h2o_start.sh

ENTRYPOINT ["/h2o-1.3.1/h2o_start.sh"]
