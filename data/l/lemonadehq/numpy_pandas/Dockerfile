FROM jjanzic/docker-python3-opencv

RUN apt-get update \
    && apt-get install -y libffi-dev git openssh-client \
    && rm -rf /var/lib/apt/lists/*

ENV NUMPY_VERSION 1.16.0
ENV PANDAS_VERSION 0.24.0

RUN pip install numpy==${NUMPY_VERSION}
RUN pip install pandas==${PANDAS_VERSION}
RUN pip install scikit-learn==0.20.2
RUN pip install scipy==1.2.0
