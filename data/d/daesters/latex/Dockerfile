# idea from aergus/latex

FROM debian:testing

ARG USER_NAME=latex
ARG USER_HOME=/home/latex
ARG USER_ID=1000
ARG USER_GECOS=LaTeX

RUN adduser \
  --home "$USER_HOME" \
  --uid $USER_ID \
  --gecos "$USER_GECOS" \
  --disabled-password \
  "$USER_NAME"

ARG WGET=wget
ARG GIT=git
ARG MAKE=make
ARG PANDOC=pandoc
ARG PYGMENTS=python3-pygments
ARG FIG2DEV=fig2dev
ARG TEXLIVEFULL=texlive-full
ARG TEXLIVEEXTRA=texlive-latex-extra
ARG TEXPUBL=texlive-publishers
ARG LOJAVA=libreoffice-java-common
ARG LOIMPRESS=libreoffice-impress
ARG LOWRITER=libreoffice-writer

RUN apt-get update && apt-get install -y \
  # some auxiliary tools
  "$WGET" \
  "$GIT" \
  "$MAKE" \
  # markup format conversion tool
  "$PANDOC" \
  # XFig utilities
  "$FIG2DEV" \
  # syntax highlighting package
  "$PYGMENTS" \
  # texlive
  "$TEXLIVEFULL" \
  "$TEXLIVEEXTRA" \
  "$TEXPUBL" \
  # libreoffice
  "$LOJAVA" \
  "$LOIMPRESS" \
  "$LOWRITER" \
  && \
  # Removing documentation packages *after* installing them is kind of hacky,
  # but it only adds some overhead while building the image.
  apt-get --purge remove -y .\*-doc$ && \
  # Remove more unnecessary stuff
  apt-get clean -y
