FROM alpine:latest
MAINTAINER bulzipke <bulzipke@naver.com>

ENV UID=1000
ENV GID=1000
ENV XDG_CONFIG_HOME="/"
ENV XDG_DATA_HOME="/"
ENV XDG_CONFIG_HOME="/"
ENV XDG_CACHE_HOME="/"

RUN apk add sqlite-dev curl-dev gmp-dev fuse ca-certificates && \
  apk add --virtual build-dependencies opam make m4 fuse-dev perl musl-dev ocaml-compiler-libs ocaml-ocamldoc wget curl unzip && \
  S6_VERSION=$(curl -sX GET "https://api.github.com/repos/just-containers/s6-overlay/releases/latest" | awk '/tag_name/{print $4;exit}' FS='[""]') && \
  curl -o s6-overlay.tar.gz -L "https://github.com/just-containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz" && \
  tar xfz s6-overlay.tar.gz -C / && \
  rm -rf s6-overlay.tar.gz && \
  sed -i 's/#user_allow_other/user_allow_other/' /etc/fuse.conf && \
  addgroup -S abc -g 1000 && adduser -S abc -G abc -u 1000

# RUN addgroup -S ocaml -g 1000 && adduser -S ocaml -G ocaml -u 1000 -D
# RUN useradd -d /home/ocaml -ms /bin/sh -g root -G sudo -p ocaml ocaml
# RUN mkdir -p /home/ocaml/bin
# RUN PATH=$PATH:/home/ocaml/bin

# WORKDIR /home/ocaml
ADD rootfs /

# RUN chown -R ocaml /home/ocaml
# RUN chmod +x /home/ocaml/*

# USER ocaml
ENTRYPOINT ["/init"]
