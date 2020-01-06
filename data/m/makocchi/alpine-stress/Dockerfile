# building image
FROM alpine:3.9 as builder
ENV STRESS_VERSION=1.0.4

WORKDIR /tmp
RUN apk add make g++
RUN wget https://people.seas.harvard.edu/~apw/stress/stress-${STRESS_VERSION}.tar.gz
RUN tar zxf stress-${STRESS_VERSION}.tar.gz && cd stress-${STRESS_VERSION} && ./configure && make && make install

# running image
FROM alpine:3.9
COPY --from=builder /usr/local/bin/stress /usr/local/bin/stress
ENTRYPOINT ["/usr/local/bin/stress"]
CMD ["--cpu", "1"]
