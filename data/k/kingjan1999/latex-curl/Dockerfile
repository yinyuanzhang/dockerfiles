FROM tianon/latex

RUN apt-get update && apt-get install -y \
		curl python python-pygments wget \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /root

RUN wget https://www.tug.org/fonts/getnonfreefonts/install-getnonfreefonts
RUN texlua /root/install-getnonfreefonts
RUN getnonfreefonts --sys --all
