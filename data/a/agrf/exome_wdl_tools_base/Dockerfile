FROM alexiswl/alpine_conda:4.7.12.1

# Set path
ENV PATH=/opt/conda/bin:$PATH

# Help reduce the size of the dockerfile
# See here for more info: https://jcrist.github.io/conda-docker-tips.html
ENV PYTHONDONTWRITEBYTECODE=true

# Install git, pandas
RUN conda install --channel anaconda --freeze-installed --yes \
      git=2.20.1 pandas=0.25.1 \
      numpy=1.17.2

# Install all the other things that are required.
RUN conda install --channel conda-forge --freeze-installed --yes \
	scikit-allel=1.2.1 rsync=3.1.3

# Clean up image
RUN conda clean --all --force-pkgs-dirs --yes

# Delete static, javascript libraries
RUN find /opt/conda/ -follow -type f -name '*.a' -delete \
  && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
  && find /opt/conda/ -follow -type f -name '*.js.map' -delete \
  && find /opt/conda/lib/python*/site-packages/bokeh/server/static -follow -type f -name '*.js' ! -name '*.min.js' -delete

