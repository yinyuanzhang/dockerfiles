FROM ahsankhan/todobackend-base:latest
LABEL maintainer="Ahsanuzzaman Khan<ahsan.khan434@gmail.com>"

# Install dev/build dependencies
RUN apt-get update && \
    apt-get install -qy software-properties-common && \
    apt-add-repository -y ppa:ansible/ansible && \
    apt-get update -qy && \
    apt-get install -qy ansible

# Copy baked in playbooks
COPY ansible /ansible

# Add volume for Ansible playbooks
VOLUME [ "/ansible" ]
WORKDIR /ansible

# Entrypoint
ENTRYPOINT ["ansible-playbook"]
CMD ["site.yml"]