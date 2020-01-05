FROM blang/latex
MAINTAINER Sergio R. <sdelrio at users dot noreply dot github dot com>

ADD make_xelatex /usr/bin/make_xelatex
ADD make_latex /usr/bin/make_latex
ADD clean /usr/bin/clean

RUN chmod +x /usr/bin/make_xelatex && chmod +x /usr/bin/make_latex && chmod +x /usr/bin/clean

VOLUME /latex
WORKDIR /latex
