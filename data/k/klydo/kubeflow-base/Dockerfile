FROM python:3.6

# Install modules first so this is cached and won't be rebuilt
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /src/

ENTRYPOINT ["python", "/src/run.py"]
