FROM ubuntu

ENV TZ=Europe/Berlin
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt-get install -y locales && \
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt install -y \
		  texlive-full \
		  latexmk \
		  biber
RUN apt install -y \
          build-essential \
		  python-pip
RUN apt install -y \
          build-essential \
		  pandoc \
		  plantuml \
       && pip install pandoc-plantuml-filter

WORKDIR /pandoc
