FROM alpine as builder
ARG version=6.4
RUN wget https://github.com/QEF/q-e/archive/qe-$version.zip && unzip qe-$version.zip
RUN apk add --no-cache bash alpine-sdk gfortran
RUN mv /q-e-qe-$version /espresso && cd /espresso  && ./configure && make all
FROM alpine
RUN apk add --no-cache libgcc libgfortran
COPY --from=builder /espresso/bin/*.x /usr/local/bin/
