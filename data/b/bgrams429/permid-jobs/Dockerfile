FROM python:3.6
MAINTAINER bgrams@cfinlabs.com

COPY . /src
WORKDIR /src

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENTRYPOINT ["python", "get_data.py"]
CMD ["--help"]