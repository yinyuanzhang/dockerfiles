FROM  alpine:3.10
RUN   apk --no-cache update \
      && apk --no-cache add \
				ansible==2.8.4-r0 \
				curl==7.65.1-r0 \
      && pip3 install pip --upgrade \
      && pip3 install openshift==0.9.2 \
											kubernetes-validate==1.13.0 \
			&& curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl \
			&& chmod +x ./kubectl \
			&& mv ./kubectl /usr/local/bin/kubectl \
			&& ln -s /usr/bin/python3 /usr/bin/python
