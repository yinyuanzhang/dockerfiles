FROM python:3.6-alpine

RUN apk --no-cache --update-cache add gcc gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev

RUN pip install scipy

WORKDIR /app
RUN apk add --no-cache libjpeg-turbo-dev libpng-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
