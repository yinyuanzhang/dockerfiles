FROM python:3.7
# FROM python:3.7-alpine
# RUN apk update
# RUN apk add make automake gcc g++ subversion python3-dev

WORKDIR /app

COPY . /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD [ "python3", "app.py" ]