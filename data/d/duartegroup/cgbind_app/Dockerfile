FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install wget -y
RUN apt-get install git -y
RUN apt-get install gcc -y
RUN apt-get install make -y

WORKDIR /
RUN /usr/bin/wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
RUN /bin/bash miniconda.sh -b -p /miniconda
ENV PATH /miniconda/bin:$PATH
RUN conda config --set always_yes yes --set changeps1 no
RUN conda update -q conda
RUN conda config --append channels conda-forge
RUN conda info -a
RUN conda create -q -n app-env python=3.7
ENV PATH /miniconda/envs/app-env/bin:$PATH
ENV CONDA_DEFAULT_ENV app-env

RUN git clone --single-branch --branch equiv_atoms https://github.com/duartegroup/autodE.git
RUN conda install --file autodE/requirements.txt
RUN cd autodE && python setup.py install && cd ..

RUN git clone --single-branch --branch fast_ba https://github.com/duartegroup/cgbind.git
RUN conda install --file cgbind/requirements.txt
RUN cd cgbind && python setup.py install && cd ..

ENV CELERY_BROKER_URL 'redis://redis:6379/0'
ENV CELERY_RESULT_BACKEND 'redis://redis:6379/0'

ENV POSTGRES_URL "db:5432"
ENV POSTGRES_USER "postgres"
ENV POSTGRES_PW "dbpw"
ENV POSTGRES_DB "cages"
ENV FLASK_APP "server"

ENV DATA_PATH "/data"
RUN mkdir $DATA_PATH

RUN conda install gunicorn
RUN pip install redis
RUN mkdir  /app
COPY requirements.txt /app
WORKDIR /app
RUN conda install --file requirements.txt

COPY app/xtb-191025.tar.xz /app
RUN mkdir /xtb && tar xf xtb-191025.tar.xz -C /xtb
ENV PATH /xtb/bin:$PATH

RUN chmod -R 555 /miniconda/envs/app-env/bin/
RUN groupadd -r appuser && useradd -r -g appuser appuser

COPY . /app
RUN cd app

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "app.server:create_app()"
