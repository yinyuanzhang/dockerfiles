FROM continuumio/miniconda3:latest
MAINTAINER gH05t_n0Va "frostazy@gmail.com"
EXPOSE 8888
ENV APP_PORT 8888
RUN /opt/conda/bin/conda install jupyter -y --quiet
RUN mkdir workdir \
 && pip install pyquery \
 && pip install pymongo \
 && pip install plotly \
 && pip install pandas \
 && pip install vthread
COPY ["config/notebook.json", "/root/.jupyter/jupyter_notebook_config.json"]
ENTRYPOINT ["/opt/conda/bin/jupyter-notebook"]
CMD ["--notebook-dir=/workdir", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
