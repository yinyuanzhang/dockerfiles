from tiokksar/eclipse

MAINTAINER Tomasz Tokarski tomasz@tomasztokarski.com

WORKDIR /tmp
COPY tmux_24_bit_colours.c /tmux_24_bit_colours.c
RUN git clone git://git.code.sf.net/p/tmux/tmux-code
WORKDIR /tmp/tmux-code
RUN git checkout 1.9a
RUN git apply /tmux_24_bit_colours.c
USER root
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install
