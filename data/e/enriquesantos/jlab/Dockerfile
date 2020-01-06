FROM python:3

RUN pip install --upgrade pip && \
    pip install \
            sklearn \
            jupyter \
            jupyterlab \
            tensorflow \
            xgboost \ 
            bayesian-optimization \
            mxnet \
            lightgbm \
            pandas-profiling \
            optml

RUN jupyter serverextension enable --py jupyterlab --sys-prefix

ENTRYPOINT ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
