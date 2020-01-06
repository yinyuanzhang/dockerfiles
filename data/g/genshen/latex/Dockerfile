FROM debian:buster-slim

# more package: python3-pygments fig2dev pandoc-citeproc 
RUN apt-get update  \
    && apt-get install --no-install-recommends -y biber latexmk make texlive-full pandoc \
    && apt-get --purge remove -y .\*-doc$  \
    && apt-get clean -y

RUN adduser --disabled-password --gecos "" latex

USER latex
WORKDIR /home/latex
