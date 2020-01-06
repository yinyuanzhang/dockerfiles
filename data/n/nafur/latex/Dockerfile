FROM	debian:buster

RUN	apt update && \
	DEBIAN_FRONTEND=noninteractive apt install -y \
		git gnuplot make \
		python3 python3-jinja2 \
		openjdk-11-jre  \
		texlive texlive-fonts-extra texlive-latex-extra texlive-science texlive-luatex texlive-lang-german \
		biber texlive-bibtex-extra && \
	apt clean
