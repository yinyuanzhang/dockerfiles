FROM codercom/code-server:latest

USER root

RUN apt install -y build-essential

USER coder

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN echo "export PATH=~/.cargo/bin:$PATH" >> ~/.bashrc

ENTRYPOINT ["dumb-init", "code-server"]