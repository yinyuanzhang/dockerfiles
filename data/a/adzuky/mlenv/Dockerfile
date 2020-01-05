# ベースとなる環境
# FROM <イメージ名>:<バージョンタグ>
FROM  nvidia/cuda:9.0-cudnn7-devel

# 作成者
MAINTAINER adzuky

# ライブラリのインストール
RUN set -x && \
    apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    curl git unzip imagemagick bzip2 libglib2.0-0 libsm6 libxrender1 libxext6 libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* && \
    git clone https://github.com/pyenv/pyenv.git /.pyenv

WORKDIR /
ENV HOME /
ENV PYENV_ROOT /.pyenv
ENV PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"

# anaconda3-5.1.0のpackage list: http://docs.anaconda.com/anaconda/packages/old-pkg-lists/5.1.0/py3.6_linux-64/
RUN set -x && \
    pyenv install anaconda3-5.1.0 && \
    pyenv global anaconda3-5.1.0 && \
    pyenv rehash

# opencv-python: コンピュータビジョンライブラリ
# tqdm: プログレスバーの表示
# kaggle-cli: kaggle公式cliツール
# gym: OpenAIの強化学習用シミュレーションプラットフォーム
# 以下2018/11/11での最新バージョン
# tensorflow-gpu: v1.12.0
# keras: v2.2.4
# chainer: v5.0.0
# chainerui: v0.6.0
# cupy-cuda90: v5.0.0
RUN set -x && \
    pip install opencv-python tqdm kaggle-cli gym && \
    pip install tensorflow-gpu==1.11.0 && \
    pip install keras==2.2.4 && \
    pip install chainer==5.0.0 && \
    pip install chainerui==0.6.0 && \
    pip install cupy-cuda90==5.0.0
