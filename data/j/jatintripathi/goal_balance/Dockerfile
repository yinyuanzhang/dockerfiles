FROM python:2.7
RUN mkdir /code
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD bash ./scripts/start.sh