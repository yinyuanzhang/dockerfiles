FROM python:3.7-alpine as base
FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base
ENV EXPOSE_PORT 5000
ENV http_proxy=host.docker.internal:4140
EXPOSE $EXPOSE_PORT
COPY --from=builder /install /usr/local
RUN mkdir /src
WORKDIR /src
COPY server.py /src/server.py
CMD ["gunicorn", "-b", "0.0.0.0:$EXPOSE_PORT", "server:api"]
