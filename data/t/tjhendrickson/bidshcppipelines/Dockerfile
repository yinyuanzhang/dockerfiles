# Use Ubuntu 14.04 LTS
FROM ubuntu:trusty-20170119

# Configure environment
ENV OS Linux
ENV FS_OVERRIDE 0
ENV FIX_VERTEX_AREA=
ENV SUBJECTS_DIR /opt/freesurfer/subjects
ENV FSF_OUTPUT_FORMAT nii.gz
ENV MNI_DIR /opt/freesurfer/mni
ENV LOCAL_DIR /opt/freesurfer/local
ENV FREESURFER_HOME /opt/freesurfer
ENV FSFAST_HOME /opt/freesurfer/fsfast
ENV MINC_BIN_DIR /opt/freesurfer/mni/bin
ENV MINC_LIB_DIR /opt/freesurfer/mni/lib
ENV MNI_DATAPATH /opt/freesurfer/mni/data
ENV FMRI_ANALYSIS_DIR /opt/freesurfer/fsfast
ENV PERL5LIB /opt/freesurfer/mni/lib/perl5/5.8.5
ENV MNI_PERL5LIB /opt/freesurfer/mni/lib/perl5/5.8.5
ENV PATH /opt/freesurfer/bin:/opt/freesurfer/fsfast/bin:/opt/freesurfer/tktools:/opt/freesurfer/mni/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH
ENV PYTHONPATH=""
ENV FSL_FIXDIR /opt/fix
ENV FSLDIR=/usr/share/fsl/5.0
ENV FSL_DIR="${FSLDIR}"
ENV FSLOUTPUTTYPE=NIFTI_GZ
ENV PATH=/usr/lib/fsl/5.0:$PATH
ENV FSLMULTIFILEQUIT=TRUE
ENV POSSUMDIR=/usr/share/fsl/5.0
ENV LD_LIBRARY_PATH=/usr/lib/fsl/5.0
ENV FSLTCLSH=/usr/bin/tclsh
ENV FSLWISH=/usr/bin/wish
ENV FSLOUTPUTTYPE=NIFTI_GZ

# Download FreeSurfer
RUN apt-get -y update \
    && apt-get install -y wget && \
    wget -qO- ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/5.3.0-HCP/freesurfer-Linux-centos4_x86_64-stable-pub-v5.3.0-HCP.tar.gz | tar zxv -C /opt \
    --exclude='freesurfer/trctrain' \
    --exclude='freesurfer/subjects/fsaverage_sym' \
    --exclude='freesurfer/subjects/fsaverage3' \
    --exclude='freesurfer/subjects/fsaverage4' \
    --exclude='freesurfer/subjects/fsaverage5' \
    --exclude='freesurfer/subjects/fsaverage6' \
    --exclude='freesurfer/subjects/cvs_avg35' \
    --exclude='freesurfer/subjects/cvs_avg35_inMNI152' \
    --exclude='freesurfer/subjects/bert' \
    --exclude='freesurfer/subjects/V1_average' \
    --exclude='freesurfer/average/mult-comp-cor' \
    --exclude='freesurfer/lib/cuda' \
    --exclude='freesurfer/lib/qt' && \
    apt-get install -y tcsh bc tar libgomp1 perl-modules curl

RUN sed -i -e 's,main *$,main contrib non-free,g' /etc/apt/sources.list.d/neurodebian.sources.list; grep -q 'deb .* multiverse$' /etc/apt/sources.list || sed -i -e 's,universe *$,universe multiverse,g' /etc/apt/sources.list

# Install FSL 5.0.9
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    curl -sSL http://neuro.debian.net/lists/trusty.us-ca.full >> /etc/apt/sources.list.d/neurodebian.sources.list

RUN apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9

RUN apt-get update && \
    apt-get install -y fsl-core=5.0.9-4~nd14.04+1

RUN apt-get build-dep -y gridengine && apt-get update -y

# Install HCP Pipelines v3.27.0
RUN apt-get update \
    && apt-get install -y --no-install-recommends python-numpy && \
    wget https://github.com/Washington-University/Pipelines/archive/v3.27.0.tar.gz -O pipelines.tar.gz && \
    cd /opt/ && \
    mkdir /opt/HCP-Pipelines && \
    tar zxf /pipelines.tar.gz -C /opt/HCP-Pipelines --strip-components=1 && \
    rm /pipelines.tar.gz && \
    wget -qO- https://www.doc.ic.ac.uk/~ecr05/MSM_HOCR_v2/MSM_HOCR_v2-download.tgz | tar xz -C /tmp && \
    mv /tmp/homes/ecr05/MSM_HOCR_v2/Ubuntu /opt/HCP-Pipelines/MSMBinaries && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install FIX
