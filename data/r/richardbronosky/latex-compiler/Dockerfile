FROM ubuntu

MAINTAINER Bruno Bronosky <bruno@bronosky.com>

RUN apt-get update

RUN apt-get install -y file texlive-latex-recommended

ADD latexcat /usr/local/bin/latexcat
RUN chmod a+x /usr/local/bin/latexcat

VOLUME /work

ENTRYPOINT ["/usr/local/bin/latexcat"]
