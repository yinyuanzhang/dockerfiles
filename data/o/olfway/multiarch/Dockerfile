ARG BUSYBOX_IMAGE=busybox:latest
FROM ${BUSYBOX_IMAGE}

COPY --from=olfway/qemu-user-static /qemu-arm-static /usr/bin/
COPY --from=olfway/qemu-user-static /qemu-aarch64-static /usr/bin/

RUN uname -a

CMD [ "/bin/sh" ]
