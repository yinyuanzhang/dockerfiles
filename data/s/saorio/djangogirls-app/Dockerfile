FROM python:3.6.4-jessie
ENV TZ=Asia/Tokyo

RUN apt-get update && apt-get install -y vim git

RUN mkdir djangogirls
WORKDIR djangogirls

RUN python -m venv myvenv
COPY . ./

RUN /bin/bash -c "source myvenv/bin/activate; pip install -r requirements.txt"
