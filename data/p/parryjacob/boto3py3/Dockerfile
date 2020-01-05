FROM python:3-alpine
MAINTAINER parryjacob

RUN apk --update --no-cache add bash openssh-client
RUN pip install boto3

WORKDIR /root/dev

CMD ["python"]