FROM mhart/alpine-node:latest
LABEL maintainer="jussi.raunio@haamu.tech"

# Update environment PATHs to include mapnik.
ENV PATH="/opt/mapnik/bin:${PATH}"
ENV LD_LIBRARY_PATH=/opt/mapnik/lib

# Install build & run environment, build mapnik and node-mapnik
# to /opt and then clean up everything.
RUN apk add --no-cache git \
                       build-base \
                       g++ \
                       bash \
                       python \
                       boost \
                       boost-program_options \
                       boost-dev \
                       freetype \
                       freetype-dev \
                       icu-libs \
                       icu-dev \
                       libjpeg \
                       libjpeg-turbo-dev \
                       libpng \
                       libpng-dev \
                       zlib \
                       zlib-dev \
                       libxml2 \
                       libxml2-dev \
                       harfbuzz \
                       harfbuzz-dev \
                       cairo \
                       cairo-dev \
                       libpq \
                       postgresql-dev &&\
    # Clone mapnik and node-mapnik sources.
    git clone --progress --recurse-submodules https://github.com/mapnik/mapnik.git /usr/src/mapnik &&\
    git clone --progress https://github.com/mapnik/node-mapnik.git /usr/src/node-mapnik &&\
    # Build a selected version of mapnik.
    cd /usr/src/mapnik &&\
    git reset --hard bfb071233eefe96607079d3b41c127a3e3c41b79 &&\
    git submodule update &&\
    ./configure PREFIX=/opt/mapnik &&\
    make -j4 &&\
    make install &&\
    # Build a selected version of node-mapnik. Also, hackily fix a bug in postinstall.sh.
    cd /usr/src/node-mapnik &&\
    git reset --hard 13f865d762ac8e61521228f50e60bfedc873d34c &&\
    sed -i -e "s/var path = require('path');/\"; echo '' > \$\{MODULE_PATH\}\/mapnik_settings.js; echo \"/"\
        -e 's/" > ${MODULE_PATH}\/mapnik_settings\.js/" >> ${MODULE_PATH}\/mapnik_settings.js/' scripts/postinstall.sh &&\
    make release_base &&\
    mkdir -p /opt/node-mapnik/node_modules/.bin &&\
    cp -a bin lib tools package.json package-lock.json README.md /opt/node-mapnik/ &&\
    cp -a node_modules/.bin/node-pre-gyp /opt/node-mapnik/node_modules/.bin/ &&\
    cp -a node_modules/node-pre-gyp /opt/node-mapnik/node_modules &&\
    # Remove build time packages and clean up the source files.
    apk del git \
            build-base \
            g++ \
            bash \
            python \
            boost-dev \
            freetype-dev \
            icu-dev \
            libjpeg-turbo-dev \
            libpng-dev \
            zlib-dev \
            libxml2-dev \
            harfbuzz-dev \
            cairo-dev \
            postgresql-dev &&\
    rm -rf /usr/src /opt/mapnik/include

# This is the directory where distribution files are located.
WORKDIR /opt

# Start shell by default.
CMD ["/bin/ash"]
