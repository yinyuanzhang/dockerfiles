FROM python:alpine
RUN pip install elasticsearch-curator requests_aws4auth
COPY config.yml delete-indices.yml docker-entrypoint.sh /
ENTRYPOINT [ "/docker-entrypoint.sh" ]
