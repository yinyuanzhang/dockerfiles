FROM python:3.7-stretch as base

FROM base as builder

MAINTAINER Fisher Pri Catz "fisher.wei@wqfw.de"

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /app

ENTRYPOINT ["bash", "-c", "git clone $GIT_REPO /app && pip install -r requirements.txt ; $ENTRYPOINT"]

