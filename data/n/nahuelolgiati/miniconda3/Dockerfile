FROM centos:7

MAINTAINER Olgiati Nahuel <nahuelolgiati@hotmail.com>

ENV LANG "en_US.utf8"
ENV LC_ALL "en_US.utf8"

RUN yum install -y wget git bzip2 && \
    yum install -y glibc.i686 zlib.i686 ncurses-libs.i686 bzip2-libs.i686 uuid.i686 libxcb.i686 && \
    yum -y install wget libX11 libX11.i686 libXft libXft.i686 && \
    yum -y clean all

#4.7.12
ENV MINICONDA3_VERSION latest
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA3_VERSION}-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

ENV PATH /opt/conda/bin:$PATH

ENV TINI_VERSION v0.16.1
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

ENTRYPOINT [ "/usr/bin/tini", "--" ]

RUN pip uninstall -y setuptools && \
    conda install setuptools && \
    conda update -n base -c defaults conda && \
    conda config --add channels http://ssb.stsci.edu/astroconda && \
    conda create -n iraf27 python=2.7 iraf-all pyraf-all stsci && \
    conda clean -y --all

ARG USER_ID=999
ARG GROUP_ID=999

RUN groupadd -f -g ${GROUP_ID} iraf && \
    useradd -l -u ${USER_ID} -g iraf iraf

RUN mkdir -p /home/iraf && chown -R iraf:iraf /home/iraf

USER iraf
ENV HOME /home/iraf

WORKDIR ${HOME}

RUN echo 'alias iraf="cd /home/iraf; conda activate iraf27; ds9 -mode none -geometry 1200x800 -zscale -cmap bb -squared & printf "xgterm\n" | mkiraf; xgterm -sb -sl 5000 -geometry 80x48 -fn 10x20 -cr red -bg grey -e cl &"' >> ~/.bashrc
