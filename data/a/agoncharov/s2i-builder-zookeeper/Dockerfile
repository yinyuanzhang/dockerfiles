# s2i-zookeeper
FROM registry.fedoraproject.org/f28/s2i-base

LABEL maintainer="Artem Goncharov <artem.goncharov@gmail.com>"

ENV BUILDER_VERSION 0.1

ENV PATH=${APP_ROOT}/bin:$PATH

LABEL io.k8s.description="Platform for building Zookeeper" \
      io.k8s.display-name="builder Zookeeper F28" \
      io.openshift.expose-services="2181,2888,3888" \
      io.openshift.tags="builder,zookeeper,0.1.0"

# TODO: Install required packages here:
RUN dnf install -y zookeeper hostname nmap-ncat -v && dnf clean all -y

# TODO (optional): Copy the builder files into /opt/app-root
# COPY ./<builder_folder>/ ${APP_ROOT}

# TODO: Copy the S2I scripts to $STI_SCRIPTS_PATH, since s2i-base image
# sets io.openshift.s2i.scripts-url label that way, or update that label
COPY ./s2i/bin/ $STI_SCRIPTS_PATH

# Copy extra files to the image.
COPY ./root/ /

# TODO: Drop the root user and make the content of /opt/app-root owned by user 1001
RUN chown -R 1001:0 ${APP_ROOT} && \
    fix-permissions ${APP_ROOT} -P

# This default user is created in the s2i-base image
USER 1001

# TODO: Set the default port for applications built using this image
EXPOSE 2181 2888 3888

# TODO: Set the default CMD for the image
CMD ["$STI_SCRIPTS_PATH/usage"]
