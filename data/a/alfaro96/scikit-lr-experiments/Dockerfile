FROM python:3.6-slim

# Update the repositories
RUN apt-get update

# Install R
RUN apt-get install -y r-base

# Copy pip adaption for R and make it executable
COPY commands/pip-r /bin/
RUN chmod +x /bin/pip-r

# Copy the requirements
COPY requirements/*.txt /req/

# Upgrade pip and install the Python requirements
RUN pip install --upgrade pip; \
    pip install -r /req/python.txt

# Install the R requirements
RUN pip-r /req/r.txt

# Define the username
ARG USERNAME=scikit-lr-experiments

# Set the HOME environment variable
# to know the path to the user home
ENV HOME /home/$USERNAME

# Add the user
RUN useradd -ms /bin/bash $USERNAME
USER $USERNAME
RUN mkdir -p $HOME/workspace
WORKDIR $HOME/workspace

# Run the file with the experiments
CMD python $FILE $ARGUMENTS
