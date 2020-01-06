FROM tparkerusgs/avopytroll:release-1.9.0

WORKDIR /app
COPY segment_gatherer.ini .
COPY trollstalker.ini .
COPY DOIRootCA.crt .

WORKDIR /app/avoviirscollector
COPY cron-viirscollector .
COPY setup.cfg .
COPY setup.py .
COPY bin bin
COPY avoviirscollector avoviirscollector
RUN python setup.py install

COPY supervisord.conf /etc/supervisor/supervisord.conf
ENV PYTHONUNBUFFERED=1

RUN pip freeze > requirements.txt
CMD ["mirror_gina"]
