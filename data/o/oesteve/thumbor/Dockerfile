FROM python:2


# Things required for a python/pip environment
COPY requirements /usr/src/app/requirements
RUN  \
    awk '$1 ~ "^deb" { $3 = $3 "-backports"; print; exit }' /etc/apt/sources.list > /etc/apt/sources.list.d/backports.list && \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y autoremove && \
    xargs apt-get -y -q install < /usr/src/app/requirements && \
    apt-get clean

ENV HOME /usr/src/app
ENV SHELL bash
ENV WORKON_HOME /usr/src/app
WORKDIR /usr/src/app

RUN pip install \
    envtpl \
    circus \
    circus-web

ADD ./ ./
RUN python setup.py install

RUN \ 
    ln /usr/lib/python2.7/dist-packages/cv2.x86_64-linux-gnu.so /usr/local/lib/python2.7/cv2.so && \
    ln /usr/lib/python2.7/dist-packages/cv.py /usr/local/lib/python2.7/cv.py

ADD conf/circus.ini.tpl /etc/
ADD conf/thumbor.conf.tpl /usr/src/app/
RUN mkdir /etc/circus.d /etc/setup.d
ADD conf/thumbor.ini.tpl /etc/circus.d/

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["circus"]

EXPOSE 8888 8000
