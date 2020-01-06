FROM python:3.7-buster

# install texlive
RUN mkdir texlive_install \
  && curl http://mirror.utexas.edu/ctan/systems/texlive/tlnet/install-tl-unx.tar.gz | tar xvz -C ./texlive_install --strip 1 \
  && ./texlive_install/install-tl -scheme small -portable -profile /dev/null

# add to path
ENV PATH="${PATH}:/usr/local/texlive/bin/x86_64-linux"
