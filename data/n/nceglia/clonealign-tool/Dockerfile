FROM nceglia/base-r-scrna:latest

MAINTAINER Nicholas Ceglia <nickceglia@gmail.com>

RUN pip install tensorflow

COPY run_clonealign.R /codebase/run_clonealign.R

CMD ["/bin/bash"]
