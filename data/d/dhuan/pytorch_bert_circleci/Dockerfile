FROM circleci/python:3.7.3-stretch

USER root

COPY pip.conf /etc/pip.conf
#COPY Pipfile ./Pipfile
#COPY Pipfile.lock ./Pipfile.lock
COPY requirements.txt /bert/requirements.txt
# download bert-base-chinese in advance
# COPY bert-base-chinese /bert/bert-base-chinese
RUN mkdir /bert/bert-base-chinese \
    && wget https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-chinese-vocab.txt \
    && wget https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-chinese-pytorch_model.bin \
    && wget https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-chinese-config.json \
    && mv bert-base-chinese-vocab.txt /bert/bert-base-chinese/vocab.txt \
    && mv bert-base-chinese-pytorch_model.bin /bert/bert-base-chinese/pytorch_model.bin \
    && mv bert-base-chinese-config.json /bert/bert-base-chinese/bert_config.json

# use pipenv
RUN pip install --upgrade pip \
    && pip install -r /bert/requirements.txt \
    && pip install pytest \
    && pip install flake8
# RUN pip install --upgrade pip && pip install pipenv \
#     && pipenv install -d \
#     && pipenv install --system \
#     && pipenv --rm \
#     && pip uninstall -y pipenv

ENV TEST_BERT_DIR /bert/bert-base-chinese
ENV TEST_DEVICE_TYPE cpu

USER circleci
