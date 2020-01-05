FROM jupyter/datascience-notebook:latest
USER root
RUN conda update -y pandas && conda install -y OpenCV basemap && pip install plotly mapsplotlib

#Install XKCD fonts. Just because.
RUN apt update && apt install fonts-humor-sans && rm ~/.cache/matplotlib -r

#Make somewhat compatible with singularity on TSD. 
RUN mkdir /tsd /usit /work /projects 

