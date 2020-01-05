FROM ubuntu:18.10

# add env to path, as otherwise it is never activated
ENV PATH=/opt/anaconda3/envs/ada/bin:/opt/anaconda3/bin:$PATH

# Download anaconda, accept agreement and install
RUN apt update && \
    apt install -y --no-install-recommends \
        fonts-humor-sans wget openjdk-8-jre-headless && \
    wget https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh && \
    bash Anaconda3-5.3.0-Linux-x86_64.sh -b -p /opt/anaconda3 && \
    rm -rf Anaconda3-5.3.0-Linux-x86_64.sh && \
    apt remove -y wget && \
    conda update conda && \
    conda clean -y --all && \
    apt -y autoremove && \
    apt autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log && \
    # if matplotlib font cache exists, remove it
    rm ~/.cache/matplotlib/ -r || true

# Tutorial 00
RUN conda create -y -n ada python=3.6 scipy pandas numpy matplotlib xlrd && \
    conda clean -y --all
# this does not work, workaround: append env to path
# RUN . activate ada
RUN pip install --upgrade pip
RUN conda install -y -n ada jupyter bokeh seaborn && \
    conda clean -y --all
RUN pip install jupyter_nbextensions_configurator
RUN conda install -y -n ada nb_conda_kernels nb_conda nbpresent && \
    conda clean -y --all
RUN pip install --upgrade ipywidgets
RUN jupyter nbextension enable --py widgetsnbextension
RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension
RUN jupyter serverextension enable --sys-prefix jupyter_nbextensions_configurator
RUN jupyter serverextension enable --sys-prefix nb_conda nbpresent

# Tutorial 04
RUN conda install -y -n ada -c conda-forge pyspark && \
    conda clean -y --all

# This should be unnecessary but in case some one tries to use findspark...
RUN conda install -y -n ada -c conda-forge findspark  && \
    conda clean -y --all
# FIXME: get a more "stable" path
ENV SPARK_HOME=/opt/anaconda3/pkgs/pyspark-2.3.1-py36_1001/lib/python3.6/site-packages/pyspark/

# Tutorial 02 + text tutorial
RUN conda install -y -n ada -c conda-forge folium python-louvain pyLDAvis && \
    conda clean -y --all

# Web scrapping tutorial + applied ML tutorial + graphs tutorial + text tutorial
RUN conda install -y -n ada requests beautifulsoup4 runipy scikit-learn \
                            networkx nltk gensim spacy && \
    conda clean -y --all

RUN python -m spacy download en && \
    python -m nltk.downloader -d /usr/local/share/nltk_data all-corpora && \
    python -m nltk.downloader -d /usr/local/share/nltk_data punkt

RUN pip install vaderSentiment

EXPOSE 8888

RUN adduser --disabled-password --gecos '' user

USER user
WORKDIR /home/user
CMD ["/bin/bash", "-c", "source activate ada ; jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser $jupyter_args ."]
