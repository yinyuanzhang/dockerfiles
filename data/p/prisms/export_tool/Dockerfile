FROM python:3.6-alpine

WORKDIR /app

# RUN apk add --no-cache python3-dev && \
#     apk add --no-cache --virtual .build-deps g++ libstdc++ && \
#     ln -s /usr/include/locale.h /usr/include/xlocale.h && \
#     pip install pipenv && \
#     pipenv install --deploy --system && \
#     apk del .build-deps

RUN apk --no-cache --update-cache add gcc \
    gfortran python3-dev py-pip build-base \
    wget freetype-dev libpng-dev openblas-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

ENV PIP_NO_CACHE_DIR false
COPY Pipfile /app
COPY Pipfile.lock /app
RUN pip install pipenv
RUN pipenv install --deploy --system

COPY . /app

EXPOSE 8000

CMD ["gunicorn", "-b", ":8000", "--capture-output", "app:app"]
