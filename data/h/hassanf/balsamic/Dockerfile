FROM hassanf/miniconda3_4.6.14:latest

LABEL maintainer="Hassan Foroughi hassan dot foroughi at scilifelab dot se" 
LABEL description="Bioinformatic analysis pipeline for somatic mutations in cancer"
LABEL version="4.1.0"

# create necessary directories
# install balsamic and it's environments
# symlink libreadline for picard to function properly 
# install vcfmerge
RUN mkdir -p /git_repos; \
    export PATH=/usr/local/miniconda/bin:$PATH; \
    export LC_ALL=en_US.utf-8; \
    export LANG=en_US.utf-8; \
    cd /git_repos && git clone https://github.com/Clinical-Genomics/BALSAMIC && cd BALSAMIC && git checkout master; \
    conda env create --file BALSAMIC/conda/BALSAMIC-py27.yaml -n BALSAMIC_py27 \
    && conda env create --file BALSAMIC/conda/BALSAMIC-py36.yaml -n BALSAMIC_py36 \
    && conda env create --file BALSAMIC/conda/BALSAMIC-vcfmerge.yaml -n BALSAMIC_vcfmerge; \
    source activate BALSAMIC_py36; \
    gatk3-register BALSAMIC/assets/GenomeAnalysisTK.jar; \
    picard_PATH=BALSAMIC/assets/picard-2.18.11-3-gc6e797f-SNAPSHOT-all.jar; \
    picard_destination=/usr/local/miniconda/envs/BALSAMIC_py36/share/; \
    cp $picard_PATH ${picard_destination}; \
    ln -s ${picard_destination}/picard-2.18.11-3-gc6e797f-SNAPSHOT-all.jar  ${picard_destination}/picard-2.18.11.jar; \
    ln -s /usr/local/miniconda/envs/BALSAMIC_py36/lib/libreadline.so.7.0 /usr/local/miniconda/envs/BALSAMIC_py36/lib/libreadline.so.6; \
    ln -s /usr/local/miniconda/envs/BALSAMIC_py36/lib/libreadline.so.7.0 /usr/local/miniconda/envs/BALSAMIC_py36/lib/libreadline.so.6.0; \
    cd /git_repos && git clone https://github.com/hassanfa/VCFmerge.git && cd VCFmerge; \
    source activate BALSAMIC_vcfmerge \
    && pip install --no-cache-dir -r requirements-dev.txt -r requirements.txt -e . \
    && conda clean -all -y

# The following fixes the error for Click
# RuntimeError: Click will abort further execution because Python 3 was
# configured to use ASCII as encoding for the environment. Consult
# https://click.palletsprojects.com/en/7.x/python3/ for mitigation steps.
ENV LC_ALL=en_US.utf-8
ENV LANG=en_US.utf-8
ENV PATH="/usr/local/miniconda/bin:${PATH}"
