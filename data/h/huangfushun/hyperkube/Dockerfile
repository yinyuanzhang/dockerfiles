FROM  gcr.io/google_containers/hyperkube-amd64:v1.11.9
RUN rm -rf  /etc/kubernetes/manifests-multi/*.json \
            && rm -rf /etc/kubernetes/addons/*.json
COPY master.json /etc/kubernetes/manifests-multi/master.json
COPY kube-proxy.json /etc/kubernetes/manifests-multi/kube-proxy.json
