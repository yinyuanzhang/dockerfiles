FROM alpine:3.10

LABEL maintainer="Marlon Falcon Hernandez <falconsoft.3d@gmail.com>"

RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3  --no-cache-dir  install -r requirements.txt

CMD python -c "from src import db, create_app; db.create_all(app=create_app())"

ENV FLASK_APP "src"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

EXPOSE 4000

CMD flask run --host=0.0.0.0

ENV MESSAGE "hello PyInvoice"
