
FROM alpine:3.7

LABEL \
    org.label-schema.docker.dockerfile="/Dockerfile" \
    org.label-schema.license="MIT" \
    org.label-schema.name="tallesman/scikit-learn" \
    org.label-schema.url="https://gitlab.com/magnuslang" \
    org.label-schema.vcs-type="Git" \
    org.label-schema.vcs-url="https://github.com/magnuslang/scikit-learn"

# python 3

RUN set -x \
    && apk update \
    && apk --no-cache add \
    ca-certificates \
    python3 \
    su-exec \
    && pip3 install --upgrade pip \
    && ln -s /usr/bin/python3.6 /usr/bin/python \
    ## clean
    && find /usr/lib/python3.6 -name __pycache__ | xargs rm -r \
    && rm -rf /root/.[acpw]* \
    ## user
    && adduser -D  -g '' -s /sbin/nologin -u 1000 docker \
    && echo "Python version installed: " && python --version

RUN apk --no-cache add \
    freetype \
    openblas \
    py3-zmq \
    tini \
    && pip3 install --upgrade pip \
    && pip3 install tornado==4.5.2 \
    && pip3 install notebook==5.2.1 \
    && pip3 install ipywidgets \
    && pip3 install jupyter-console \
    ## numpy 
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && apk --no-cache add --virtual .builddeps \
    build-base \
    freetype-dev \
    gfortran \
    openblas-dev \
    pkgconf \
    python3-dev \
    wget \
    && pip3 install numpy \
    ## scipy
    && pip3 install scipy \
    ## pnadas 
    && apk --no-cache add  \
    py3-dateutil \
    py3-tz \
    && pip3 install pandas \
    ## scikit-learn 
    && pip3 install scikit-learn \
    ## seaborn/matplotlib
    && pip3 install seaborn \
    ## excel read/write 
    && pip3 install xlrd openpyxl \
    ## jp font
    && wget http://dl.ipafont.ipa.go.jp/IPAexfont/ipaexg00301.zip \
    && unzip ipaexg00301.zip \
    && mkdir -p /usr/share/fonts \
    && mv ipaexg00301/ipaexg.ttf /usr/share/fonts/ \
    ## clean
    && apk del .builddeps \
    && find /usr/lib/python3.6 -name __pycache__ | xargs rm -r \
    && rm -rf \
    /root/.[acpw]* \
    ipaexg00301* \
    ## dir
    && mkdir -p /etc/jupyter \
    ## user
    && adduser -D  -g '' -s /sbin/nologin jupyter \
    && addgroup jupyter docker


# jupyter launch

WORKDIR /code

COPY entrypoint.sh  /usr/local/bin/
COPY jupyter_notebook_config.py /etc/jupyter/

EXPOSE 8888

ENTRYPOINT ["/sbin/tini", "--", "entrypoint.sh"]
CMD ["jupyter", "notebook"]