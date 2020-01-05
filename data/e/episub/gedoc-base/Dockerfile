FROM ubuntu:18.10

RUN apt-get update -y \
	&& apt-get install -y --no-install-recommends \
		curl \
		pandoc \
		texlive-binaries \
		texlive-latex-base \
		texlive-latex-extra \
		texlive-fonts-recommended \
		texlive-fonts-extra \
		texlive-lang-all \
		latexmk \
		lmodern \
		texlive-xetex \
		fonts-arphic-bkai00mp \
		fonts-arphic-gbsn00lp \
		fonts-arphic-bsmi00lp \
		fonts-arphic-gkai00mp \
		fonts-arphic-uming \
		fonts-arphic-ukai \
		fontconfig \
		optipng \
		poppler-utils \
		qpdf \
		imagemagick && fc-cache -fv && apt-get clean

ADD install.sh /install.sh
RUN /install.sh
RUN fc-cache -f
