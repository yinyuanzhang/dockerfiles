FROM python:3.6.6-slim
LABEL maintainer="Ryan Marren <marrenr@mskcc.org>"

COPY ./requirements.txt /tmp/
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

COPY ./app /app/
COPY ./gunicorn_config.py /

EXPOSE 8080

ENTRYPOINT ["gunicorn", "--config", "/gunicorn_config.py", "-b", ":8080", "app"]