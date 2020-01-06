FROM debian:10

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y texlive-full git-all && \
    useradd --create-home --shell /bin/bash latex-user

USER latex-user

WORKDIR /home/latex-user

ENTRYPOINT ["/bin/bash", "-c"]
