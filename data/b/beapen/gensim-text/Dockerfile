FROM continuumio/miniconda3

RUN mkdir /code

WORKDIR /code

COPY . /code/

RUN conda install -n base -c anaconda --file /code/requirements.txt && \
    conda clean --all --yes

RUN echo "conda activate base" >> ~/.bashrc
