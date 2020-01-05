FROM python:3.7-alpine

RUN pip install --no-cache-dir ruamel.yaml==0.15.89

COPY generate.py /usr/local/bin/

COPY docker_generate.py /usr/local/bin

ENTRYPOINT ["/usr/local/bin/generate.py"]

CMD ["-h"]

