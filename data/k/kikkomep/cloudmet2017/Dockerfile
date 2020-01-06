FROM crs4/wft4galaxy-develop:latest

# set the term var
ENV TERM xterm-256color

# tutorial workdir
ENV TUTORIAL_WORKDIR /home/jovyan/work/cm17

# clone the tutorial repository
RUN git clone https://github.com/kikkomep/cm17 ${TUTORIAL_WORKDIR}

# change workdir
WORKDIR ${TUTORIAL_WORKDIR}