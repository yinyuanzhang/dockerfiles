FROM ipython/scipyserver

RUN pip install --upgrade pip

########################################
#
# Image based on ipython/scipyserver
#
#
# docker run -d -p 444:8888 -e "PASSWORD=XXX" --volumes-from scipy-data l0rth0s/scipyserver
# docker run -d -p 444:8888 -e "PASSWORD=XXX" -v /root/notebooks:/notebooks l0rth0s/scipyserver
#######################################

# Install opencv prerequisites...
RUN apt-get update -qq && apt-get install -y --force-yes \
            libopencv-dev \
            python-opencv;


# Additional python modules
RUN pip2 install imutils
RUN pip3 install imutils

RUN pip2 install bokeh
RUN pip3 install bokeh

RUN pip2 install ggplot
RUN pip3 install ggplot

RUN pip2 install mpld3
RUN pip3 install mpld3

RUN pip2 install vincent
RUN pip3 install vincent

RUN pip2 install keras
RUN pip3 install keras

RUN pip2 install textblob
RUN pip3 install textblob
RUN python -m textblob.download_corpora

RUN pip2 install seaborn
RUN pip3 install seaborn

RUN pip2 install ipywidgets
RUN pip3 install ipywidgets

RUN pip2 install folium
RUN pip3 install folium

RUN pip2 install boto
RUN pip3 install boto

# RUN python -m nltk.downloader all-corpora

RUN pip2 install -r https://raw.githubusercontent.com/automl/auto-sklearn/master/requirements.txt
RUN pip3 install -r https://raw.githubusercontent.com/automl/auto-sklearn/master/requirements.txt

RUN pip2 install auto-sklearn
RUN pip3 install auto-sklearn

VOLUME /notebooks
WORKDIR /notebooks
