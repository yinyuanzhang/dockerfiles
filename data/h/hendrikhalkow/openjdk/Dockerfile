FROM centos:7 AS build

# Separate layer to avoid re-downloading
RUN curl -Ls "https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11%2B28/OpenJDK11-jre_x64_linux_hotspot_11_28.tar.gz" | tar zx

RUN \
  mv "/jdk-"* /openjdk && \
  pushd /openjdk && \
  mkdir -m 777 app && \
  mkdir -m 777 tmp && \
  pushd bin && \
  find . ! -name 'java' -type f -exec rm -f {} + && \
  popd && \
  rm -rf \
    conf/security/{README.txt,limited} \
    include \
    legal \
    && \
  true

FROM scratch

COPY --from=build \
  /lib64/libz.so.1 \
  /lib64/libpthread.so.0 \
  /lib64/libdl.so.2 \
  /lib64/libc.so.6 \
  /lib64/ld-linux-x86-64.so.2 \
  /lib64/libm.so.6 \
  /lib64/librt.so.1 \
  /lib64/

COPY --from=build /openjdk/ /
ENTRYPOINT [ "/bin/java" ]
CMD [ "-version" ]
USER 1001
