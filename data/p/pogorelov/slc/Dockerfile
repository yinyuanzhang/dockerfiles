FROM python:3.7.0-stretch
COPY . /slc
WORKDIR /slc
RUN pip install -r /slc/requirements.txt
ENTRYPOINT ["python", "/slc/slc.py" ]