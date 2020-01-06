FROM base/archlinux
LABEL name="archiron"
MAINTAINER adjivas <adjivas@student.42.fr>
RUN pacman -Syy ;
RUN pacman -S --noconfirm git gcc ;
RUN curl -sSf http://static.rust-lang.org/dist/rustc-nightly-x86_64-unknown-linux-gnu.tar.gz | tar zx -C /tmp && \
    sh /tmp/rustc-nightly-x86_64-unknown-linux-gnu/install.sh ;
RUN curl -sSf https://static.rust-lang.org/cargo-dist/cargo-nightly-x86_64-unknown-linux-gnu.tar.gz | tar zx -C /tmp && \
    sh /tmp/cargo-nightly-x86_64-unknown-linux-gnu/install.sh ;
RUN git clone https://github.com/iron/iron.git $HOME/iron ;
CMD bash -c "echo \"$(hostname --ip-address)localhost\" > /etc/hosts" && \
    bash -c "cargo run --manifest-path $HOME/iron/Cargo.toml --example hello" ;
ENV HOME /root
WORKDIR $HOME/iron
EXPOSE 3000
