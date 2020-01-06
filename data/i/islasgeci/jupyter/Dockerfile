FROM jupyter/r-notebook:ad3574d3c5c7
USER root

# Define variables de entorno
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONIOENCODING=utf-8
ENV QT_QPA_PLATFORM=offscreen
ENV TZ=US/Pacific

# Instala paquetes en el sistema operativo
RUN apt-get update && apt-get install --yes apt-utils && apt-get dist-upgrade --yes
RUN apt-get install --yes --no-install-recommends \
    csvkit \
    curl \
    git \
    gnumeric \
    jq \
    make \
    texlive-full \
    texlive-lang-spanish \
    texlive-science \
        && \
    apt clean

# Instala modulos con conda
RUN conda install --quiet --yes \
    'cartopy' \
    'goodtables' \
    'pandas' \
    'utm' \
        && \
    conda clean --all -f -y && \
    fix-permissions $CONDA_DIR

# Instala pythontex
RUN curl -L http://mirrors.ctan.org/macros/latex/contrib/pythontex.zip --output /tmp/pythontex.zip && \
    unzip /tmp/pythontex.zip -d /tmp && \
    cd /tmp/pythontex && \
    latex pythontex.ins && \
    mkdir ~/texmf/tex --parents && \
    mv * ~/texmf/tex && \
    chmod +x ~/texmf/tex/pythontex.py && \
    ln --symbolic ~/texmf/tex/pythontex.py /usr/local/bin/pythontex

# Define directorio de trabajo
WORKDIR /workdir

# Inicia `jupyter lab` después de agregar permisos de escritura y ejecución para todos
CMD ["bash", "-c", "umask 000 && jupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.token=''"]
