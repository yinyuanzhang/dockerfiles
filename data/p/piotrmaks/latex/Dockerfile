FROM debian:testing-slim

ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 /usr/bin/dumb-init
RUN chmod +x /usr/bin/dumb-init
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["/bin/bash"]

RUN apt-get update \
 && apt-get upgrade --yes \
 && apt-get install --yes \
     curl \
     git \
     make \
     pandoc \
     pandoc-citeproc \
     python3-pygments \
     fig2dev \
     asymptote biber chktex cm-super context dvidvi dvipng feynmf fragmaster info lacheck latexdiff latexmk lcdf-typetools lmodern prerex psutils purifyeps t1utils tex-gyre texinfo texlive-base texlive-bibtex-extra texlive-binaries texlive-extra-utils texlive-font-utils texlive-fonts-extra texlive-fonts-extra-links texlive-fonts-extra-links texlive-fonts-recommended texlive-formats-extra texlive-games texlive-humanities texlive-lang-czechslovak texlive-lang-english texlive-lang-european texlive-lang-french texlive-lang-german texlive-lang-greek texlive-lang-italian texlive-lang-polish texlive-lang-portuguese texlive-lang-spanish texlive-latex-base texlive-latex-extra texlive-latex-recommended texlive-luatex texlive-metapost texlive-music texlive-pictures texlive-plain-generic texlive-pstricks texlive-publishers texlive-science texlive-xetex tipa vprerex \
     gnuplot \
     hunspell \
     hunspell-pl \
     hunspell-en-us \
     fonts-liberation2 \
 && apt-get clean \
# update impnattypo to latest
 && cd /tmp \
 && curl -OL http://mirrors.ctan.org/macros/latex/contrib/impnattypo.zip \
 && unzip impnattypo.zip \
 && cd impnattypo \
 && lualatex impnattypo.ins \
 && lualatex impnattypo.dtx \
 && cp impnattypo.sty /usr/share/texlive/texmf-dist/tex/latex/impnattypo/impnattypo.sty \
 && mktexlsr \
 && cd / \
 && rm -rf /tmp/*

# install git-info hook
ADD http://mirrors.ctan.org/macros/latex/contrib/gitinfo2/post-xxx-sample.txt /etc/git/hooks/post-checkout
RUN chmod +rx /etc/git/hooks/post-checkout

ARG GROUP=1000
ARG USER=1000

RUN groupadd --gid ${GROUP} latex \
 && useradd --uid ${USER} \
            --create-home \
            --gid latex \
            --shell /bin/bash \
            latex

USER latex
