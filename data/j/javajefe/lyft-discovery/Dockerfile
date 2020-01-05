FROM python:2.7.14-stretch
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python wsgi.py