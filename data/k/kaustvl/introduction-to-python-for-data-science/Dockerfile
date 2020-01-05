FROM continuumio/miniconda3:4.7.10

LABEL maintainer="david.pugh@kaust.edu.sa"

SHELL [ "/bin/bash", "-c" ]

# Update conda as root
RUN conda update --name base --channel defaults --yes conda

# Create a non-root user
ENV USER al-khawarizmi
ENV HOME /home/$USER

RUN adduser --disabled-password \
    --gecos "Non-root user" \
    --uid 1000 \
    --gid 100 \
    --home $HOME \
    $USER

# Create conda environment as non-root user 
USER $USER
RUN mkdir $HOME/app
WORKDIR $HOME/app

# Build the specified conda environment from an environment file
COPY --chown=1000:100 environment.yml /usr/tmp/environment.yml
RUN conda env create --prefix ./env --file /usr/tmp/environment.yml && \
    conda clean --all --force-pkgs-dir --yes && \
    conda init bash

# Use an entrypoint script to insure conda environment is properly activated at runtime
COPY --chown=1000:100 docker/entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.sh" ]

# default command will be to launch JupyterLab server for development
EXPOSE 8888
CMD [ "jupyter", "lab", "--no-browser", "--ip", "0.0.0.0" ]
