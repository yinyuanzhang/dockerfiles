# builds jobs
# pushed to senseyeio/cray-builder
FROM lambci/lambda:build-python3.7
VOLUME /build
VOLUME /output
WORKDIR /processing
CMD cp /build/* . && pip install -t . -r requirements.txt && zip -r job.zip . && mv job.zip /output