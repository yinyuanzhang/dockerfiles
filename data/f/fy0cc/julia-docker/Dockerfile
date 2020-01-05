
FROM debian:stretch

ARG L32=""
USER root
WORKDIR /root/

# update apt
RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		ca-certificates \
# ERROR: no download agent available; install curl, wget, or fetch
		curl \
		gnupg\
	; \
	rm -rf /var/lib/apt/lists/*

# install gcc and make tools
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get -y install \
		# dependencies for build Cairo.jl
		build-essential gettext libcairo2 libpango1.0-0 && \
    rm -rf /var/lib/apt/lists/*


ENV JULIA_PATH /usr/bin/
ENV PATH $JULIA_PATH/bin:$PATH



# RUN ${L32} gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 3673DF529D9049477F76B37do566E3C7DC03D6E495

# We template this in here instead of passing it in as an ARG at the top like
# we do with L32 so that we can re-use the `apt update` and `gpg --keyserver`
# steps above as much as possible as they take a nontrivial amount of time.
ARG JULIA_URL="https://julialang-s3.julialang.org/bin/linux/x64/0.6/julia-0.6.4-linux-x86_64.tar.gz"

# Download Julia
RUN ${L32} curl -sSL "${JULIA_URL}" -o julia.tar.gz

# Verify the Julia download (this is removed for builds without a .tar.gz.asc)
# RUN ${L32} curl -sSL "${JULIA_URL}.asc" -o julia.tar.gz.asc && \
    # ${L32} gpg --batch --verify julia.tar.gz.asc julia.tar.gz && \
    # ${L32} rm -r "${HOME}/.gnupg" julia.tar.gz.asc

# Unpack Julia into /usr
RUN ${L32} tar -xzf julia.tar.gz -C /usr --strip-components 1
RUN chown root:root /usr/bin/julia

# Cleanup after yourself
RUN ${L32} rm -rf /var/lib/apt/lists/* julia.tar.gz*

# Create entrypoint.sh to shoe-horn ${L32} into everything
RUN ${L32} echo "#!/bin/bash" > /entrypoint.sh && \
    ${L32} echo "${L32} \"\$@\"" >> /entrypoint.sh && \
    ${L32} chmod +x /entrypoint.sh


# Install Julia packages from REQUIRE file
RUN julia -e "Pkg.update()"
COPY REQUIRE /root/.julia/v0.6/REQUIRE
RUN julia -e "Pkg.resolve()"


# Install aws-cli
RUN apt-get update &&\
		apt-get install -y python python-pip &&\
		python -m pip install --upgrade pip &&\
	  python -m pip install awscli --upgrade --user &&\
		echo "export PATH=/root/.local/bin:$PATH" > /root/.bashrc

COPY entrypoint.sh /root/entrypoint.sh
ENV PATH=/root/.local/bin/:$PATH

# ENTRYPOINT ["bash","/root/entrypoint.sh"]
CMD ["julia"]
