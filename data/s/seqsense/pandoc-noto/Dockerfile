FROM ubuntu:xenial

RUN apt-get update -qq \
  && apt-get install --no-install-recommends -y \
    etoolbox \
    lmodern \
    make \
    pandoc \
    python-pip \
    texlive-fonts-recommended \
    texlive-latex-recommended \
    texlive-xetex \
    unzip \
    wget \
  && apt-get clean && rm -rf /var/lib/apt/lists

RUN wget -q https://noto-website-2.storage.googleapis.com/pkgs/NotoSerifCJKjp-hinted.zip -O /tmp/NotoSerifCJKjp.zip \
  && mkdir -p $HOME/.fonts/NotoSerifCJKjp \
  && unzip /tmp/NotoSerifCJKjp.zip -d $HOME/.fonts/NotoSerifCJKjp \
  && rm /tmp/NotoSerifCJKjp.zip

RUN wget -q https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip -O /tmp/NotoSansCJKjp.zip \
  && mkdir -p $HOME/.fonts/NotoSansCJKjp \
  && unzip /tmp/NotoSansCJKjp.zip -d $HOME/.fonts/NotoSansCJKjp \
  && rm /tmp/NotoSansCJKjp.zip

WORKDIR /work
