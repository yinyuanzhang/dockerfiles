FROM jupyter/base-notebook

USER root

# Install unzip 
RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
    unzip \
    libedit-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Install J
USER jovyan
RUN wget http://www.jsoftware.com/download/j806/install/j806_linux64.tar.gz && \ 
    tar -xvf j806_linux64.tar.gz && \
    echo install \'all\' | /home/jovyan/j64-806/bin/jconsole 
RUN rm j806_linux64.tar.gz

# Install jkernel
#RUN git clone https://github.com/martin-saurer/jkernel.git
RUN wget https://github.com/martin-saurer/jkernel/archive/master.zip && \
    unzip master.zip
RUN mv jkernel-master jkernel  && \
    mv jkernel/jkernel /opt/conda/lib/python3.6/site-packages/ && \
    mv jkernel/kernel_definition/jkernel /opt/conda/share/jupyter/kernels/ && \
    sed -ie "s/^JInsFol = '\/Users\/martin\/J805'/JInsFol = '\/home\/jovyan\/j64-806'/g" /opt/conda/lib/python3.6/site-packages/jkernel/qjide.cfg && \
    mkdir /opt/conda/lib/python3.6/site-packages/notebook/static/components/codemirror/mode/J && \
    mv jkernel/syntax/J.js /opt/conda/lib/python3.6/site-packages/notebook/static/components/codemirror/mode/J/J.js && \
    rm master.zip && rm -r jkernel/syntax jkernel/kernel_definition

# Install widgets
RUN conda install -c conda-forge ipywidgets -y
RUN jupyter nbextension enable --py widgetsnbextension

# Update pip
RUN pip list --outdated --format=legacy | awk '{print $1}' | xargs pip install -U

