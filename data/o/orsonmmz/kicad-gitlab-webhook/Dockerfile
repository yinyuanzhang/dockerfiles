FROM alpine:3.8

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
COPY server.py /app

RUN apk add --update --no-cache python3
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

USER 1000

CMD sh ./launcher.sh
EXPOSE 5000
