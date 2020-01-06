FROM debian:stretch-slim
MAINTAINER Josh Gelman <gelmo@outlook.com>

ENV DEBIAN_FRONTEND=noninteractive

RUN useradd eggdrop

ENV EGGDROP_SHA256 74212f33f8c44be68ea6bd8c41f636620771328f9e8dc1549e218e637efbc9bc
ENV EGGDROP_COMMIT 83d237a1d82a74dd36c86bacd4b833131143c062

RUN apt-get update
RUN apt-get install -y --no-install-recommends wget tcl-dev mysqltcl ca-certificates libreadline7 libreadline-dev libterm-readline-gnu-perl build-essential gosu
RUN wget "https://github.com/eggheads/eggdrop/archive/$EGGDROP_COMMIT.tar.gz" -O develop.tar.gz
RUN echo "$EGGDROP_SHA256  develop.tar.gz" | sha256sum -c -
RUN tar -zxvf develop.tar.gz
RUN rm develop.tar.gz
RUN cd eggdrop-$EGGDROP_COMMIT
RUN /bin/bash -c 'chmod +x /eggdrop-$EGGDROP_COMMIT/configure'
RUN /bin/bash -c '/eggdrop-$EGGDROP_COMMIT/configure'
RUN make config
RUN make
RUN make install DEST=/home/eggdrop/eggdrop
RUN rm -rf eggdrop-$EGGDROP_COMMIT
RUN mkdir /home/eggdrop/eggdrop/data
RUN chown -R eggdrop /home/eggdrop/eggdrop

ENV LISTEN="3333"
ENV USERFILE="eggdrop.user"
ENV CHANFILE="eggdrop.chan"

WORKDIR /home/eggdrop/eggdrop
EXPOSE 3333
COPY entrypoint.sh /home/eggdrop/eggdrop
COPY docker.tcl /home/eggdrop/eggdrop/scripts/

ENTRYPOINT ["/home/eggdrop/eggdrop/entrypoint.sh"]
CMD ["eggdrop.conf"]
