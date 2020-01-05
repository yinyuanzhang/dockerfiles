FROM ubuntu:trusty

# Install prereqs
RUN apt-get update -qq && apt-get install -yq --no-install-recommends \
    apt-utils ca-certificates unzip xorg wget xvfb \
    bc libgomp1 libxmu6 libxt6 tcsh tar \
    ghostscript libgs-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && chmod 777 /opt && chmod a+s /opt

# Install packages required by dax
RUN apt-get update && apt-get install -yq \
    python-pip libfreetype6-dev pkg-config libxml2-dev libxslt1-dev \
    python-dev zlib1g-dev python-numpy python-scipy python-requests \
    python-urllib3 python-pandas
RUN pip install pandas matplotlib seaborn --upgrade

# Install dax 
RUN pip install dax==0.8.0

# Install FreeSurfer with minimal files
RUN wget -qO- https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.1/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.1.tar.gz | tar zxv -C /opt \
    --exclude='freesurfer/average' \
    --exclude='freesurfer/diffusion' \
    --exclude='freesurfer/docs' \
    --exclude='freesurfer/fsfast' \
    --exclude='freesurfer/fsafd' \
    --exclude='freesurfer/subjects' \
    --exclude='freesurfer/trctrain' \
    --exclude='freesurfer/matlab' \
    --exclude='freesurfer/tktools' \
    --exclude='freesurfer/mni' \
    --exclude='freesurfer/data' \
    --exclude='freesurfer/bin/dmri*' \
    --exclude='freesurfer/bin/gcam*' \
    --exclude='freesurfer/bin/kvl*' \
    --exclude='freesurfer/lib/cuda' \
    --exclude='freesurfer/lib/tcl' \
    --exclude='freesurfer/lib/vtk' \
    --exclude='freesurfer/lib/KWWidgets' \
    --exclude='freesurfer/lib/tcltktixblt' \
    --exclude='freesurfer/lib/images' \
    --exclude='freesurfer/lib/petsc' \
    --exclude='freesurfer/lib/qt' && \
    rm /opt/freesurfer/bin/mris_* /opt/freesurfer/bin/[a-eg-ln-z]* /opt/freesurfer/bin/freeview*

# Configure environment
ENV FSLOUTPUTTYPE=NIFTI_GZ
ENV FSLMULTIFILEQUIT=TRUE
ENV OS Linux
ENV FS_OVERRIDE 0
ENV SUBJECTS_DIR /opt/freesurfer/subjects
ENV FSF_OUTPUT_FORMAT nii.gz
ENV FREESURFER_HOME /opt/freesurfer
ENV PATH=$PATH:/opt/freesurfer/bin:/usr/local/bin:/usr/bin:/bin
ENV PYTHONPATH=""
ENV FS_LICENSE=/opt/license.txt
RUN touch /opt/license.txt

# Make sure other stuff is in path
COPY src /opt/src/
RUN chmod +x /opt/src/proc.sh
RUN chmod +x /opt/src/mcflirt
ENV PATH=/opt/src:$PATH

# Make directories for I/O to bind
RUN mkdir /INPUTS /OUTPUTS

# Get the main code
COPY main.py /opt/main.py
ENTRYPOINT ["python", "/opt/main.py"]
