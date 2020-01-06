FROM ubuntu:bionic

# Set PlantUML version for download
ENV PLANTUML_VERSION=1.2019.9

# Install required packages to install MiKTeX, graphviz, tex-gyre and required packages install PlantUML
RUN apt-get update && apt-get install -y --no-install-recommends \
        apt-transport-https \
        ca-certificates \
        dirmngr \
        ghostscript \
        gnupg \
        gosu \
        make \
        perl \
        tex-gyre \
        graphviz \
        openjdk-11-jre-headless \
        curl \
        git

# Install PlantUML
RUN mkdir -p /app \
    && curl -L https://sourceforge.net/projects/plantuml/files/plantuml.${PLANTUML_VERSION}.jar/download -o /app/plantuml.jar

# Refresh font cache (for tex-gyre)
# See https://tex.stackexchange.com/a/88424
RUN fc-cache

# Add MiKTeX repo
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys D6BC243565B2087BC3F897C9277A7293F59E4889
RUN echo "deb http://miktex.org/download/ubuntu bionic universe" | tee /etc/apt/sources.list.d/miktex.list

# Install MiKTeX
RUN apt-get update && apt-get install -y --no-install-recommends miktex
RUN miktexsetup finish \
    && initexmf --admin --set-config-value=[MPM]AutoInstall=1 \
    && mpm --admin --update-db \
    && mpm --admin \
        --install amsfonts \
        --install biber-linux-x86_64 \
        --install tex-gyre \
        --install tex-gyre-math \
    && initexmf --admin --update-fndb

# Install udhbwvst
# See https://tex.stackexchange.com/a/69484
RUN mkdir -p /tmp/dhbw-vs-latex-template \
    && git clone https://github.com/skyfrk/dhbw-vs-latex-template /tmp/dhbw-vs-latex-template \
    && mkdir -p /localtexmf/tex/latex/udhbwvst \
    && cp -r /tmp/dhbw-vs-latex-template/src/udhbwvst* /localtexmf/tex/latex/udhbwvst/ \
    && rm -rf /tmp/dhbw-vs-latex-template \
    && initexmf --admin --register-root=/localtexmf \
    && initexmf --admin --update-fndb

# Add entrypoint script to create miktex user in case MIKTEX_UID is set
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

ENV MIKTEX_USERCONFIG=/miktex/.miktex/texmfs/config
ENV MIKTEX_USERDATA=/miktex/.miktex/texmfs/data
ENV MIKTEX_USERINSTALL=/miktex/.miktex/texmfs/install
ENV PLANTUML_JAR=/app/plantuml.jar
ENV GRAPHVIZ_DOT=/usr/bin/dot

WORKDIR /miktex/work

CMD ["bash"]
