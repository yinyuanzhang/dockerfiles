FROM python:2.7-alpine
RUN apk add --update --no-cache \
    findutils
RUN pip install --upgrade b2
CMD ["b2", "version"]
