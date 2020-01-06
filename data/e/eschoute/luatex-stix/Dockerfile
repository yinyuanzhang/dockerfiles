FROM debian:testing-slim
RUN apt-get update

# Install lualatex and packages
RUN apt-get install -y texlive-luatex \
					texlive-latex-extra \
					texlive-bibtex-extra \
					texlive-science \
					biber \
					latexmk \
					python-pygments \
					wget

# Install stix fonts 2
RUN wget -q https://github.com/stipub/stixfonts/archive/v2.0.1.tar.gz \
	&& tar -xzf v2.0.1.tar.gz \
	&& cp stixfonts-2.0.1/OTF/*.otf /usr/local/share/fonts/ \
	&& fc-cache \
	&& rm v2.0.1.tar.gz && rm -r stixfonts-2.0.1
# Update otf cache
RUN luaotfload-tool --update
