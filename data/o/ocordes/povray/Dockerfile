FROM alpine:3.9

# written by: Oliver Cordes 2019-06-25
# changed by: Oliver Cordes 2019-06-25



RUN apk add --update --no-cache \
    git \
    coreutils \
    build-base \
    autoconf \
    automake \
    bash \
    boost-dev \
    zlib-dev \
    libpng-dev \
    tiff-dev \
    sdl-dev \
    ilmbase-dev \
    openexr-dev 

RUN git clone https://github.com/POV-Ray/povray.git && \
    cd /povray && \
    git checkout release/v3.8.0 && \
    cd /povray/unix && \
    ./prebuild.sh && \
    cd /povray &&  \
    echo "typedef unsigned int uint;" > uint-hack.h 

WORKDIR /povray

RUN ./configure COMPILED_BY="Oliver Cordes ocordes/povray:3.8-alpha" \
      --disable-optimiz \
      CXXFLAGS="-O3 -march=sandybridge -include uint-hack.h -I/usr/include/OpenEXR"
RUN make install && mv /usr/local/bin/povray /usr/local/bin/povray.sandybridge
RUN make clean
RUN ./configure COMPILED_BY="Oliver Cordes ocordes/povray:3.8-alpha" \
      --disable-optimiz \
      CXXFLAGS="-O3 -march=nehalem -include uint-hack.h -I/usr/include/OpenEX$"
RUN make install && mv /usr/local/bin/povray /usr/local/bin/povray.nehalem
RUN make clean
RUN ./configure COMPILED_BY="Oliver Cordes ocordes/povray:3.8-alpha" \
      --disable-optimiz \
      CXXFLAGS="-O3 -march=core2 -include uint-hack.h -I/usr/include/OpenEXR"
RUN make install && mv /usr/local/bin/povray /usr/local/bin/povray.core2
RUN make clean
RUN ./configure COMPILED_BY="Oliver Cordes ocordes/povray:3.8-alpha" \
      --disable-optimiz \
      CXXFLAGS="-O3 -march=k8 -include uint-hack.h -I/usr/include/OpenEXR"
RUN make install && mv /usr/local/bin/povray /usr/local/bin/povray.k8
RUN make clean
RUN ./configure COMPILED_BY="Oliver Cordes ocordes/povray:3.8-alpha" \
      --disable-optimiz \
      CXXFLAGS="-O3 -march=x86-64 -include uint-hack.h -I/usr/include/OpenEXR"
RUN make install && mv /usr/local/bin/povray /usr/local/bin/povray.x86-64

WORKDIR /

RUN cd / && \
    rm -rf /povray && \
    rm -rf /usr/local/share/doc/povray-3.8 && \
    rm -rf /usr/local/share/povray-3.8/scenes


FROM alpine:3.9

COPY --from=0 /usr/local /usr/local
COPY --from=0 /root/.povray /root/.povray

RUN apk add --update --no-cache \
    boost \
    zlib \
    libpng \
    tiff \
    sdl \
    ilmbase \
    openexr && \
    rm -rf /var/cache/apk*

RUN mkdir /source && \
    mkdir /output


WORKDIR /source

COPY povray /usr/local/bin/povray
RUN chmod 755 /usr/local/bin/povray

ENTRYPOINT ["/usr/local/bin/povray"]


