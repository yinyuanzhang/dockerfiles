FROM python:latest

MAINTAINER Manuel J. Garrido <manuel.garrido@gmail.com>

RUN pip install "Nikola[extras]"

ENV NIKOLA_HOME /home/nikola

RUN useradd -d $NIKOLA_HOME -m -s /bin/bash nikola

WORKDIR $NIKOLA_HOME

VOLUME $NIKOLA_HOME

EXPOSE 8000

USER nikola

ENTRYPOINT ["/bin/bash"]