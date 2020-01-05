FROM resin/armv7hf-debian-qemu

CMD ["cross-build-start"]

FROM microsoft/dotnet:2-sdk as builder
WORKDIR /repo
COPY . .
ARG CONFIGURATION=RELEASE
RUN export DOTNET_CLI_TELEMETRY_OPTOUT=1 \
 && dotnet clean \
 && dotnet build --configuration ${CONFIGURATION} $(pwd)/MediaBrowser.sln \
 && dotnet publish --configuration ${CONFIGURATION} $(pwd)/MediaBrowser.sln --output /jellyfin

FROM microsoft/dotnet:2-runtime
COPY --from=builder /jellyfin /jellyfin
RUN apt update \
 && apt install -y ffmpeg gosu
EXPOSE 8096
VOLUME /config /media
ENV PUID=1000 PGID=1000
ENTRYPOINT chown $PUID:$PGID /config /media \
 && gosu $PUID:$PGID dotnet /jellyfin/jellyfin.dll -programdata /config

CMD ["cross-build-end"]
