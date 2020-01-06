FROM xkumiyu/python-base
MAINTAINER xkumiyu <xkumiyu@gmail.com>

# update Ubutnu
RUN apt-get update -y

# install Python Packege
RUN apt-get install -y python-numpy --no-install-recommends
RUN apt-get install -y python-scipy --no-install-recommends
RUN apt-get install -y python-matplotlib --no-install-recommends
RUN apt-get install -y ipython --no-install-recommends
RUN apt-get install -y ipython-notebook --no-install-recommends
RUN apt-get install -y python-pandas --no-install-recommends
RUN apt-get install -y python-sympy --no-install-recommends
RUN apt-get install -y python-nose --no-install-recommends

# clean Ubuntu
RUN rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*
RUN apt-get clean

# setup ipython notebook
EXPOSE 8888
VOLUME /notebook
WORKDIR /notebook

ADD notebook.sh /
RUN chmod u+x /notebook.sh

# exec ipython notebook
CMD /notebook.sh



# # install scikit-learn
# RUN pip install scikit-learn

# # install rpy2
# RUN apt-get install -y libreadline-dev r-base --no-install-recommends
# RUN pip install rpy2

# # install Graphviz
# RUN apt-get install -y graphviz graphviz-dev --no-install-recommends
# RUN pip install pydot

# # install ipython, notebook
# # RUN apt-get install -y ipython --no-install-recommends
# RUN pip install pyzmq
# RUN pip install jinja2
# RUN pip install tornado
# RUN pip install ipython[notebook]
