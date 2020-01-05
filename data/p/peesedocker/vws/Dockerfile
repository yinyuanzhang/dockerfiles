FROM busybox as builder

COPY install.sh config.json /tmp/
RUN chmod +x /tmp/install.sh
RUN /tmp/install.sh


FROM scratch

COPY --from=builder /tmp/v2ray /tmp/v2ctl /tmp/config.json /

CMD ["/v2ray"]
