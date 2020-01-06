FROM python:3-alpine

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk --no-cache --update-cache add git gcc gfortran build-base wget freetype-dev libpng-dev openblas-dev libxml2-dev libxslt-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN pip install --no-cache-dir numpy scipy cython lxml scikit-learn
RUN pip install --no-cache-dir git+https://github.com/dragnet-org/dragnet
