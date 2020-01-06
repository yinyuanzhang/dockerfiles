FROM ubuntu:latest

RUN apt -y update
RUN apt -y install python3-pip python3 python3-dev
COPY *           /webapp/
COPY templates/* /webapp/templates/
COPY static/css/*     /webapp/static/css/
COPY static/js/*     /webapp/static/js/
WORKDIR /webapp
RUN pip3 install -r requirements.txt
RUN export KUBECONFIG=/webapp/config
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]

EXPOSE 8000