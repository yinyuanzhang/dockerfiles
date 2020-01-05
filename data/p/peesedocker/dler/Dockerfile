FROM busybox as builder

COPY download.sh url.txt /tmp/
RUN chmod +x /tmp/download.sh
RUN /tmp/download.sh


FROM scratch

COPY --from=builder /tmp/file.tar.gz /
