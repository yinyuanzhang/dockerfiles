FROM frolvlad/alpine-python3

RUN pip install elasticsearch
RUN pip install requests

RUN mkdir /app

WORKDIR /app

CMD ["python3", "start.py" ]

ADD *.py /app/



