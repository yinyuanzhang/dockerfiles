FROM busybox:latest

ENV CNI_VERSION v0.8.3

WORKDIR /cni
ADD https://github.com/containernetworking/plugins/releases/download/$CNI_VERSION/cni-plugins-linux-amd64-$CNI_VERSION.tgz cni-plugins.tgz

ENTRYPOINT ["tar", "xvzf", "cni-plugins.tgz", "-C", "/opt/cni/bin"]
