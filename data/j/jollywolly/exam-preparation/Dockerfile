FROM python:3.6.6-stretch

ENV LANG C.UTF-8
RUN apt-get update

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./ /usr/src/app

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

# run the application
CMD ["run.sh"]
