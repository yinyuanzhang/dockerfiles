FROM lambci/lambda-base:build

ENV AWS_EXECUTION_ENV=AWS_Lambda_python2.7 \
    PYTHONPATH=/var/runtime

RUN rm -rf /var/runtime /var/lang && \
  easy_install pip==9.0.3 && \
  pip install -U pip==9.0.3 virtualenv --no-cache-dir && \
  curl https://lambci.s3.amazonaws.com/fs/python2.7.tgz | tar -zx -C /
