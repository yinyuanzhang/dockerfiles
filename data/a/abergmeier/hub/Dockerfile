FROM golang:1.13.4-buster AS build-env

COPY . /src

WORKDIR /src

ENV CGO_ENABLED=0

RUN /src/script/build -o /tmp/hub


FROM alpine/git:1.0.7

COPY --from=build-env /tmp/hub /usr/local/bin/hub

COPY build/package/uid_entrypoint /usr/local/bin/uid_entrypoint

RUN chmod g+rx /usr/local/bin/hub /usr/local/bin/uid_entrypoint

# Arbitrary UID support: https://docs.openshift.com/container-platform/3.11/creating_images/guidelines.html
RUN chgrp -R 0 /etc/passwd /usr/local/bin/hub /usr/local/bin/uid_entrypoint && \
    chmod -R g=u /etc/passwd

ENTRYPOINT ["uid_entrypoint", "/usr/local/bin/hub"]

USER 1001
