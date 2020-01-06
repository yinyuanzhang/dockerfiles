FROM python:latest

RUN pip install poetry
RUN mkdir /project
WORKDIR /project
RUN poetry init

ADD pup.sh /usr/local/bin
ENTRYPOINT ["/usr/local/bin/pup.sh"]
CMD ["shell"]
