FROM python:2.7
MAINTAINER Marc Meszaros <marc@snapable.com>

RUN virtualenv /src
RUN /src/bin/pip install envitro pyrax

COPY backup.py /src/
WORKDIR /src

CMD ["/src/bin/python", "backup.py"]
