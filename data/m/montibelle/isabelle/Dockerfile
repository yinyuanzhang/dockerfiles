FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    curl \
    less \
    libgomp1 \
    libfontconfig1 \
    rlwrap \
    unzip \
    libwww-perl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# add isabelle user
RUN useradd -m isabelle && (echo isabelle:isabelle | chpasswd)
USER isabelle


# install Isabelle
WORKDIR /home/isabelle
RUN curl --fail https://isabelle.in.tum.de/dist/Isabelle2019_linux.tar.gz > Isabelle.tar.gz && \
    tar xzf Isabelle.tar.gz && \
    mv Isabelle2019 Isabelle && \
    rm -f Isabelle/doc/*.pdf && \
    sed -i -e 's@ISABELLE_HOME_USER=.*@ISABELLE_HOME_USER="$USER_HOME/.isabelle"@g' Isabelle/etc/settings
ENV PATH="/home/isabelle/Isabelle/bin:${PATH}"


# set up the logic 
ARG DEF_LOGIC="HOLCF"
RUN sed -i -e 's@ISABELLE_LOGIC=.*@'"ISABELLE_LOGIC=$DEF_LOGIC"'@g' Isabelle/etc/settings && \
    isabelle build -o system_heaps -b -j 4 -v HOLCF
