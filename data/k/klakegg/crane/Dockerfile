FROM alpine:3.9 AS fetcher

#ADD repo.zip /

ADD files /files

RUN sh /files/build.sh


FROM scratch

COPY --from=fetcher /files /