RUN apt-get update && apt-get install -y build-essential libpcre3 libpcre3-dev  fort77 xorg-dev libbz2-dev liblzma-dev libblas-dev gfortran gcc-multilib gobjc++ libreadline-dev bzip2 libcurl4-gnutls-dev default-jdk gdebi

RUN cd /opt && \
    wget http://www.fmrib.ox.ac.uk/~steve/ftp/fix.tar.gz && \
    tar zxvf fix.tar.gz && \
    rm fix.tar.gz
RUN mv /opt/fix* /opt/fix

RUN cd /opt && \
    wget https://cloud.r-project.org/bin/linux/ubuntu/trusty/r-base-core_3.4.4-1trusty0_amd64.deb && \
    wget https://cloud.r-project.org/bin/linux/ubuntu/trusty/r-base-dev_3.4.4-1trusty0_all.deb && \
    gdebi -n r-base-core_3.4.4-1trusty0_amd64.deb && \
    gdebi -n r-base-dev_3.4.4-1trusty0_all.deb && \
    apt-get install -y libssl-dev 

RUN R --vanilla -e "install.packages('coin', repos='http://cran.us.r-project.org', dependencies=TRUE)" -e "install.packages('strucchange', repos='http://cran.us.r-project.org', dependencies=TRUE)" -e "install.packages('https://cran.r-project.org/src/contrib/Archive/party/party_1.0-25.tar.gz', repos=NULL, type='source')" -e "install.packages('https://cran.r-project.org/src/contrib/Archive/kernlab/kernlab_0.9-24.tar.gz', repos=NULL, type='source')" -e "install.packages('ROCR', repos='http://cran.us.r-project.org', dependencies=TRUE)" -e "install.packages('https://cran.r-project.org/src/contrib/Archive/e1071/e1071_1.6-7.tar.gz', repos=NULL, type='source')" -e "install.packages('https://cran.r-project.org/src/contrib/Archive/randomForest/randomForest_4.6-12.tar.gz', repos=NULL, type='source')"

RUN mkdir /tmp/v83 && \
    cp /opt/fix*/compiled/Linux/x86_64/MCRInstaller.zip /tmp/v83 && \
    cd /tmp/v83 && \
    unzip MCRInstaller.zip
RUN  cd /tmp/v83 && ./install -mode silent -agreetolicense yes -destinationFolder /usr/local/R2014a

# Install Connectome Workbench dev version
RUN apt-get update && \
	cd /opt && \
	wget http://brainvis.wustl.edu/workbench/workbench-rh_linux64-dev_latest.zip && \
	unzip workbench-rh_linux64-dev_latest.zip && \
	export PATH=/opt/workbench/bin_rh_linux64:${PATH}

# Ensure Dependencies for PostFix are met
RUN apt-get update
RUN mkdir /tmp/v81 && \
    cd /tmp/v81 && \
    wget http://ssd.mathworks.com/supportfiles/MCR_Runtime/R2013a/MCR_R2013a_glnxa64_installer.zip && \
    unzip MCR_R2013a_glnxa64_installer.zip
RUN  cd /tmp/v81 && ./install -mode silent -agreetolicense yes -destinationFolder /usr/local/R2013a

# Ensure dependencies for MSMAll are met
RUN apt-get update
RUN	mkdir /tmp/v91 && \
	cd /tmp/v91 && \
	wget http://ssd.mathworks.com/supportfiles/downloads/R2016b/deployment_files/R2016b/installers/glnxa64/MCR_R2016b_glnxa64_installer.zip && \
	unzip MCR_R2016b_glnxa64_installer.zip
RUN  cd /tmp/v91 && ./install -mode silent -agreetolicense yes -destinationFolder /usr/local/R2016b


