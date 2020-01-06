FROM debian:buster

#ADD https://github.com/varnish/varnish-modules/archive/0.15.0.tar.gz /tmp/varnish-modules.tar.gz
#
#RUN apt-get update && apt-get install --yes build-essential varnish-dev 
#RUN apt-get install autotools
#
#RUN cd /tmp && tar zxf varnish-modules.tar.gz && cd varnish-modules* && ls && \
#    ./bootstrap && ./configure && make && make install

RUN apt-get update && apt-get install --yes varnish && apt-get install --yes varnish-modules

ADD teastore.vcl /etc/varnish/default.vcl

CMD ["varnishd", "-F", "-f", "/etc/varnish/default.vcl", "-s", "malloc,256M", "-a", "webui=0.0.0.0:1111", "-a", "registry=0.0.0.0:2222", "-a", "image=0.0.0.0:3333", "-a", "auth=0.0.0.0:4444", "-a", "persistence=0.0.0.0:5555", "-a", "recommender=0.0.0.0:6666"]
