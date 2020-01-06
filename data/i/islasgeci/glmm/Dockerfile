FROM islasgeci/jupyter:8e52
# Instala paquetes de R
RUN conda install --quiet --yes \
    'r-car' \
    'r-emmeans' \
    'r-ggpubr' \
    'r-lme4' \
    'r-mumin' \ 
        && \
    conda clean --all -f -y && \
    fix-permissions $CONDA_DIR
CMD ["bash", "-c", "umask 000 && bash"]
