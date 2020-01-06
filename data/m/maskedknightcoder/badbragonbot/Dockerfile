FROM python:3.6

COPY . /app

WORKDIR /app

ENV PATH="${PATH}:/app"

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["entrypoint.sh"]
