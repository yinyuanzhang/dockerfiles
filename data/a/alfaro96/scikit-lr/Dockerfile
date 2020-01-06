FROM python:3.6-slim

# Update the repositories
RUN apt-get update

# Install Git for version control
RUN apt-get install -y git

# Install gcc and g++ for Cython
RUN apt-get install -y gcc g++ make

# Copy the requirements
COPY requirements/*.txt /req/

# Concatenate the requirements file to
# obtain a new one with the whole list
RUN cat /req/*.txt > /req/requirements.txt

# Upgrade pip and install the requirements
RUN pip install --upgrade pip; \
    pip install -r /req/requirements.txt

# Define the username
ARG USERNAME=scikit-lr

# Set the HOME environment variable
# to know the path to the user home
ENV HOME /home/$USERNAME

# Add the user
RUN useradd -ms /bin/bash $USERNAME
USER $USERNAME
RUN mkdir -p $HOME/workspace
WORKDIR $HOME/workspace

# Set the PYTHONPATH environment variable
# to know where the packages are installed
ENV PYTHONPATH /home/$USERNAME/.local

# Set bash as default command
CMD /bin/bash
