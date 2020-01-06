FROM dclong/jupyterhub-jdk

RUN pip3 install --no-cache-dir --upgrade --ignore-installed entrypoints

RUN pip3 install --no-cache-dir \
        mypy pylint flake8 yapf pytest \
        numpy scipy pandas pyarrow==0.12.1 dask[dataframe] \
        scikit-learn xgboost \
        matplotlib bokeh holoviews[recommended] \
        tabulate \
        JayDeBeApi sqlparse \
        requests[socks]

RUN jupyter labextension install @pyviz/jupyterlab_pyviz \
    && npm cache clean --force
