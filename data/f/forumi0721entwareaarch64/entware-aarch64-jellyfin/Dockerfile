ARG BUILD_ARCH=x64

FROM forumi0721alpine${BUILD_ARCH}/alpine-${BUILD_ARCH}-dotnet-2-sdk:latest as builder

LABEL maintainer="forumi0721@gmail.com"

ENV DOTNET_RUNTIME=linux-arm64

COPY build/. /usr/local/

#RUN ["docker-build-start"]

RUN ["docker-build"]

#RUN ["docker-build-end"]



FROM forumi0721/entware-aarch64-base:latest

LABEL maintainer="forumi0721@gmail.com"

COPY --from=builder /opt/jellyfin /opt/jellyfin

COPY local/. /usr/local/

RUN ["docker-build-start"]

RUN ["docker-init"]

RUN ["docker-build-end"]

ENTRYPOINT ["docker-run"]

EXPOSE 8096/tcp 8920/tcp

VOLUME /conf.d

