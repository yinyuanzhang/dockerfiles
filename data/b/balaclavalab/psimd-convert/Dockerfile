FROM python:3.7-alpine

WORKDIR /app

RUN apk add build-base jpeg-dev zlib-dev && \
    CC="cc -mavx2" pip3 install -U --force-reinstall pillow-simd && \
    pip3 install flask gunicorn && \
    mkdir /mem

COPY gunicorn_config.py app.py ./

EXPOSE 5001

ENTRYPOINT ["gunicorn", "--config", "/app/gunicorn_config.py", "app:app"]
