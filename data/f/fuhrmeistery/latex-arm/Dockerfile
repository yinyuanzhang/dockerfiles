FROM debian:stretch
LABEL maintainer="yannikfuhrmeister@web.de"
RUN     apt-get update && \
        apt-get install -y file texlive-full \
                python3-pygments \
                git \
                make \
                pandoc \
                fig2dev \
                wget && \
        apt-get --purge remove -y .\*-doc$ && \
        apt-get clean -y \
