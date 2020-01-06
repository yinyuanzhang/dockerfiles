FROM python:2.7
MAINTAINER Austin Keller <atkeller@uw.edu>

RUN groupadd -r appuser && \
    useradd -r -g appuser appuser

RUN mkdir -p /app/wd && \
chmod -R 777 /app/wd

COPY pipeline.py /app

WORKDIR /app/wd

USER appuser

CMD ["python", "/app/pipeline.py", "-h"]
