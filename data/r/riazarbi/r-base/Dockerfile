# Lock to a particular Ubuntu image
ARG BASE_CONTAINER=ubuntu:bionic-20190612@sha256:9b1702dcfe32c873a770a32cfd306dd7fc1c4fd134adfb783db68defc8894b3c
FROM $BASE_CONTAINER

LABEL authors="Riaz Arbi,Gordon Inggs"

# BASE ==========================================
# Let's make it a bit more functional
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get clean && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get update && \
    apt-get install -y \
    vim \
    nano \
    htop \
    bash \
    cmake \
    make \
    gcc \
    wget \
    apt-utils \
    git \
    sudo \
    locales \
    dnsutils \
    curl \
    screen \
    python3 \
    python3-pip \
# Jupyter-specific
 && apt-get update \
 && apt-get install -yq --no-install-recommends \
    wget \
    bzip2 \
    ca-certificates \
    sudo \
    locales \
    fonts-liberation \
    npm \
    libffi-dev \
# R-specific
    libapparmor1 \
    libedit2 \
    lsb-release \
    psmisc \
    libssl1.0.0 \
    gnupg \
    apt-transport-https \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Set the timezone
ENV TZ="Africa/Johannesburg"
RUN echo $TZ > /etc/timezone \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y tzdata \
 && rm /etc/localtime \
 && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
 && dpkg-reconfigure -f noninteractive tzdata \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Define en_ZA
RUN DEBIAN_FRONTEND=noninteractive \
    locale-gen en_ZA && \
    locale-gen en_ZA.UTF-8 && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale

ENV LANGUAGE en_ZA.UTF-8
ENV LANG en_ZA.UTF-8
ENV LC_ALL en_ZA.UTF-8
ENV LC_CTYPE en_ZA.UTF-8
ENV LC_MESSAGES en_ZA.UTF-8

# DRIVERS =======================================================
# JAVA
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && \
    apt-get install -y \
    default-jre \
    default-jdk \
# ODBC
    gnupg2 \
    unixodbc-dev \
    unixodbc-bin \
    unixodbc \
    libaio1 \
    alien \
# Microsoft driver
# && wget https://packages.microsoft.com/keys/microsoft.asc -O microsoft.asc && \
#    apt-key add microsoft.asc && \
#    wget https://packages.microsoft.com/config/ubuntu/18.04/prod.list -O prod.list && \
#    cp prod.list /etc/apt/sources.list.d/mssql-release.list && \
#    apt-get update && \
#    ACCEPT_EULA=Y apt-get install -y \
#    msodbcsql17 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Note: we've dropped Selenium because a better pattern is deploying a sidecar Selenium container

# Oracle driver
RUN wget -q https://github.com/cityofcapetown/docker_datascience/raw/master/base/drivers/oracle-instantclient18.3-basic-18.3.0.0.0-1.x86_64.rpm \
 && wget -q https://github.com/cityofcapetown/docker_datascience/raw/master/base/drivers/oracle-instantclient18.3-odbc-18.3.0.0.0-1.x86_64.rpm \ 
 && alien -i oracle-instantclient18.3-basic-18.3.0.0.0-1.x86_64.rpm \
 && alien -i oracle-instantclient18.3-odbc-18.3.0.0.0-1.x86_64.rpm \
 && rm oracle-instantclient18.3-basic-18.3.0.0.0-1.x86_64.rpm \
 && rm oracle-instantclient18.3-odbc-18.3.0.0.0-1.x86_64.rpm

