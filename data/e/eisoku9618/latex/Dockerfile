FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt update \
        && apt install -y --no-install-recommends \
        # Essential programs and files
        texlive-latex-base \
        # LaTeX additional packages
        texlive-latex-extra \
        # Plain (La)TeX packages
        texlive-plain-generic \
        # latexmk
        latexmk \
        && rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
