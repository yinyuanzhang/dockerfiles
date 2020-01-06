FROM python:3.7.2-alpine3.8
COPY run-clang-format.py /
RUN apk add clang
RUN mkdir /files
WORKDIR /files

ENTRYPOINT ["python", "/run-clang-format.py"]