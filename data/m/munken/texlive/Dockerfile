FROM debian:sid
LABEL maintainer "Michael Munch <mm.munk@gmail.com>"
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    TERM=dumb
ARG BUILD_DATE

RUN apt-get update -qq && apt-get upgrade -qq && \
    apt-get install -y --no-install-recommends \
	curl \
	fig2dev \
	fonts-texgyre \
	fontconfig \
	git \
	ghostscript \
	libgetopt-long-descriptive-perl \
	libdigest-perl-md5-perl \
	latexml \
	latexmk \
	pdftk \
	python \
	python-matplotlib \
	python-numpy \
	python-pygments \
	python-pip \
	python-scipy \
	texlive-full \
	unzip \
	wget \
	zip && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://gitlab.com/git-latexdiff/git-latexdiff.git \
    && cp git-latexdiff/git-latexdiff /usr/bin/ \
    && rm -rf git-latexdiff


