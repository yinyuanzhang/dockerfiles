FROM debian:stretch-slim AS build-env
LABEL Image to compile lepton binary (revision 1.2.1-21-g3d339f1)

# compile lepton (by Dropbox)
# output file is /root/lepton/lepton
RUN apt-get update && apt-get install -y git autoconf build-essential python
RUN git clone https://github.com/dropbox/lepton.git /root/lepton
RUN cd /root/lepton; \
    git checkout --quiet 3d339f168b651608b188fbaa35ca8422ee20d906 && \
    ./autogen.sh && \
    ./configure && \
    make liblocalzlib.a && \
    make && \
    make check


FROM debian:stretch-slim
LABEL io.k8s.display-name="lepton" \
      io.k8s.description="lepton (by Dropbox)"

COPY --from=build-env /root/lepton/lepton /usr/local/bin/lepton

ENTRYPOINT ["/bin/sh"]
