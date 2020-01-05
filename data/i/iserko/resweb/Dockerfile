FROM python:2.7
MAINTAINER Igor Serko <igor.serko@gmail.com>
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt \
    --exists-action=w && \
    rm /tmp/requirements.txt
ENV PYTHONPATH /opt/resweb
EXPOSE 5000
ADD . /opt/resweb
CMD python -m resweb.core
