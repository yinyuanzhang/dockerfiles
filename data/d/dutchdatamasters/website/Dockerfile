FROM python:3.7.2-stretch

MAINTAINER rene.cleijpool@dutchdatamasters.com



ADD . /app
WORKDIR /app

# Config files


RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app
ENV FLASK_DEBUG=1

 
#CMD ["uwsgi", "uwsgi.ini"]
CMD ["flask" , "run", "--host=0.0.0.0"]
