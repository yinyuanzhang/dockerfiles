FROM dockerbase/devbase-pip

ADD . /app
WORKDIR /app
RUN sudo python setup.py install

ENTRYPOINT ["youtube-dl-server"]
EXPOSE 9191

