## Build requirements pkg list
ARG FROM=opensuse/leap:15
FROM ${FROM} as requirementsbindepbuilder

ARG BINDEP_LOCATION=https://opendev.org/openstack/loci/raw/branch/master/bindep.txt
ARG PYDEP_LOCATION=https://opendev.org/openstack/loci/raw/branch/master/pydep.txt

WORKDIR /bindeps/

RUN zypper ar https://download.opensuse.org/repositories/devel:/languages:/python:/backports/openSUSE_Leap_15.0/devel:languages:python:backports.repo && zypper --gpg-auto-import-keys refresh
RUN zypper install --no-confirm --auto-agree-with-licenses --force-resolution --no-recommends python3-bindep lsb-release

ADD ${BINDEP_LOCATION} bindep.txt
ADD ${PYDEP_LOCATION} pydep.txt
RUN bindep -l csv requirements python3 | sed 's/,/ /g' > list-distropkg

## Build requirements
FROM ${FROM} as requirementsbuilder

ARG PROJECT_REF=master
ARG REQUIREMENTS_PROJECT_REF=$PROJECT_REF
ARG UPPERCONSTRAINTS_URL=https://raw.githubusercontent.com/openstack/requirements/${REQUIREMENTS_PROJECT_REF}/upper-constraints.txt
ARG PIP_WHEEL_ARGS=""
LABEL org.openstack.projectname="requirements"
LABEL org.openstack.reference="${REQUIREMENTS_PROJECT_REF}"

WORKDIR /wheels/

COPY --from=requirementsbindepbuilder /bindeps/list-distropkg /list-distropkg
COPY pip-package-blacklist.txt pip-package-extralist.txt /wheels/
ADD ${UPPERCONSTRAINTS_URL} /wheels/upper-constraints.txt

RUN zypper install \
    --no-confirm \
    --auto-agree-with-licenses \
    --force-resolution \
    --no-recommends \
    gnu_parallel \
    python3-devel \
    python3-setuptools \
    python3-wheel \
    python3-pip \
    $(cat /list-distropkg); \
    rm -f /list-distropkg

RUN cat upper-constraints.txt pip-package-extralist.txt | grep -v -f pip-package-blacklist.txt > wheel-build-list.txt
RUN cat wheel-build-list.txt | parallel "pip wheel --no-deps ${PIP_WHEEL_ARGS}"

## Build project pkg list
# keep same order as possible from requirementsbindepbuilder
ARG FROM=opensuse/leap:15
FROM ${FROM} as projectbindepbuilder

ARG PROJECT
ARG PROFILES

WORKDIR /bindeps/

RUN zypper ar https://download.opensuse.org/repositories/devel:/languages:/python:/backports/openSUSE_Leap_15.0/devel:languages:python:backports.repo && zypper --gpg-auto-import-keys refresh
RUN zypper install --no-confirm --auto-agree-with-licenses --force-resolution --no-recommends python3-bindep lsb-release

COPY --from=requirementsbindepbuilder /bindeps/bindep.txt /bindeps/bindep.txt
COPY --from=requirementsbindepbuilder /bindeps/pydep.txt /bindeps/pydep.txt

RUN bindep -l csv ${PROJECT} ${PROFILES} python3 | sed 's/,/ /g' > list-distropkg.txt
RUN bindep -f pydep.txt -l newline ${PROJECT} ${PROFILES} python3 > list-pypkg.txt

## Build project
ARG FROM=opensuse/leap:15
FROM ${FROM} as projectimage

ENV PATH=/var/lib/openstack/bin:$PATH
ARG PROJECT
ARG PROFILES
ARG PROJECT_REPO="https://opendev.org/openstack/${PROJECT}.git"
ARG PROJECT_REF="master"
ARG PIP_ARGS=""
ARG PIP_EXTRA_PACKAGES=""
ARG RPM_EXTRA_PACKAGES=""
ARG UID=42424
ARG GID=42424
LABEL org.openstack.projectname="${PROJECT}"
LABEL org.openstack.reference="${PROJECT_REF}"

COPY --from=projectbindepbuilder /bindeps/list-*.txt /tmp/
COPY --from=requirementsbuilder /wheels/ /wheels/
COPY project-install.sh /tmp/

RUN /tmp/project-install.sh
WORKDIR /var/lib/openstack
