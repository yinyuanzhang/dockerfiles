FROM quay.io/bgruening/galaxy:latest
MAINTAINER Fabiano Menegidio <fabiano.menegidio@biology.bio.br>

ENV GALAXY_CONFIG_BRAND="Triffid Flavour"
ENV GALAXY_CONFIG_CONDA_AUTO_INSTALL=True
ENV GALAXY_CONFIG_CONDA_AUTO_INIT=True

ADD config/triffid_0.yaml $GALAXY_ROOT/tools_0.yaml
ADD config/triffid_1.yaml $GALAXY_ROOT/tools_1.yaml
ADD config/triffid_2.yaml $GALAXY_ROOT/tools_2.yaml
ADD config/triffid_3.yaml $GALAXY_ROOT/tools_3.yaml
ADD config/triffid_4.yaml $GALAXY_ROOT/tools_4.yaml
ADD config/triffid_5.yaml $GALAXY_ROOT/tools_5.yaml
ADD config/triffid_6.yaml $GALAXY_ROOT/tools_6.yaml
ADD config/triffid_7.yaml $GALAXY_ROOT/tools_7.yaml
ADD config/triffid_8.yaml $GALAXY_ROOT/tools_8.yaml
ADD config/triffid_9.yaml $GALAXY_ROOT/tools_9.yaml
ADD config/tool_conf.xml $GALAXY_ROOT/config/
ADD config/dependency_resolvers_conf.xml $GALAXY_ROOT/config/

RUN df -h \
    && install-tools $GALAXY_ROOT/tools_0.yaml \
    && /tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null \
    && rm /export/galaxy-central/ -rf \
    && df -h
    
RUN df -h \
    && install-tools $GALAXY_ROOT/tools_1.yaml \
    && /tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null \
    && rm /export/galaxy-central/ -rf \
    && df -h
    
RUN df -h \
    && install-tools $GALAXY_ROOT/tools_2.yaml \
    && /tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null \
    && rm /export/galaxy-central/ -rf \
    && df -h

RUN df -h \
    && install-tools $GALAXY_ROOT/tools_3.yaml \
    && /tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null \
    && rm /export/galaxy-central/ -rf \
    && df -h
    
RUN df -h \
    && install-tools $GALAXY_ROOT/tools_4.yaml \
    && /tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null \
    && rm /export/galaxy-central/ -rf \
    && df -h
    
RUN df -h \
    && install-tools $GALAXY_ROOT/tools_5.yaml \
    && /tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null \
    && rm /export/galaxy-central/ -rf \
    && df -h
    
RUN df -h \
    && install-tools $GALAXY_ROOT/tools_6.yaml \
    && /tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null \
    && rm /export/galaxy-central/ -rf \
    && df -h
    
RUN df -h \
    && install-tools $GALAXY_ROOT/tools_7.yaml \
    && /tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null \
    && rm /export/galaxy-central/ -rf \
    && df -h

RUN df -h \
    && install-tools $GALAXY_ROOT/tools_8.yaml \
    && /tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null \
    && rm /export/galaxy-central/ -rf \
    && df -h

RUN df -h \
    && install-tools $GALAXY_ROOT/tools_9.yaml \
    && /tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null \
    && rm /export/galaxy-central/ -rf \
    && df -h

VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy)
EXPOSE :80
EXPOSE :21
EXPOSE :22
EXPOSE :8800

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
