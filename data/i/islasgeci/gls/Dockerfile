FROM islasgeci/jupyter:8e52
# Instala paquetes
RUN conda install --quiet --yes \
    'r-ncdf4' && \
    conda clean --all -f -y && \
    fix-permissions $CONDA_DIR
RUN R -e "devtools::install_github('benjamin-merkel/probGLS')"
CMD ["bash", "-c", "umask 000 && bash"]
