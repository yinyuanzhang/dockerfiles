FROM gcc:9.1.0

LABEL maintainer="Ryo Ota <nwtgck@gmail.com>"

ENV NAUTY nauty26r10

RUN \
  # Dowload and decompress
  # (from: http://pallini.di.uniroma1.it/)
  curl http://pallini.di.uniroma1.it/$NAUTY.tar.gz | tar xvzf - && \
  cd $NAUTY && \
  # Build
  ./configure && \
  make && \
  # Install
  # (Create symbolic links to use as commands)
  ls | xargs file | grep "ELF 64-bit LSB executable" | awk '{sub(":", ""); print $1}' | xargs -I {} ln -s $PWD/{}  /usr/local/bin/{}
