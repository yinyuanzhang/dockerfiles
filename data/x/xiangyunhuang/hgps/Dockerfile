FROM fedora:30

ARG R_VERSION
ENV R_VERSION=${R_VERSION:-3.6.0} \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    TERM=xterm

LABEL org.label-schema.license="GPL-2.0" \
      org.label-schema.vcs-url="https://github.com/XiangyunHuang/HGPS" \
      org.label-schema.vendor="Hierarchical Gaussian Processes in Stan (HGPS)" \
      maintainer="Xiangyun Huang <xiangyunfaith@outlook.com>"

RUN groupadd staff \
  && useradd -g staff -d /home/docker docker

RUN dnf update -y \
  && dnf install -y R \
    R-littler \
    R-littler-examples \
    pandoc \
    pandoc-citeproc \
  && dnf clean all \
  && echo "options(repos = c(CRAN = 'https://mirrors.tuna.tsinghua.edu.cn/CRAN/'))" >> /usr/lib64/R/etc/Rprofile.site \	
  && echo "options(download.file.method = 'libcurl')" >> /usr/lib64/R/etc/Rprofile.site \	
  && mkdir -p /usr/local/lib/R/site-library \
  && chown -R root:staff /usr/local/lib/R/site-library \
  && chmod g+wx /usr/local/lib/R/site-library \
  && ln -s /usr/lib64/R/library/littler/examples/install.r /usr/bin/install.r \
  && ln -s /usr/lib64/R/library/littler/examples/install2.r /usr/bin/install2.r \
  && ln -s /usr/lib64/R/library/littler/examples/installGithub.r /usr/bin/installGithub.r \
  && ln -s /usr/lib64/R/library/littler/examples/testInstalled.r /usr/bin/testInstalled.r \
  && install.r docopt \
  && mkdir ~/.R \
  && echo "CXXFLAGS += -Wno-ignored-attributes" >> ~/.R/Makevars \
  && echo "CXX14 = g++" >> ~/.R/Makevars \
  && echo "CXX14FLAGS = -fPIC -flto=2 -mtune=native -march=native" >> ~/.R/Makevars \
  && echo "CXX14FLAGS += -Wno-unused-variable -Wno-unused-function -Wno-unused-local-typedefs" >> ~/.R/Makevars \
  && echo "CXX14FLAGS += -Wno-ignored-attributes -Wno-deprecated-declarations -Wno-attributes -O3" >> ~/.R/Makevars \
  && install2.r --error rmarkdown rstan dplyr

RUN mkdir -p /home/docker/workspace
WORKDIR /home/docker/workspace

CMD ["R"]
