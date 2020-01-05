FROM ubuntu:19.10

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
	&& apt-get install -y dia git inkscape libreoffice make python3-pygments python3-seaborn python3-toml sqlite3 texlive-full unoconv \
	&& apt-get purge -y '.*-doc$' \
	&& apt-get clean -y
