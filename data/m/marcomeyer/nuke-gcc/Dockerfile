FROM centos/devtoolset-6-toolchain-centos7

USER 0
RUN mkdir -p /usr/local/foundry/RLM
RUN chown -R 1001:1001 /usr/local/foundry
RUN yum -y install cmake make bc wget zlib-devel mesa-libGLU-devel && yum clean all -y
USER 1001