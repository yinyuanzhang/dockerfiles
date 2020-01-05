FROM debian:buster
ADD https://github.com/geckoboard/sql-dataset/releases/download/v0.2.4/sql-dataset-linux-amd64 /sql-dataset
RUN apt-get update && apt-get install -y ca-certificates
RUN chmod +x /sql-dataset
ENTRYPOINT ["/sql-dataset"]
CMD ["-config", "/config.yml"]

