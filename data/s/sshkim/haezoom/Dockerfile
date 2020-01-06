FROM lambci/lambda:build-python3.6

RUN rm /var/runtime/awslambda/runtime.cpython-36m-x86_64-linux-gnu.so
COPY runtime-mock.py /var/runtime/awslambda/runtime.py

RUN pip install setuptools==39.0.1
