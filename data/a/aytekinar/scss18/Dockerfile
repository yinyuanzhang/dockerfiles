FROM jupyterhub/singleuser AS julia
USER root:root
WORKDIR /
RUN wget https://julialang-s3.julialang.org/bin/linux/x64/1.0/julia-1.0.1-linux-x86_64.tar.gz
RUN tar xvzf julia-1.0.1-linux-x86_64.tar.gz
RUN mv julia-1.0.1/ /opt/julia

FROM jupyterhub/singleuser AS mlpackages
RUN pip install --upgrade --no-cache-dir jupyterlab keras matplotlib numpy scikit-learn pandas
RUN jupyter labextension install @jupyterlab/hub-extension

FROM jupyterhub/singleuser
COPY --from=julia /opt/julia /opt/julia
COPY --from=mlpackages /opt/conda /opt/conda
RUN /opt/julia/bin/julia --eval 'using Pkg; pkg"add IJulia"; pkg"precompile"; pkg"gc"'
