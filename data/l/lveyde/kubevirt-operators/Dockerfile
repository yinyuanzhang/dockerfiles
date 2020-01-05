# To build this, from project root run:
# docker build -t docker.io/djzager/kubevirt-operators -f Dockerfile .
FROM quay.io/openshift/origin-operator-registry

# Need root in order to be able to install git
# Only need this if the manifests are stored elsewhere
# USER root
# RUN yum -y install git
COPY registry /registry

# Initialize the database
RUN initializer --manifests /registry --output bundles.db

# There are multiple binaries in the origin-operator-registry
# We want the registry-server
ENTRYPOINT ["registry-server"]
CMD ["--database", "bundles.db"]
