# https://medium.com/@chadlagore/conda-environments-with-docker-82cdc9d25754
FROM continuumio/miniconda3:4.5.11

COPY eprime_convert.yml /env/

RUN conda env create -f /env/eprime_convert.yml &&\
    conda clean --all

# Pull the environment name out of the environment.yml
RUN echo "source activate $(head -1 /env/eprime_convert.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 /env/eprime_convert.yml | cut -d' ' -f2)/bin:$PATH

ENTRYPOINT [ "/bin/bash", "-c" ]