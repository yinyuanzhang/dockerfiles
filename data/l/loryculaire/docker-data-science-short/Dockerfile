FROM "continuumio/anaconda3"

RUN mkdir /opt/notebooks
RUN jupyter notebook --generate-config --allow-root
RUN echo "c.NotebookApp.password = u'sha1:6a3f528eec40:6e896b6e4828f525a6e20e5411cd1c8075d68619'" >> /root/.jupyter/jupyter_notebook_config.py

RUN conda update conda
RUN conda update anaconda
RUN conda update --all
RUN conda install -c pytorch -c fastai fastai
RUN conda install -c conda-forge xgboost
#RUN conda install -c conda-forge keras



EXPOSE 8888

CMD ["jupyter", "notebook", "--allow-root", "--notebook-dir=/opt/notebooks", "--ip='0.0.0.0'", "--port=8888", "--no-browser"]
