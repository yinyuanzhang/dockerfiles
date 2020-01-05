# Docker image with all necessary Homebrew and Ensembl taps, and the basic dependencies
FROM muffato/ensembl-linuxbrew-basic-dependencies

# Clone the Ensembl repos
ARG ENSEMBL_INSTALL_DIR=/home/linuxbrew/repos
RUN mkdir -p $ENSEMBL_INSTALL_DIR \
    && git clone --depth 1 https://github.com/Ensembl/ensembl.git $ENSEMBL_INSTALL_DIR/ensembl \
    && git clone --depth 1 https://github.com/Ensembl/ensembl-io.git $ENSEMBL_INSTALL_DIR/ensembl-io \
    && git clone --depth 1 https://github.com/Ensembl/ensembl-compara.git $ENSEMBL_INSTALL_DIR/ensembl-compara \
    && git clone --depth 1 https://github.com/Ensembl/ensembl-test.git $ENSEMBL_INSTALL_DIR/ensembl-test \
    && git clone --depth 1 https://github.com/Ensembl/ensembl-hive.git $ENSEMBL_INSTALL_DIR/ensembl-hive \
    && git clone --depth 1 https://github.com/Ensembl/ensembl-hive-docker-swarm.git $ENSEMBL_INSTALL_DIR/ensembl-hive-docker-swarm \
    && git clone --branch dev/hive_master --depth 1 https://github.com/Ensembl/ensembl-analysis.git $ENSEMBL_INSTALL_DIR/ensembl-analysis \
    && git clone --branch v1.6.x --depth 1 https://github.com/bioperl/bioperl-live $ENSEMBL_INSTALL_DIR/bioperl-live \
    && git clone --branch release-1-6-9 --depth 1 https://github.com/bioperl/bioperl-run $ENSEMBL_INSTALL_DIR/bioperl-run

# Install the system dependencies via brew
RUN brew install curl sqlite3 graphviz cpanminus \
 && brew cleanup \
 && rm -rf /home/linuxbrew/.cache/Homebrew

# Install the Perl dependencies (CPAN)
RUN cpanm --installdeps --with-recommends --notest $ENSEMBL_INSTALL_DIR/ensembl \
 && cpanm --installdeps --with-recommends --notest $ENSEMBL_INSTALL_DIR/ensembl-compara \
 && cpanm --installdeps --with-recommends --notest $ENSEMBL_INSTALL_DIR/ensembl-test \
 && cpanm --installdeps --with-recommends --notest $ENSEMBL_INSTALL_DIR/ensembl-hive \
 && rm -rf /home/linuxbrew/.cpan /home/linuxbrew/.cpanm

# Install the Python dependencies
RUN pip install --user -r https://raw.githubusercontent.com/Ensembl/python-requirements/master/compara/requirements.txt \
 && rm -rf /home/linuxbrew/.cache/pip

RUN ln -sf Blast.pm.example   $ENSEMBL_INSTALL_DIR/ensembl-analysis/modules/Bio/EnsEMBL/Analysis/Config/Blast.pm \
 && ln -sf Compara.pm.example $ENSEMBL_INSTALL_DIR/ensembl-analysis/modules/Bio/EnsEMBL/Analysis/Config/Compara.pm \
 && ln -sf General.pm.example $ENSEMBL_INSTALL_DIR/ensembl-analysis/modules/Bio/EnsEMBL/Analysis/Config/General.pm

COPY --chown=linuxbrew:linuxbrew install_cask.sh $ENSEMBL_INSTALL_DIR/

# Setup the environment
ENV PERL5LIB "$ENSEMBL_INSTALL_DIR/ensembl/modules:$ENSEMBL_INSTALL_DIR/ensembl-io/modules:$ENSEMBL_INSTALL_DIR/ensembl-analysis/modules:$ENSEMBL_INSTALL_DIR/ensembl-compara/modules:$ENSEMBL_INSTALL_DIR/ensembl-test/modules:$ENSEMBL_INSTALL_DIR/ensembl-hive/modules:$ENSEMBL_INSTALL_DIR/bioperl-live:$ENSEMBL_INSTALL_DIR/bioperl-run/lib:$PERL5LIB"
ENV PATH "$ENSEMBL_INSTALL_DIR/ensembl-hive/scripts:$PATH"
ENV EHIVE_ROOT_DIR "$ENSEMBL_INSTALL_DIR/ensembl-hive"
ENV ENSEMBL_CVS_ROOT_DIR "$ENSEMBL_INSTALL_DIR"
ENV LINUXBREW_HOME "/home/linuxbrew/.linuxbrew"

