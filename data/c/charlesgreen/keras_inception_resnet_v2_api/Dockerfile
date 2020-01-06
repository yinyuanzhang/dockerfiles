FROM tensorflow/tensorflow:2.0.0-py3

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app /app
COPY ./app/models /app/models
WORKDIR /app
