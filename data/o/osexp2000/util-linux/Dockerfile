# https://github.com/auto-build-docker-images/gcc/blob/master/Dockerfile
FROM osexp2000/gcc as builder

USER root

RUN apt-get update && apt-get -y install libncurses-dev libaudit-dev libselinux-dev

# the reason why not download tgz then decompress is that it cause result binaries lost version info
RUN git clone https://github.com/sjitech/util-linux /util-linux-src

WORKDIR /util-linux-src

#
# build a dynamic linked version (require system shared lib to run)
#
RUN git checkout v2.32-fix-bug-of-exec_shell
RUN ./autogen.sh && ./configure --with-audit --with-selinux
RUN grep '^#define HAVE_LIB' config.h
RUN make CFLAGS="-DNDEBUG -v" install-strip DESTDIR=/util-linux-dist

WORKDIR /util-linux-dist

# Important! Preparing lib64/*.so* and /lib/x86_64-linux-gnu/*.so* for dynamic linked program to run.
# Coping util-linux generated lib/*.so to lib/x86_64-linux-gnu/ for some utils such as lsns to run.
# The util-linux generated lib/*.so itself are not used in runtime, just keep it for as a lib.
RUN cp -r /lib/x86_64-linux-gnu lib/ && cp -r /lib64 . && for f in lib/*.so*; do ln -f $f lib/x86_64-linux-gnu/; done

# bash is installed in /usr/local/bin, so I have to link it to bin/
RUN ln -s ../usr/local/bin/bash bin/

###############################################################################

FROM bash

COPY --from=builder /util-linux-dist /

ENTRYPOINT []
CMD ["/bin/bash"]
