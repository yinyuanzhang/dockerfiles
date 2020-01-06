FROM ubuntu:latest
MAINTAINER makefu

RUN apt-get -q update && apt-get -y -q upgrade && apt-get -y -q install build-essential python-pip python-dev git && apt-get clean
RUN pip install markdown pelican
RUN mkdir /pelican
COPY . /pelican
RUN rm -rf /pelican/output
RUN cd /pelican && pelican
WORKDIR /pelican/output
EXPOSE 8000
CMD ["python","-m","SimpleHTTPServer","8000"]
