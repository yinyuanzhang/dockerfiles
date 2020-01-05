FROM python:2.7

# Install uWSGI
RUN pip install uwsgi

# Install all need packets
RUN apt-get update && apt-get install -y uwsgi-plugin-python python-virtualenv python-openslide \
    && rm -rf /var/lib/apt/lists/*

RUN virtualenv /venv
RUN mkdir /app/
ADD requirements.txt /app/requirements.txt
RUN /venv/bin/pip install -r /app/requirements.txt

ADD ./uwsgi.ini /app/uwsgi.ini

EXPOSE 5555
ENTRYPOINT ["/usr/bin/uwsgi", "--ini", "/app/uwsgi.ini"]

