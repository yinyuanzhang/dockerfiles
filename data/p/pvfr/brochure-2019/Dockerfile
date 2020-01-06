FROM python:3-stretch

LABEL maintainer="jacques@supcik.net"

RUN apt-get update && apt-get install -y \
      git wget curl unzip \
      texlive \
      texlive-latex-extra \
      texlive-xetex \
      texlive-lang-french \
      latexmk \
      fontconfig \
  && python -m pip install --upgrade pip setuptools

COPY fonts/* /usr/local/share/fonts/
RUN fc-cache -fv

COPY app /app
WORKDIR /app
RUN python -m pip install -r requirements.txt
