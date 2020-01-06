FROM ubuntu:18.04

ENV OWASP_CRS_VERSION=v3.2/dev

LABEL maintainer="Daniel Pryor <http://github.com/pryorda/>"

COPY --from=pryorda/docker-waf-base:latest /usr/src/modsecurity/ /usr/src/modsecurity/
COPY --from=pryorda/docker-waf-base:latest /usr/local/nginx/ /usr/local/nginx/

RUN adduser --disabled-password --system --home /var/cache/nginx --shell /sbin/nologin --group nginx && \ 
        ln -s /usr/local/nginx/sbin/nginx /bin/nginx && \
	cp /usr/src/modsecurity/unicode.mapping /usr/local/nginx/conf/ && \
	mkdir -p /opt/modsecurity/var/audit/ && \
	apt-get update && \
	apt-get install -y git libyajl-dev libpcre3 libpcre3-dev libssl-dev libtool autoconf apache2-dev libxml2-dev libcurl4-openssl-dev && \
	git clone -b ${OWASP_CRS_VERSION} https://github.com/SpiderLabs/owasp-modsecurity-crs.git /usr/src/owasp-modsecurity-crs && \
	cp -R /usr/src/owasp-modsecurity-crs/rules/ /usr/local/nginx/conf/  && \
	mv /usr/local/nginx/conf/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf.example  /usr/local/nginx/conf/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf && \
	mv /usr/local/nginx/conf/rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf.example  /usr/local/nginx/conf/rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf && \
        mkdir -p /var/log/nginx/ && \
	apt-get purge -y git && \
	apt-get autoremove -y && \
        rm -rf /var/lib/apt/lists/*

COPY nginx.conf /usr/local/nginx/conf/nginx.conf
COPY modsec_includes.conf /usr/local/nginx/conf/modsec_includes.conf
COPY modsecurity.conf /usr/local/nginx/conf/modsecurity.conf
COPY crs-setup.conf /usr/local/nginx/conf/rules/crs-setup.conf

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log 

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]

