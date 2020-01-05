
FROM c3h3/oblas-py278

RUN pip install cython==0.19

RUN git clone -q --branch=v1.8.2 https://github.com/numpy/numpy.git /tmp/numpy
ADD numpy-site.cfg /tmp/numpy/site.cfg 
RUN cd /tmp/numpy && python setup.py config && python setup.py build && python setup.py install

#RUN wget https://gist.github.com/raw/3842524/df01f7fa9d849bec353d6ab03eae0c1ee68f1538/test_numpy.py
#RUN OMP_NUM_THREADS=1 python test_numpy.py
#RUN OMP_NUM_THREADS=12 python test_numpy.py

RUN rm -rf /tmp/numpy

RUN git clone -q --branch=v0.14.0 https://github.com/scipy/scipy.git /tmp/scipy
ADD scipy-site.cfg /tmp/scipy/site.cfg
RUN cd /tmp/scipy && python setup.py config && python setup.py build && python setup.py install
RUN rm -rf /tmp/scipy


