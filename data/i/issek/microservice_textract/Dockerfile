FROM python:3.5

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get -qq -y install swig libpulse-dev unrtf catdoc antiword enca
RUN pip3 install -r requirements.txt && pip3 install gunicorn && mkdir uploaded

ENV FLASK_APP wsgi.py
EXPOSE 5000

CMD ["gunicorn", "--workers=1","--timeout=3600", "-b 0.0.0.0:5000","wsgi:app"]

