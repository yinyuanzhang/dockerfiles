FROM ucsdets/datascience-notebook:2019.4-stable

LABEL maintainer="UC San Diego ITS/ETS <ets-consult@ucsd.edu>"

RUN conda install --quiet --yes \
		nltk
RUN python -m nltk.downloader -d /opt/conda/share/nltk_data all