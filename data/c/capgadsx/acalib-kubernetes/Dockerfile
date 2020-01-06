FROM csrg/generic_builder:latest
MAINTAINER Carlos Ponce <cponce@alumnos.inf.utfsm.cl>
ENV LANG="en_US.UTF-8" \
    LC_ALL="en_US.UTF-8" \
    PATH="/opt/conda/bin:$PATH"
WORKDIR /root
RUN conda install -y libgfortran bokeh urllib3
ADD https://raw.githubusercontent.com/capgadsx/acalib/dask-testing/requirements.txt requirements.txt
RUN pip install -r requirements.txt