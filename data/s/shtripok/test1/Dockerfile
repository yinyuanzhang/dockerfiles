# contains qemu-*-static for cross-compilation
FROM multiarch/qemu-user-static as qemu


FROM i386/rust:1.37-buster as rust

COPY --from=qemu /usr/bin/qemu-aarch64-static /usr/bin
RUN /usr/bin/qemu-aarch64-static --version
RUN mount; uname -a

RUN apt-get update && apt-get install -y gcc
WORKDIR /app

COPY a.c .
RUN uname -a
RUN getconf FILESIZEBITS /
RUN gcc -o a a.c
RUN file a
RUN mkdir foo
#RUN cd foo
WORKDIR /app/foo
RUN ../a
