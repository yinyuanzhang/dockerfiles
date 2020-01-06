FROM ubuntu:16.04

COPY . /app

WORKDIR /app

RUN apt-get update
RUN apt-get install -y python3-pip python3.5-dev
RUN cd /usr/local/bin && ln -s /usr/bin/python3 python  && pip3 install --upgrade pip
RUN cd /app

RUN pip3 install -r requirements.txt

ENV NAME Microservice_scatterplot
CMD ["gunicorn", "--workers=4", "-b 0.0.0.0:5000","wsgi:app"]

EXPOSE 5000
