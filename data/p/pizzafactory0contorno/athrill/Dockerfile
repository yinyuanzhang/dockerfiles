FROM alpine as builder

ARG TARGET_ARCH

RUN apk add --no-cache git gcc make libc-dev


RUN git clone https://github.com/tmori/athrill.git
WORKDIR athrill/trunk/src/build/target/linux_${TARGET_ARCH}/
RUN make

FROM pizzafactory0contorno/piatto:alpine
USER root
RUN mkdir -p /opt/bin/ /opt/src/athrill /opt/src/athrill-target/
COPY --from=builder /athrill/bin/linux/athrill2 /opt/bin/
COPY --from=builder /athrill/trunk/ /opt/src/athrill/
USER user
ENV PATH $PATH:/opt/bin/
