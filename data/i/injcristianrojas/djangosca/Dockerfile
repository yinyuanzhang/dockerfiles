FROM alpine:3.1
MAINTAINER Cristián Rojas

RUN apk add --update python python-dev py-pip build-base git
RUN pip install Django
RUN git clone https://bitbucket.org/injcristianrojas/djangosca.git /djangosca

WORKDIR /workdir

CMD ["python", "/djangosca/djangoSCA.py", "-r", "/djangosca/djangoSCA.rules", \
    "/workdir"]
