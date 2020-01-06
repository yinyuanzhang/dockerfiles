FROM python:3.6.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /usr/src/nanashe
WORKDIR /usr/src/nanashe
ADD requirements.txt /usr/src/nanashe
RUN pip install -r requirements.txt
ADD . /usr/src/nanashe
VOLUME /var/nanashe
CMD gunicorn -b 0.0.0.0:8000 nanashe.wsgi
