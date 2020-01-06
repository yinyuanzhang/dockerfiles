FROM base/archlinux:latest
ARG parallel=4

USER root
RUN useradd -m build

RUN pacman --noconfirm -Syyu pacman-contrib emscripten cmake binutils make gcc fakeroot
RUN paccache -vrk0

USER build
RUN curl https://aur.archlinux.org/cgit/aur.git/snapshot/binaryen.tar.gz | tar xvz -C /home/build

WORKDIR /home/build/binaryen
ENV MAKEFLAGS -j$parallel
RUN makepkg

USER root
RUN pacman --noconfirm -Rns pacman-contrib fakeroot
RUN pacman --noconfirm -U binaryen-*.pkg.tar.xz

USER build
WORKDIR /home/build
RUN rm -r binaryen

COPY hello.cpp .
RUN source /etc/profile && emcc -v
RUN source /etc/profile && em++ -std=c++14 -o hello.js hello.cpp -s BINARYEN=1 -s DISABLE_EXCEPTION_CATCHING=0 -Os
RUN node hello.js

