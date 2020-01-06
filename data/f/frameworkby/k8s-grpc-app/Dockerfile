FROM python:3.7-alpine

RUN apk add --no-cache g++ musl-dev 
# libffi libffi-dev

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ENV PYTHONPATH=/app
ENV GRPC_VERBOSITY=DEBUG

COPY . /app

WORKDIR /app

ENTRYPOINT ["python"]

CMD ["main.py"]
