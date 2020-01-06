FROM continuumio/anaconda
RUN apt-get update && apt-get install -y graphviz build-essential unzip && rm -Rf /var/cache/apt
RUN pip install shapely matplotlib numpy pandas geopandas sympy ortools scipy cma pybrain gprof2dot pylint
RUN mkdir -p /root/.config/matplotlib/ && sh -c 'echo "backend: agg" > /root/.config/matplotlib/matplotlibrc'
