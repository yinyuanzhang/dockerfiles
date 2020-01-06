FROM conda/miniconda2:latest

RUN apt-get update && apt-get install -y git

RUN conda create -y -n hmmhc -c bioconda python=2.7 ghmm=0.9 'icu=58.*'
RUN echo "source activate hmmhc" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH
RUN /bin/bash -l -c "source activate hmmhc && pip install git+https://github.com/artyomovlab/hmmhc#egg=hmmhc"
