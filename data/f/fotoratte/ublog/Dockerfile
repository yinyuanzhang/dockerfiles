FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
VOLUME /code/templates_user
RUN adduser ublog --gecos "" --home /code
RUN chmod +x /code/docker-entrypoint.sh
RUN chown -R ublog:ublog /code
USER ublog

ENTRYPOINT docker-entrypoint.sh