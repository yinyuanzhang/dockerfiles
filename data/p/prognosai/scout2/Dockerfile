# Base image to be used.
FROM circleci/python:2

# Maintainer of the Dockerfile.
LABEL maintainer="Prognos sectechops team"

# Run as the user
USER circleci

# AWS Access Keys to run the scout2 tool
ENV AWS_SECRET_ACCESS_KEY=""
ENV AWS_ACCESS_KEY_ID=""
ENV PATH "$PATH:/home/circleci/.local/bin"

# Installing scout2 package
RUN pip install awsscout2 --user

# Working directory
WORKDIR /home/circleci

# Entrypoint for the docker image
ENTRYPOINT ["Scout2"]


# Default command for the container.
CMD ["--help"]