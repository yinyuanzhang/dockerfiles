FROM fynbab/boto3image:latest
ENV PYTHONPATH=/usr/local/lib/python3.7/site-packages
WORKDIR /src
COPY ./s3.py /src/
COPY ./config.py /src/
ENTRYPOINT ["/usr/bin/python", "/src/s3.py"]
