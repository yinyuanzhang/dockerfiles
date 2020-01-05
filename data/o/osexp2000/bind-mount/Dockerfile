# osexp2000/util-linux-static: https://github.com/auto-build-docker-images/util-linux-static/blob/master/Dockerfile
FROM bash as tmp-image

COPY --from=osexp2000/util-linux-static /bin/mount /dist/bin/
COPY ./scripts /dist/usr/local/bin/

# bash is installed in /usr/local/bin, so I have to link it to bin/
RUN ln -s ../usr/local/bin/bash /dist/bin/

FROM bash

COPY --from=tmp-image /dist /

ENTRYPOINT ["bind-mount"]
