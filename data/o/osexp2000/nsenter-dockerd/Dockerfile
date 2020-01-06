FROM busybox as tmp-image

COPY --from=busybox /bin/busybox /dist/bin/
RUN ln -s busybox /dist/bin/sh
RUN ln -s busybox /dist/bin/cat

# https://github.com/auto-build-docker-images/nsenter/blob/master/Dockerfile
FROM osexp2000/nsenter

COPY --from=tmp-image /dist /

ENTRYPOINT ["/bin/sh", "-c", "/nsenter --target `/bin/cat /proc/1/root/run/docker.pid` --all -- \"$@\"", "--"]
