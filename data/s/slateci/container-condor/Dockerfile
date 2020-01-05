FROM opensciencegrid/osg-wn:3.4-devel-el7

LABEL maintainer="Lincoln Bryant <lincolnb@uchicago.edu>"

# Temporary hack until OSG 3.5 releases, for Scitokens support
RUN sed -i 's/enabled=1/enabled=0/g' /etc/yum.repos.d/osg.repo
RUN echo -e "[osg-upcoming]\nname=OSG Software for Enterprise Linux 7 - Upcoming - x86_64\nmirrorlist=https://repo.opensciencegrid.org/mirror/osg/upcoming/el7/release/x86_64\nfailovermethod=priority\npriority=97\nenabled=1\ngpgcheck=1\ngpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-OSG" > /etc/yum.repos.d/osg-upcoming.repo

# another hack- we need to remove singularity and replace it with Igor's script
# that wraps around the singularity binary from CVMFS and removes the --pid
# option
RUN yum remove -y singularity
ADD singularity_npid.sh /usr/bin/singularity

# libXt needed for some application
# tcsh needed for fsurf
# ATLAS needs unzip, gcc at least.
RUN yum -y install condor \ 
                   openssh-clients \ 
                   openssh-server \
                   libXt \
                   tcsh \
                   gcc \
                   libXpm \
                   libXpm-devel \
                   supervisor \
                   unzip && \
    yum install http://linuxsoft.cern.ch/wlcg/centos7/x86_64/wlcg-repo-1.0.0-1.el7.noarch.rpm -y && \
    yum install HEP_OSlibs -y && \
    yum clean all
   
    
RUN mkdir -p /var/lib/condor/credentials

# some extra bits for ATLAS
RUN mkdir -p /scratch && mkdir -p /home/usatlas/usatlas{1..4} && chmod 777 /scratch && chmod 777 /home/usatlas/usatlas{1..4}

# GPU stuff, sort this out later!
#RUN yum localinstall http://developer.download.nvidia.com/compute/cuda/repos/rhel7/x86_64/cuda-repo-rhel7-9.2.148-1.x86_64.rpm -y
#RUN yum install cuda-drivers-390.12 xorg-x11-drv-nvidia-390.12 xorg-x11-drv-nvidia-devel-390.12 xorg-x11-drv-nvidia-gl-390.12 xorg-x11-drv-nvidia-libs-390.12 nvidia-kmod-390.12  -y
#RUN yum install cuda-9.1.85 -y
#RUN ln -s /usr/local/cuda-9.0 /usr/local/cuda
#RUN curl -OL http://us.download.nvidia.com/XFree86/Linux-x86_64/396.51/NVIDIA-Linux-x86_64-396.51.run
#RUN chmod +x NVIDIA-Linux-x86_64-396.51.run; ./NVIDIA-Linux-x86_64-396.51.run -s

# Configuration
COPY worker.conf /etc/condor/config.d/
COPY osgvo-node-advertise /usr/local/bin/
COPY supervisord.conf /etc/supervisord.conf
COPY user-job-wrapper.sh /usr/libexec/condor/

# ssh stuff, sort this out later too!
#RUN yum install supervisor -y
#COPY supervisord.conf /etc/
#COPY sshd_config /etc/ssh/
#RUN adduser osg
#RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''
#RUN ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -N ''
#RUN ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N ''
#RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''
#RUN ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -N ''
#RUN ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N ''

# We may mount /var/lib/docker from the host, so we chown that
ENTRYPOINT chown -R condor: /var/lib/condor && \
           /usr/bin/supervisord -c /etc/supervisord.conf
