FROM base/archlinux
LABEL name="archrust"
MAINTAINER adjivas <adjivas@student.42.fr>
RUN pacman -Syy ;
RUN pacman -S --noconfirm gcc ;
RUN curl -sSf http://static.rust-lang.org/dist/rustc-nightly-x86_64-unknown-linux-gnu.tar.gz | tar zx -C /tmp && \
    sh /tmp/rustc-nightly-x86_64-unknown-linux-gnu/install.sh ;
RUN curl -sSf https://static.rust-lang.org/cargo-dist/cargo-nightly-x86_64-unknown-linux-gnu.tar.gz | tar zx -C /tmp && \
    sh /tmp/cargo-nightly-x86_64-unknown-linux-gnu/install.sh ;
ENV HOME /root
ENTRYPOINT bash
WORKDIR $HOME
