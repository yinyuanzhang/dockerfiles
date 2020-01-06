FROM python:3.7-alpine

RUN set -ex \
 && apk add --no-cache freetype libpng openblas libxml2 libxslt tini libzmq git \
 && apk add --no-cache --virtual build-deps gcc libc-dev g++ freetype-dev libpng-dev openblas-dev libxml2-dev libxslt-dev \
 && pip install --no-cache-dir numpy matplotlib scipy pandas scikit-learn notebook==5.6.0 jupyter \
 && pip install --no-cache-dir jupyter_contrib_nbextensions \
 && pip install --no-cache-dir BeautifulSoup4 html5lib plyfile \
 && apk del build-deps \
 && rm -rf /var/cache/apk/* \
 && find /usr/local/lib/python3.7/ -type d -name tests -depth -exec rm -rf {} \; \
 && find /usr/local/lib/python3.7/ -type d -name test -depth -exec rm -rf {} \; \
 && find /usr/local/lib/python3.7/ -name __pycache__ -depth -exec rm -rf {} \; \
 && adduser jupy -D

USER jupy
RUN jupyter contrib nbextension install --user && \
    git clone https://github.com/authman/DAT210x.git /home/jupy/DAT210x

EXPOSE 8888
WORKDIR /home/jupy/DAT210x
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser"]
