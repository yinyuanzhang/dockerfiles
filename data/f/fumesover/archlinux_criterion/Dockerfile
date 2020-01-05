FROM archlinux/base

RUN pacman --noconfirm --noprogressbar -Syyu; \
    pacman --noconfirm --noprogressbar --needed -S make gcc autoconf automake \
            cmake ctags gcc-libs gdb glibc git cmake base-devel gettext \
            nanomsg python-cram

COPY ./install_criterion.sh /usr/bin/install_criterion
COPY ./entrypoint.sh /usr/bin/entrypoint

RUN install_criterion

WORKDIR /code/

ENTRYPOINT [ "entrypoint" ]
