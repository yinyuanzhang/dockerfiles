FROM dockercore/golang-cross

COPY --from=goreleaser/goreleaser /bin/goreleaser /usr/bin/goreleaser

WORKDIR /src

CMD ["goreleaser", "-v"]
