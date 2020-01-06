FROM hashicorp/packer:1.4.3

RUN apk add --no-cache \
        bash \
        py-pip \
      	jq \
 && pip install --upgrade \
        pip \
        awscli
        

ENTRYPOINT ["/bin/bash"]
