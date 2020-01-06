FROM python:3

COPY . .

WORKDIR tests

ENV PATH=$PATH:/tests
ENV PYTHONPATH /tests

RUN pip install airtest
RUN pip install pocoui

CMD [ "python", "./test_9pm.air/test_9pm.py" ]
