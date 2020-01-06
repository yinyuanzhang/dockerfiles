FROM fedora
ADD https://github.com/parasti/mingw-list-deps/raw/master/mingw-list-deps /usr/local/bin/mingw-list-deps
RUN chmod a+rx /usr/local/bin/mingw-list-deps
RUN dnf --assumeyes install \
    make \
    findutils \
    mingw32-gcc
RUN dnf --assumeyes install \
    mingw32-SDL2 \
    mingw32-libpng \
    mingw32-libjpeg-turbo \
    mingw32-freetype \
    mingw32-libvorbis \
    mingw32-gettext
RUN URL="https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.15.tar.gz"; \
    ARCHIVE="SDL2_ttf-2.0.15.tar.gz"; \
    DIR="SDL2_ttf-2.0.15"; \
    cd /usr/local/src && \
    curl -o "$ARCHIVE" "$URL" && \
    tar -x -z -f "$ARCHIVE" && \
    cd "$DIR" && \
    mingw32-configure && \
    mingw32-make -j2 install-strip && \
    cd .. && \
    rm -rf "$DIR" "$ARCHIVE"