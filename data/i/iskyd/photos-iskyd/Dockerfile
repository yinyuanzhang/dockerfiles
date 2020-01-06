FROM python:3.7

WORKDIR /home/photos

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -

RUN apt-get update && apt-get install -y vim nodejs

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY ./ .

RUN venv/bin/pip install -e .

RUN npm install -g gulp && npm install && gulp static

COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

ENV FLASK_APP photos

EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
