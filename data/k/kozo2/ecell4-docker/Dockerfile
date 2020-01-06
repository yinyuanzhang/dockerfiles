FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y g++ python-dev libboost-dev libgsl0-dev libhdf5-serial-dev pkg-config cython python-pip git libboost-test-dev python-zmq python-matplotlib
RUN pip install ipython jinja2 tornado
RUN cd /tmp; git clone git://github.com/ecell/ecell4
RUN cd /tmp/ecell4; git checkout -t origin/rulebase; PREFIX=/usr/local PYTHONPATH=/usr/local/lib/python2.7/dist-packages bash /tmp/ecell4/install.sh core core_python gillespie gillespie_python ode ode_python lattice lattice_python util_python bd bd_python
EXPOSE 8888
CMD LD_LIBRARY_PATH=/usr/local/lib ipython notebook --notebook-dir='/tmp/ecell4/ipynb' --no-browser --ip='*' --port 8888
