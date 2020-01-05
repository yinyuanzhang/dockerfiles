FROM superherointj/archlinux-base
RUN pacman -Syu --noconfirm git make ncurses zlib ponyc pony-stable llvm llvm-libs llvm7-libs clang
RUN mkdir /app
WORKDIR /app
CMD ponyc