FROM python:3.5-buster

#ENV PYPI_REPO=https://pypi.tuna.tsinghua.edu.cn/simple/ 
ENV PYPI_REPO=https://pypi.python.org/simple/

RUN apt-get update && apt-get install -y --no-install-recommends \
		nginx \
	&& rm -rf /var/lib/apt/lists/*

COPY documents /tmp/documents
COPY requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt -i ${PYPI_REPO}
COPY entrypoint.sh .
COPY templates /tmp/templates
COPY action.yaml .

EXPOSE 80

CMD ["/bin/bash", "entrypoint.sh"]
