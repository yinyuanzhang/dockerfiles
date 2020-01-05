#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

FROM python:3

# Install pylint
RUN pip install pylint

# Configure apt
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get -y install python3 \
    && apt-get install -y gdebi-core python3-dev python-dev libtool-bin \
    && apt-get install -y libcurl4-openssl-dev libpcre3-dev libssh-dev libxml2-dev libxslt1-dev cmake \
    && apt-get -y install --no-install-recommends apt-utils 2>&1

# Install git, process tools, lsb-release (common in install instructions for CLIs)
RUN apt-get -y install git procps lsb-release

# Install any missing dependencies for enhanced language service
RUN apt-get install -y libicu[0-9][0-9]

RUN mkdir /workspace
WORKDIR /workspace

# Install Python dependencies from requirements.txt if it exists
#COPY .devcontainer/requirements.txt /requirements.txt
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN if [ -f "/requirements.txt" ]; then pip install -r /requirements.txt ; fi

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog

# Set the default shell to bash rather than sh
ENV SHELL /bin/bash
