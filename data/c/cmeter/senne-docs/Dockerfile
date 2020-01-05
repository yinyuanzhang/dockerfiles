FROM python:3.7-alpine AS builder

RUN apk add --no-cache make && \
    pip install -U sphinx sphinx-rtd-theme

COPY . /code

WORKDIR /code/docs

RUN make html


FROM nginx:alpine

WORKDIR /usr/share/nginx/html

COPY --from=builder /code/docs/_build/html .