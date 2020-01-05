FROM python:2-stretch
MAINTAINER Jacopo Mauro

# install required python packages
RUN apt-get update &&\
	apt-get -y install \
	    # for gecode
	    libgl1 \
		# for fzn2smt
	    openjdk-8-jdk-headless && \
	rm -rf /var/lib/apt/lists/* && \
    pip install \
	    antlr4-python2-runtime \
	    psutil \
	    click

# minizinc + gecode + chuffed
COPY --from=jacopomauro/minizinc:v2.2.1 /tool/MiniZincIDE /tool/MiniZincIDE
ENV PATH "$PATH:/tool/MiniZincIDE/bin"
ENV LD_LIBRARY_PATH "$LD_LIBRARY_PATH:/tool/MiniZincIDE/lib"

# z3 solver
COPY --from=jacopomauro/z3:v4.8.0 /tool/z3 /tool/z3
ENV PYTHONPATH "$PYTHONPATH:/tool/z3/install/lib/python-2/site-packages"
ENV PATH "$PATH:/tool/z3/install/bin"

# fzn2smt
COPY --from=jacopomauro/fzn2smt:v2.0.2 /tool/fzn2smt /tool/fzn2smt
ENV CLASSPATH "$CLASSPATH:/tool/fzn2smt:/tool/fzn2smt/antlr-runtime-3.2.jar"

# or-tools
COPY --from=jacopomauro/or-tools:v6.9.1 /tool/or-tools /tool/or-tools
ENV PATH "$PATH:/tool/or-tools/bin"
RUN ln -s /tool/or-tools/ortools/flatzinc/mznlib_sat /tool/MiniZincIDE/share/minizinc/or-tools


# download and install zephyurs2
RUN cd /tool && \
  git clone --depth=1 https://jacopomauro@bitbucket.org/jacopomauro/zephyrus2.git && \
  pip install -e /tool/zephyrus2


EXPOSE 9001
WORKDIR /tool/zephyrus2/zephyrus2
CMD ["python", "server.py"]


