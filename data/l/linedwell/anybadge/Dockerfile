FROM python:2.7.17-alpine3.10
LABEL name=anybadge version=0.1 maintainer=Linedwell

RUN pip install --no-cache-dir \
    anybadge==1.1.1 \
    && pip uninstall pip -y
