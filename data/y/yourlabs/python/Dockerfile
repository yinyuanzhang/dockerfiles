FROM node:10-alpine

ENV PYTHONIOENCODING UTF-8
ENV PYTHONUNBUFFERED 1
ENV DEBUG 1

RUN apk update && apk --no-cache upgrade && apk --no-cache add --virtual build-deps curl python3 py3-psycopg2 bash git diffutils libffi-dev py3-cffi python3-dev gcc musl-dev openssl-dev make gettext
RUN ln -sfn /usr/bin/pip3 /usr/bin/pip
RUN ln -sfn /usr/bin/python3 /usr/bin/python
RUN curl -sL https://sentry.io/get-cli/ | bash
RUN pip --no-cache install --upgrade pip
RUN pip install -e git+https://yourlabs.io/oss/processcontroller.git#egg=processcontroller
RUN pip install -e git+https://yourlabs.io/oss/clilabs.git#egg=clilabs
RUN pip install -e git+https://yourlabs.io/oss/autoplay.git#egg=autoplay
ADD requirements.txt /requirements.txt
RUN pip --no-cache install --upgrade -r /requirements.txt

ADD bin/* /bin
