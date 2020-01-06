FROM python:3-onbuild

RUN apt-get update && apt-get install -y \
    python3-pip

RUN pip3 install requests

ENTRYPOINT ["python", "./client.py"]
