FROM alpine:latest
LABEL maintainer="andrei.ozerov92@gmail.com"
LABEL version="1.0.4"

RUN apk update && apk upgrade && \
    apk add --no-cache \
    patch \
    python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install -UI \
    pip \
    pbr \
    setuptools \
    jenkins-job-builder==2.0.3 && \
    rm -r /root/.cache

COPY files/0001-reset-anchors.patch /usr/lib/python3.6/site-packages/jenkins_jobs/0001-reset-anchors.patch

RUN cd /usr/lib/python3.6/site-packages/jenkins_jobs && \
    patch < 0001-reset-anchors.patch

CMD [ "sh", "-c", "jenkins-jobs --ignore-cache --conf ${JENKINS_INI} -l debug update --workers ${WORKERS} -r ${JOBS_DIR}" ]