#Create necessary environment variables
RUN echo "cHJpbnRmICJrcnp5c3p0b2YuZ29yZ29sZXdza2lAZ21haWwuY29tXG41MTcyXG4gKkN2dW12RVYzelRmZ1xuRlM1Si8yYzFhZ2c0RVxuIiA+IC9vcHQvZnJlZXN1cmZlci9saWNlbnNlLnR4dAo=" | base64 -d | sh
ENV CARET7DIR=/opt/workbench/bin_rh_linux64
ENV HCPPIPEDIR=/opt/HCP-Pipelines
ENV HCPPIPEDIR_Templates=${HCPPIPEDIR}/global/templates
ENV HCPPIPEDIR_Bin=${HCPPIPEDIR}/global/binaries
ENV HCPPIPEDIR_Config=${HCPPIPEDIR}/global/config
ENV HCPPIPEDIR_PreFS=${HCPPIPEDIR}/PreFreeSurfer/scripts
ENV HCPPIPEDIR_FS=${HCPPIPEDIR}/FreeSurfer/scripts
ENV HCPPIPEDIR_PostFS=${HCPPIPEDIR}/PostFreeSurfer/scripts
ENV HCPPIPEDIR_fMRISurf=${HCPPIPEDIR}/fMRISurface/scripts
ENV HCPPIPEDIR_fMRIVol=${HCPPIPEDIR}/fMRIVolume/scripts
ENV HCPPIPEDIR_tfMRI=${HCPPIPEDIR}/tfMRI/scripts
ENV HCPPIPEDIR_dMRI=${HCPPIPEDIR}/DiffusionPreprocessing/scripts
ENV HCPPIPEDIR_dMRITract=${HCPPIPEDIR}/DiffusionTractography/scripts
ENV HCPPIPEDIR_Global=${HCPPIPEDIR}/global/scripts
ENV HCPPIPEDIR_tfMRIAnalysis=${HCPPIPEDIR}/TaskfMRIAnalysis/scripts
ENV MSMBin=${HCPPIPEDIR}/MSMBinaries
ENV MSMBINDIR=${MSMBin}
ENV MSMCONFIGDIR=${HCPPIPEDIR}/MSMConfig


#make /bids_dir, /output_dir and /fsf_template_dir
RUN mkdir /bids_dir && \
    mkdir /output_dir && \
    mkdir /fsf_template_dir
    
#create 360CortSurf_19Vol_parcel.dlabel.nii
RUN cd / && \
	wget https://github.umn.edu/hendr522/HCPPipelines/blob/master/modified_files/360CortSurf_19Vol_parcel.dlabel.nii

## Install the validator
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get remove -y curl && \
    apt-get install -y nodejs

RUN npm install -g bids-validator@0.26.11

RUN apt-get update && apt-get install -y --no-install-recommends python-pip python-six python-nibabel python-setuptools python-dev git
RUN pip install git+https://github.com/INCF/pybids.git@0.6.0
#RUN pip install pybids==0.5.1
ENV PYTHONPATH=""
# install gradient_unwarp.py (v1.0.3)
#RUN pip install https://github.com/Washington-University/gradunwarp/archive/v1.0.3.zip

# upgrade our libstdc++
RUN echo "deb http://ftp.de.debian.org/debian stretch main" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --force-yes libstdc++6 nano
    
# overwrite matlab mcr shared object
RUN rm /usr/local/R2016b/v91/sys/os/glnxa64/libstdc++.so.6 && \
	ln -s /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /usr/local/R2016b/v91/sys/os/glnxa64/libstdc++.so.6


COPY run.py /run.py
RUN chmod 555 /run.py

COPY version /version
COPY IntendedFor.py /IntendedFor.py
COPY modified_files/fsl_sub /usr/lib/fsl/5.0/fsl_sub
COPY modified_files/settings.sh ${FSL_FIXDIR}/settings.sh
COPY modified_files/PostFix.sh ${HCPPIPEDIR}/PostFix/PostFix.sh
COPY modified_files/run_prepareICAs.sh ${HCPPIPEDIR}/PostFix/Compiled_prepareICAs/distrib/run_prepareICAs.sh
COPY modified_files/RestingStateStats.sh ${HCPPIPEDIR}/RestingStateStats/RestingStateStats.sh
COPY modified_files/run_RestingStateStats.sh ${HCPPIPEDIR}/RestingStateStats/Compiled_RestingStateStats/distrib/run_RestingStateStats.sh
COPY modified_files/run_ComputeVN.sh ${HCPPIPEDIR}/MSMAll/scripts/Compiled_ComputeVN/run_ComputeVN.sh
COPY modified_files/MSMAllPipeline.sh ${HCPPIPEDIR}/MSMAll/MSMAllPipeline.sh
COPY modified_files/MSMAll.sh ${HCPPIPEDIR}/MSMAll/scripts/MSMAll.sh
COPY modified_files/generate_level1_fsf.sh ${HCPPIPEDIR}/Examples/Scripts/generate_level1_fsf.sh
COPY modified_files/hcp_fix_multi_run /opt/fix/


ENTRYPOINT ["/run.py"]
