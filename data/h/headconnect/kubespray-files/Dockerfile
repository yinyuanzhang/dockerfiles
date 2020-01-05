# This is your Editor pane. Write the Dockerfile here and 
# use the command line to execute commands
FROM nginx:alpine
COPY . /usr/share/nginx/html

RUN mkdir -p /kubernetes-release/release/v1.12.4/bin/linux/amd64
ADD https://storage.googleapis.com/kubernetes-release/release/v1.12.4/bin/linux/amd64/kubeadm /usr/share/nginx/html/kubernetes-release/release/v1.12.4/bin/linux/amd64/

RUN mkdir -p /kubernetes-release/release/v1.11.6/bin/linux/amd64
ADD https://storage.googleapis.com/kubernetes-release/release/v1.11.6/bin/linux/amd64/kubeadm /usr/share/nginx/html/kubernetes-release/release/v1.11.6/bin/linux/amd64/

RUN mkdir -p /kubernetes-release/release/v1.10.12/bin/linux/amd64
ADD https://storage.googleapis.com/kubernetes-release/release/v1.10.12/bin/linux/amd64/kubeadm /usr/share/nginx/html/kubernetes-release/release/v1.10.12/bin/linux/amd64/

RUN mkdir -p /usr/share/nginx/html/kubernetes-release/release/v1.12.4/bin/linux/amd64
ADD https://storage.googleapis.com/kubernetes-release/release/v1.12.4/bin/linux/amd64/hyperkube /usr/share/nginx/html/kubernetes-release/release/v1.12.4/bin/linux/amd64/

RUN mkdir -p /usr/share/nginx/html/kubernetes-release/release/v1.11.6/bin/linux/amd64
ADD https://storage.googleapis.com/kubernetes-release/release/v1.11.6/bin/linux/amd64/hyperkube /usr/share/nginx/html/kubernetes-release/release/v1.11.6/bin/linux/amd64/

RUN mkdir -p /usr/share/nginx/html/kubernetes-release/release/v1.10.12/bin/linux/amd64
ADD https://storage.googleapis.com/kubernetes-release/release/v1.10.12/bin/linux/amd64/hyperkube /usr/share/nginx/html/kubernetes-release/release/v1.10.12/bin/linux/amd64/

RUN mkdir -p /usr/share/nginx/html/coreos/etcd/releases/download/v3.2.24
ADD https://github.com/coreos/etcd/releases/download/v3.2.24/etcd-v3.2.24-linux-amd64.tar.gz /usr/share/nginx/html/coreos/etcd/releases/download/v3.2.24/

RUN mkdir -p /usr/share/nginx/html/containernetworking/plugins/releases/download/v0.6.0
ADD https://github.com/containernetworking/plugins/releases/download/v0.6.0/cni-plugins-amd64-v0.6.0.tgz /usr/share/nginx/html/containernetworking/plugins/releases/download/v0.6.0/

RUN apk update
RUN apk add nginx
#RUN apk add nano

COPY default.conf /etc/nginx/conf.d/default.conf
run chmod -R a+r /usr/share/nginx/html/

ENTRYPOINT ["nginx", "-g", "daemon off;"]
