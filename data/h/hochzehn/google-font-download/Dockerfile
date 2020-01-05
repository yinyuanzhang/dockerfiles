FROM alpine

RUN apk add --no-cache bash curl ncurses coreutils grep
RUN bash --version

ADD google-font-download /opt/

WORKDIR /dist

ENTRYPOINT ["/opt/google-font-download"]
CMD ["--help"]
