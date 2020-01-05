FROM ubuntu:bionic

WORKDIR /var/local

# combine into one run command to reduce image size
RUN apt-get update && apt-get install --assume-yes perl wget libfontconfig1 && \
    wget -qO- "https://yihui.name/gh/tinytex/tools/install-unx.sh" | sh  && \
    apt-get clean
ENV PATH="${PATH}:/root/bin"
RUN tlmgr update --self
RUN tlmgr install xetex
RUN fmtutil-sys --all

# install only the packages you need
# this is the bit which fails for most other methods of installation
RUN tlmgr install xcolor pgf fancyhdr parskip babel-english units lastpage mdwtools comment genmisc epstopdf
# tlmgr install: package epstopdf-base not present in repository.
# epstopdf consists of the main source file epstopdf.dtx and the derived files
##    epstopdf.sty, epstopdf.pdf, epstopdf.ins, epstopdf.drv,
##    epstopdf-base.sty, epstopdf-test1.tex.
RUN mkdir /root/.TinyTeX/texmf-dist/tex/latex/manually-added-because-epstopdf-base-sty-not-found/
COPY epstopdf-base.sty /root/.TinyTeX/texmf-dist/tex/latex/manually-added-because-epstopdf-base-sty-not-found/epstopdf-base.sty

