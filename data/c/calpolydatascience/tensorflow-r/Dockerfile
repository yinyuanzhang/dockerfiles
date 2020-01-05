FROM jupyter/tensorflow-notebook:1386e2046833 
# latest as of 10-15-2019

# install R and dependancies into image 
RUN conda update -n base conda && \
    conda install -c r r-irkernel
