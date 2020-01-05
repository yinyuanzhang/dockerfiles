FROM chunjiesamliu/jukeras-base:latest
LABEL maintainer="Chun-Jie Liu <chunjie-sam-liu@foxmail.com>"

COPY requirements.txt requirements.sys /tmp/

USER root
RUN apt-get update -qq \
  # install packages from requirements.sys
  && xargs apt-get -y --no-install-recommends install < /tmp/requirements.sys \
  && apt-get clean \
  && apt-get autoremove \
  && rm -rf /var/lib/apt/lists/* /tmp/requirements.sys

USER $NB_UID
WORKDIR $HOME

RUN conda install --quiet --yes --file /tmp/requirements.txt \
  && conda clean --all -f -y \
  && fix-permissions $CONDA_DIR \
  && fix-permissions /home/$NB_USER