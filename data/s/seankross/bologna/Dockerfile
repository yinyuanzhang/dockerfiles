FROM rocker/verse:latest

RUN apt-get install xdg-utils --fix-missing

RUN apt-get install -y build-essential checkinstall \
	&& apt-get install -y imagemagick

RUN apt-get update \
  && apt-get install -y \
       libpoppler-cpp-dev \
       ffmpeg \
       libtesseract-dev \
       libleptonica-dev \
       tesseract-ocr-eng \
       libwebp-dev \
       libgdal-dev \
  && install2.r --error --deps TRUE \
       magick googledrive tuber pdftools \
  && installGithub.r --deps TRUE \
       muschellij2/ari muschellij2/didactr
