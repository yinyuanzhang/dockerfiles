FROM ubuntu:16.04

ENV PORT 8888
EXPOSE $PORT

RUN apt-get update 

# Basic Ubuntu Dependencies  
RUN apt-get install -y curl python3 python3-pip python-dev build-essential \
                 python3-dev python3-setuptools

# WeasyPrint dependency (for exporting to PDF)
RUN apt-get install -y python3-dev python3-pip python3-setuptools python3-wheel \
                    python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
                    libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

# PDF conversion kit
RUN apt-get install -y wkhtmltopdf
                
# Jupyter
RUN pip3 install --upgrade pip setuptools
RUN pip3 install jupyter 
RUN pip3 install ipykernel && python3 -m ipykernel install  
RUN pip3 install jupyterlab

# Python packages
RUN pip3 install virtualenv 

# General data processing
RUN pip3 install pandas numpy

# HTML template engines
RUN pip3 install Cheetah3 jinja2

# Machine learning
RUN pip3 install sklearn tensorflow imblearn keras GPy tpot fancyimpute

# Probablistic programming
RUN pip3 install edward

# Statistical computation
RUN pip3 install scipy bootstrapped

# Visualization
RUN pip3 install bokeh wordcloud seaborn 

# Cloud API access
RUN pip3 install boto3 awscli

# PDF conversions
RUN pip3 install pdfkit WeasyPrint

# Saving to Excel files
RUN pip3 install openpyxl XlsxWriter

# Natural language processing
RUN pip3 install nltk gensim

# Download NLTK Data
RUN python3 -m nltk.downloader -d /usr/local/share/nltk_data all

# Dask packages requirement
RUN pip3 install h5py Pillow matplotlib scipy toolz snakeviz graphviz 
RUN pip3 install dask distributed  

# For random data generations
RUN pip3 install names faker

# For parallel executions
RUN pip3 install joblib

# Copy resource files for data generations
ADD resources /root/resources

RUN mkdir /data

USER $NB_USER
CMD cd /data && \
     /usr/local/bin/jupyter lab --port=$PORT --ip=0.0.0.0 --no-browser --allow-root
