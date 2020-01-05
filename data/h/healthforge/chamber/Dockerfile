FROM alpine AS fetch
ARG version=2.2.0
ADD https://github.com/segmentio/chamber/releases/download/v$version/chamber-v$version-linux-amd64 /chamber
RUN chmod +x /chamber

FROM scratch
COPY --from=fetch /chamber /chamber/chamber
VOLUME /chamber
ENTRYPOINT ["/chamber/chamber"]
