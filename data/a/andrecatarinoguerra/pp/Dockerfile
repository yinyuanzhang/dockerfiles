FROM python:3.7-alpine
RUN apk update --no-cache 
RUN apk add git --no-cache
RUN apk add curl --no-cache
RUN apk add build-base --no-cache
RUN apk add libffi-dev libressl-dev --no-cache
ENV PATH "/root/.poetry/bin:${PATH}"
RUN curl -o get-poetry.py https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py
RUN python get-poetry.py --version 1.0.0b9
RUN poetry config virtualenvs.in-project true
