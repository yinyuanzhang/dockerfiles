FROM python:3.6.8-alpine3.8

RUN apk add --update --no-cache \
    --virtual=.build-dependencies \
    git && \
    mkdir /src && \
    cd /src && \
    git clone --recursive -b v0.81 https://github.com/dmlc/xgboost && \
    sed -i '/#define DMLC_LOG_STACK_TRACE 1/d' /src/xgboost/dmlc-core/include/dmlc/base.h && \
    sed -i '/#define DMLC_LOG_STACK_TRACE 1/d' /src/xgboost/rabit/include/dmlc/base.h && \
    apk del .build-dependencies

RUN apk add --update --no-cache \
    --virtual=.build-dependencies \
    make gfortran gcc musl-dev linux-headers swig \
    python3-dev \
    py-setuptools g++ && \
    apk add --no-cache openblas lapack-dev libexecinfo-dev libstdc++ libgomp && \
    pip install setuptools && \
    pip install nose && \
    pip install Cython && \
    pip install numpy==1.15.4 && \
    pip install scipy==1.2.0 && \
    pip install pandas==0.23.4 scikit-learn==0.19.0 && \
    pip install lockfile && \
    pip install joblib && \
    pip install psutil && \
    pip install pyyaml && \
    pip install liac-arff && \
    pip install ConfigSpace==0.4.7 && \
    pip install pynisher==0.4.2 && \
    pip install pyrfr==0.7.4 && \
    pip install smac==0.8 && \
    ln -s locale.h /usr/include/xlocale.h && \
    cd /src/xgboost; make -j4 && \
    cd /src/xgboost/python-package && \
    python3 setup.py install && \
    pip install auto-sklearn && \
    rm /usr/include/xlocale.h && \
    rm -r /root/.cache && \
    rm -rf /src && \
    apk del .build-dependencies
