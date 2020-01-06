FROM gliderlabs/alpine

RUN if [ ! -d /home/core ] ; then mkdir -p /home/core ; fi

ENV PYPY pypy-2.5.0-linux64

ADD https://bitbucket.org/pypy/pypy/downloads/${PYPY}.tar.bz2 /home/core/${PYPY}.tar.bz2

VOLUME /home/host-core

ADD install-to-coreos.sh /

CMD sh /install-to-coreos.sh ${PYPY}

