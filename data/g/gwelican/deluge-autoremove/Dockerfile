FROM python:3-alpine

WORKDIR /app

COPY Pipfile .
RUN pip install pipenv && pipenv install
ADD deluge.py .

CMD ["pipenv","run","python","deluge.py"]

