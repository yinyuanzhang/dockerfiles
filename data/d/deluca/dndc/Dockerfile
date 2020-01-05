FROM clux/diesel-cli:latest as diesel

FROM docker:latest
COPY --from=diesel /bin/diesel /usr/local/bin/diesel