ENV LD_LIBRARY_PATH /usr/lib/oracle/18.3/client64/lib/${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
RUN ldconfig

RUN echo "[Oracle Driver 18.3]\nDescription=Oracle Unicode driver\nDriver=/usr/lib/oracle/18.3/client64/lib/libsqora.so.18.1\nUsageCount=1\nFileUsage=1" \
  >> /etc/odbcinst.ini

# ODBC
EXPOSE 1433

# PYTHON ======================================================================
# Infrastructure-dependent prerequisites
RUN python3 -m pip install --upgrade pip setuptools wheel \
 && python3 -m pip install minio \
 && python3 -m pip install pyhdb \
 && python3 -m pip install pandas \
 && python3 -m pip install pyarrow \
 && python3 -m pip install python-magic

# JUPYTER =====================================================================

# Create same user as jupyter docker stacks so that k8s will run fine
ARG NB_USER="jovyan"
ARG NB_UID="1000"
ARG NB_GID="100"

RUN apt-get update && apt-get install -yq --no-install-recommends \
    npm nodejs
# Install all the jupyter packages
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install jupyter jupyterhub jupyterlab \
 && python3 -m pip install nbgitpuller
#    jupyter labextension install @jupyter-widgets/jupyterlab-manager && \
#    jupyter labextension install @jupyterlab/git && \
#    python3 -m pip install jupyterlab-git && \
#    jupyter serverextension enable --py jupyterlab_git --sys-prefix && \
#    python3 -m pip install ipyleaflet && \
#    jupyter nbextension enable --py --sys-prefix ipyleaflet && \
#    jupyter nbextension enable --py widgetsnbextension && \
#    jupyter labextension install jupyter-leaflet && \
#    python3 -m pip install ipympl && \
#    jupyter labextension install jupyter-matplotlib

# Configure environment
ENV SHELL=/bin/bash \
    NB_USER=$NB_USER \
    NB_UID=$NB_UID \
    NB_GID=$NB_GID \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8
ENV HOME=/home/$NB_USER

# Add a script that we will use to correct permissions after running certain commands
ADD fix-permissions /usr/local/bin/fix-permissions
RUN chmod +x /usr/local/bin/fix-permissions

# Enable prompt color in the skeleton .bashrc before creating the default NB_USER
RUN sed -i 's/^#force_color_prompt=yes/force_color_prompt=yes/' /etc/skel/.bashrc

# Create NB_USER with name jovyan user with UID=1000 and in the 'users' group
# and make sure these dirs are writable by the `users` group.
RUN echo "auth requisite pam_deny.so" >> /etc/pam.d/su && \
    sed -i.bak -e 's/^%admin/#%admin/' /etc/sudoers && \
    sed -i.bak -e 's/^%sudo/#%sudo/' /etc/sudoers && \
    useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    chmod g+w /etc/passwd 
RUN /usr/local/bin/fix-permissions $HOME

USER $NB_UID
WORKDIR $HOME

# Clean npm cache, create a new jupyter notebook config
RUN npm cache clean --force && \
    jupyter notebook --generate-config && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    fix-permissions /home/$NB_USER

# Expose the right port
EXPOSE 8888

# Configure container startup
CMD ["/bin/bash", "start-notebook.sh"]

# Add local files as late as possible to avoid cache busting
COPY start.sh /usr/local/bin/
COPY start-notebook.sh /usr/local/bin/
COPY start-singleuser.sh /usr/local/bin/
COPY jupyter_notebook_config.py /etc/jupyter/

# Fix permissions on /etc/jupyter as root
USER root
RUN fix-permissions /etc/jupyter/

# RSESSION ==================================================================

# Install R and RStudio
ENV RSTUDIO_VERSION 1.2.5001

# Add apt gpg key
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E298A3A825C0D65DFD57CBB651716619E084DAB9 \
 && gpg -a --export E298A3A825C0D65DFD57CBB651716619E084DAB9 | sudo apt-key add - \
 && echo deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/ >> /etc/apt/sources.list \
 && echo deb http://za.archive.ubuntu.com/ubuntu/ bionic-backports main restricted universe >> /etc/apt/sources.list \
# Install prerequisites
 && DEBIAN_FRONTEND=noninteractive \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    gfortran \
    libclang-dev \
    r-base \
    r-recommended \
    r-base-dev \
    gdebi-core \
# Install RStudio
 && wget --quiet https://download2.rstudio.org/server/bionic/amd64/rstudio-server-${RSTUDIO_VERSION}-amd64.deb \
 && gdebi -n rstudio-server-${RSTUDIO_VERSION}-amd64.deb \ 
 && rm rstudio-server-${RSTUDIO_VERSION}-amd64.deb 
# Install Shiny Server
RUN wget -q "https://download3.rstudio.org/ubuntu-14.04/x86_64/shiny-server-1.5.9.923-amd64.deb" -O ss-latest.deb \
 && gdebi -n ss-latest.deb \
 && rm -f ss-latest.deb 
#    Install R package dependencies
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    libxml2-dev \
#    libssl-dev \
    libssh2-1-dev \
    libgit2-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* 
#   Note we use install2r because it halts build it package install fails. 
#   This is silent with install.packages(). Also multicore is nice.

RUN Rscript -e 'install.packages(c("littler", "docopt"))' \ 
 && ln -s /usr/local/lib/R/site-library/littler/examples/install2.r /usr/local/bin/install2.r \
 && ln -s /usr/local/lib/R/site-library/littler/examples/installGithub.r /usr/local/bin/installGithub.r \
 && ln -s /usr/local/lib/R/site-library/littler/bin/r /usr/local/bin/r \
# Install jupyter R kernel
 && install2.r -e -n 3 -s --deps TRUE \
 devtools \
 shiny \ 
 rmarkdown \
 knitr \
 RJDBC

# Jupyter-rsession
RUN R -e "install.packages('IRkernel')" \
 && R --quiet -e "IRkernel::installspec(user=FALSE)"
# && python3 -m pip install git+https://github.com/jupyterhub/jupyter-server-proxy \
# && python3 -m pip install git+https://github.com/jupyterhub/jupyter-rsession-proxy 
RUN python3 -m pip install jupyter-server-proxy \
  && python3 -m pip install jupyter-rsession-proxy
RUN /usr/local/bin/fix-permissions $HOME

# Run as NB_USER ============================================================

USER $NB_USER
ENV PATH="${PATH}:/usr/lib/rstudio-server/bin"
