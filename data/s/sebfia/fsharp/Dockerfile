FROM ubuntu:xenial
MAINTAINER Sebastian Fialka <sebastian.fialka@sebfia.net>

ENV MONO_VERSION 4.2.3.4
ENV FSHARP_VERSION 4.0.1.8
ENV FSHARP_PREFIX /usr
ENV FSHARP_GACDIR /usr/lib/mono/gac
ENV FSHARP_BASENAME fsharp-$FSHARP_VERSION
ENV FSHARP_ARCHIVE $FSHARP_VERSION.tar.gz
ENV FSHARP_ARCHIVE_URL https://github.com/fsharp/fsharp/archive/$FSHARP_ARCHIVE
ENV MONO_THREADS_PER_CPU 50

RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb http://download.mono-project.com/repo/debian wheezy/snapshots/$MONO_VERSION main" > /etc/apt/sources.list.d/mono-xamarin.list && \
    apt-get -y update && \
    apt-get -y --no-install-recommends install binutils mono-devel ca-certificates-mono nuget libtool make automake wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /tmp/src && \
    cd /tmp/src && \
    wget $FSHARP_ARCHIVE_URL && \
    tar xf $FSHARP_ARCHIVE && \
    cd $FSHARP_BASENAME && \
    ./autogen.sh --prefix=$FSHARP_PREFIX --with-gacdir=$FSHARP_GACDIR && \
    make && \
    make install && \
    cd ~ && \
    rm -rf /tmp/src

CMD ["fsharpi"]
