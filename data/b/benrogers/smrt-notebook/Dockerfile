FROM jupyter/scipy-notebook:702d2f6a3eaa

RUN pip install ipyleaflet==0.9.0

RUN jupyter nbextension install --py --symlink --sys-prefix ipyleaflet \
 && jupyter nbextension enable --py --sys-prefix ipyleaflet \
 && jupyter labextension install @jupyter-widgets/jupyterlab-manager

RUN conda install jupyter_dashboards -c conda-forge
