FROM debian:testing

ARG USERHOME=/home/latex
ARG USERNAME=latex
ARG UID=1000
ARG GID=1000

RUN addgroup \
    --gid "$GID" \
    "$USERNAME" && \
    adduser \
    --home "$USERHOME" \
    --uid "$UID" \
    --gid "$GID" \
    "$USERNAME"

RUN apt-get update && \
    apt-get install -y \
    curl \
    git \
    make \
    pandoc \
    texlive-full \
    inkscape \
    && apt-get --purge remove -y .\*-doc$ && \
    apt-get clean -y

USER "$USERNAME"
