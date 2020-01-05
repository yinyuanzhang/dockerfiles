FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        less postgresql-client
#RUN mkdir /apps
WORKDIR /app
#ARG BUILD_ENV=dev
ADD config/requirements.txt ./requirements.txt
RUN pip install --upgrade pip; \
    pip install -r requirements.txt
RUN django-admin startproject project .;
COPY ./apps ./app


#FROM python:3
#RUN apt-get update \
#    && apt-get install -y --no-install-recommends \
#        less postgresql-client
#WORKDIR /usr/src/app
#ARG BUILD_ENV=prod
#ADD config/requirements ./requirements
#RUN pip install --upgrade pip; \
#    pip install -r requirements/$BUILD_ENV.txt
#RUN django-admin startproject myproject .; \
#    mv ./myproject ./origproject
