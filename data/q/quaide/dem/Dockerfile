FROM python:3.7-alpine
RUN apk update && apk upgrade \
&& pip install pyYaml docker
WORKDIR /app
COPY /app/* /app/
CMD python main.py