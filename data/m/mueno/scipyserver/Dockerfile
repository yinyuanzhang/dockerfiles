FROM ipython/scipystack

MAINTAINER mueno

VOLUME /notebooks
WORKDIR /notebooks

EXPOSE 8888

# You can mount your own SSL certs as necessary here
ENV PEM_FILE /key.pem
# $PASSWORD will get `unset` within notebook.sh, turned into an IPython style hash
ENV PASSWORD Do not make this your default
ENV USE_HTTP 0

RUN pip install --upgrade pip
RUN pip install elasticsearch arrow pyyaml py-dateutil bokeh
RUN pip3 install elasticsearch arrow pyyaml py-dateutil bokeh xlrd

RUN pip install --upgrade pandas
RUN pip3 install --upgrade pandas

RUN python3 -c "import bokeh.sampledata; bokeh.sampledata.download()"

ADD notebook.sh /
RUN chmod u+x /notebook.sh

CMD ["/notebook.sh"]
