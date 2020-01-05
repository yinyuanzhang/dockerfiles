FROM python:3.7

RUN \
    useradd user \
    && mkdir /home/user \
    && chown user:user /home/user \
    && pip3 install \
        ipython \
        scipy \
        scikit-learn \
        pandas \
        matplotlib \
        xgboost \
        lightgbm \
        catboost \
        seaborn \
        jupyter

WORKDIR /home/user
USER user
CMD [ "ipython" ]
