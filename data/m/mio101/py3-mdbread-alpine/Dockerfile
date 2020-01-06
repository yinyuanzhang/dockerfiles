FROM python:3.6.1-alpine

# --------------------- install mdbread ---------------------
COPY mdbtools-0.7.1.zip mdbread /tmp/
# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
RUN apk --no-cache add \
    autoconf \
    automake \
    build-base \
    glib \
    glib-dev \
    libtool && \

  # install mdb-tools
  cd /tmp && \
  unzip mdbtools-0.7.1.zip && rm mdbtools-0.7.1.zip && \
  cd mdbtools-0.7.1 && \
  autoreconf -i -f && ./configure --disable-man && make && make install && \

  # install mdbread
  pip install --no-cache-dir Cython && \
  cd /tmp && \
  ln -s /usr/include/locale.h /usr/include/xlocale.h && \
  export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig/ && \
  cp /tmp/mdbtools-0.7.1/include/mdbsql.h /tmp/mdbtools-0.7.1/include/mdbtools.h /usr/lib/glib-2.0/include/ && \
  python setup.py install && \

  # clean up
  apk update && \
  apk del build-base autoconf automake glib-dev && \
  apk info && \
  rm -rf /tmp/*

# --------------------- install parser ---------------------
# COPY parser /parser
# WORKDIR /parser
CMD ["python"]

