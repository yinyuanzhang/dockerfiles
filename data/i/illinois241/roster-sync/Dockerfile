FROM python:3.6-alpine

ADD . /usr/local/share/roster-sync

RUN pip install -r /usr/local/share/roster-sync/requirements.txt

ENTRYPOINT ["python", "/usr/local/share/roster-sync/main.py"]
