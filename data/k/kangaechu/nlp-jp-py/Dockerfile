FROM kangaechu/nlp-jp:latest

ENV PYKNP_PKG='pyknp-0.3'
WORKDIR /nlp

ADD http://nlp.ist.i.kyoto-u.ac.jp/DLcounter/lime.cgi?down=http://lotus.kuee.kyoto-u.ac.jp/nl-resource/pyknp/${PYKNP_PKG}.tar.gz&name=${PYKNP_PKG}.tar.gz ${PYKNP_PKG}.tar.gz
RUN apk add --update --no-cache python3 mecab-dev bash openblas && \
  apk add --no-cache --virtual .builddeps musl linux-headers gcc g++ make gfortran openblas-dev python3-dev && \
  tar xzf ${PYKNP_PKG}.tar.gz && \
  cd ${PYKNP_PKG} && \
  python3 setup.py install && \
  cd .. && \
  rm -rf pyknp-* && \
  pip3 install --upgrade pip && \
  pip install six numpy scipy scikit-learn mecab-python3 && \
  apk del .builddeps

CMD [ "/bin/sh" ]
