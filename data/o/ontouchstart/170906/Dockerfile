FROM storm:1.1.0

# http://streamparse.readthedocs.io/en/stable/quickstart.html
# https://github.com/juxt/docker/blob/master/alpine-clojure/Dockerfile
ENV LEIN_ROOT 1

RUN apk add --update wget ca-certificates bash && \
    wget -q "https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein" \
         -O /usr/local/bin/lein && \
    chmod 0755 /usr/local/bin/lein && \
    lein && \
    apk del wget ca-certificates && \
    rm -rf /tmp/* /var/cache/apk/*

RUN apk add --update libffi-dev openssl-dev alpine-sdk python-dev py-pip 
RUN pip install streamparse
RUN pip show streamparse
RUN lein version
RUN sparse --version
RUN sparse quickstart wordcount
WORKDIR wordcount
