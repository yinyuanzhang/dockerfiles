FROM python:3.6-slim
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
# RUN apk --update add python py-pip openssl ca-certificates py-openssl wget
# RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev \
#         python-dev py-pip build-base lapack-dev openblas-dev gfortran\
#         && pip install --upgrade pip \
#         && pip install -r requirements.txt \
#         && apk del build-dependencies
