FROM sharelatex/sharelatex:v1.2.1

# Set the new PATH for TeX Live 2018
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/texlive/2018/bin/x86_64-linux/

# Copy the previous TeX Live environment
RUN cd /usr/local/texlive ; \
    cp -a 2017 2018

# Upgrade to Tex Live 2018 from official instructions :
#	https://www.tug.org/texlive/upgrade.html
RUN cd /usr/local/texlive/2018 ; \
    wget --quiet -- http://mirror.ctan.org/systems/texlive/tlnet/update-tlmgr-latest.sh ; \
    sh update-tlmgr-latest.sh  -- --upgrade ; \
    tlmgr update --self --all

# Install additionnals packages {{{
RUN tlmgr install adjustbox \
                  amscls \
                  amsfonts \
                  amsmath \
                  booktabs \
                  babel \
                  babel-english \
                  babel-french \
                  bigfoot \
                  caption \
                  chemstyle \
                  cite \
                  enumitem \
                  epstopdf \
                  float \
                  fncychap \
                  footmisc \
                  geometry \
                  graphics \
                  hyperref \
                  latex \
                  lettrine \
                  lineno \
                  lipsum \
                  lm \
                  mathtools \
                  mhchem \
                  multirow \
                  natbib \
                  oberdiek \
                  pdfpages \
                  psnfss \
                  physics \
                  placeins \
                  siunitx \
                  sttools \
                  subfigure \
                  subfloat \
                  textgreek \
                  tools \
                  wrapfig \
                  xcolor
# }}}

# Ensure Sharelatex can use TeX Live 2018
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/texlive/2018/bin/x86_64-linux/
