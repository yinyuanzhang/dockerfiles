FROM alpine:3.10.3 as builder
RUN wget -O - 'https://github.com/ktr0731/evans/releases/download/0.8.4/evans_linux_amd64.tar.gz' | tar zxvf -
FROM scratch
COPY --from=builder /evans /evans
ENTRYPOINT ["/evans"]