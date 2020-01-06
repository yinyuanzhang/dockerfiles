FROM python:alpine

RUN pip install "flask==1.1.1"
RUN pip install "luqum==0.8.0"
RUN pip install "waitress==1.3.1"

COPY app app

ENTRYPOINT waitress-serve --port=80 --call 'app.app:create_app'
