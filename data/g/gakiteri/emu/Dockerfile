### RUN ME WITH ###
# docker run -it --rm --privileged -p 23:22 gakiteri/emu:kubernetes
# docker run -it --rm --privileged -v /var/run/docker.sock:/var/run/docker.sock -p 23:22 gakiteri/emu:kubernetes

FROM gakiteri/emu:ubuntu

# INSTALL NECESARY PACKAGES
RUN apt-get install -y gnupg software-properties-common ca-certificates \
# INSTALL KUBERNETES SERVICE
  && curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl \
  && chmod +x ./kubectl \
  && mv ./kubectl /usr/local/bin/kubectl \
# INSTALL MINIKUBE
  && curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_1.3.1.deb \
  && sudo dpkg -i minikube_1.3.1.deb \
  && rm minikube_1.3.1.deb \
# INSTALL DOCKER
  && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
  && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
  && apt-get install -y docker-ce docker-ce-cli containerd.io \
  && apt-get clean

# --no-install-recommends

# RUN CONFIGURATION
RUN minikube config set vm-driver none \
  && apt-get install -y --no-install-recommends ebtables ethtool socat \
  && echo "#!/bin/sh" > \autorun.sh \
  && echo 'echo "pass\\npass\\n" | passwd root' >> /autorun.sh \
  && echo "rm /autorun.sh" >> /autorun.sh \
  && chmod +x /autorun.sh \
  && /autorun.sh

#  systemctl enable kubelet.service \
#  && minikube delete \
#  && minikube start
