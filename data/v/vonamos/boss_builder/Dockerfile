FROM vonamos/boss_base:latest

ENV HOME=/home/user
RUN mkdir -p $HOME/project
RUN mkdir -p $HOME/.cargo/registry
COPY conf/cargo-config $HOME/.cargo/config
COPY bin $HOME/bin
COPY openssl /$HOME/openssl
ENV PATH=$HOME/bin:$PATH
ENTRYPOINT ["entrypoint.sh"]
CMD [""]
