FROM python:3.6.8-alpine3.8

RUN apk add --update --no-cache \
    --virtual=.build-dependencies \
    make gfortran gcc musl-dev linux-headers swig \
    python3-dev \
    py-setuptools g++ && \
    apk add --no-cache openblas lapack-dev libexecinfo-dev libstdc++ libgomp && \
    pip install setuptools && \
    pip install numpy==1.15.4 && \
    pip install scipy==1.2.0 && \
    pip install psutil && \
    pip install pynisher==0.4.2 && \
    pip install ConfigSpace && \
    pip install pandas==0.23.4 scikit-learn && \
    pip install pyrfr==0.8.0 && \
    pip install sobol_seq && \
    pip install joblib && \
    pip install lazy_import && \
    pip install scikit-optimize && \
    pip install emcee && \
    ln -s locale.h /usr/include/xlocale.h && \
    rm /usr/include/xlocale.h && \
    rm -r /root/.cache && \
    rm -rf /src && \
    apk del .build-dependencies
