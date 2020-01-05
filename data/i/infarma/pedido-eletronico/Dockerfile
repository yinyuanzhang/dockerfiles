FROM ubuntu:16.04

MAINTAINER Equipe P&D "contato@infarma.com.br"

# Install software
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git wget tar nano vim tzdata

# Install goLang
RUN wget https://dl.google.com/go/go1.11.4.linux-amd64.tar.gz
RUN tar -xvf go1.11.4.linux-amd64.tar.gz
RUN mv go /usr/local
RUN rm -rf go1.11.4.linux-amd64.tar.gz

# GOROOT & GOPATH & PATH
ENV GOROOT="/usr/local/go"
ENV PATH="$GOPATH/bin:$GOROOT/bin:$PATH"
ENV MODE="prod"
ENV DATABASE_IP=""
ENV DATABASE_NAME=""
ENV DATABASE_INSTANCE=""
ENV DATABASE_PORT=""
ENV DATABASE_USER=""
ENV DATABASE_PASSWORD=""

# Make ssh dir
RUN mkdir /root/.ssh/
RUN mkdir /root/layouts

# Copy to project
COPY static/frontend/static /root/pedido-eletronico
# Copy to ImportPath
COPY src /root/src

# Ports
EXPOSE 9000

# Run app in production mode
ENTRYPOINT ./root/pedido-eletronico -importPath pedido-eletronico -srcPath "/root/src" -runMode $MODE