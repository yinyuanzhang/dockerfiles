FROM ubuntu
ENV HOME=/home/convox
ENV EDITOR=nano
ENV CONVOX=/usr/bin/convox
WORKDIR ${HOME}
RUN apt-get update && \
    apt-get install -y zsh nano vim curl git && \
    mkdir -p .local/bin && \
    curl -L https://convox.com/cli/linux/convox -o ${CONVOX} && \
    chmod +x ${CONVOX}
COPY .zshrc .
CMD ["zsh"]
