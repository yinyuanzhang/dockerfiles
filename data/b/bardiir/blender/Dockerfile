FROM ubuntu:16.04

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		curl \
		bzip2 \
		libfreetype6 \
		libgl1-mesa-dev \
		libglu1-mesa \
		libxrender1 \
		libxi6 \
		ca-certificates \
		unzip \
		xvfb \
	&& apt-get -y autoremove \
	&& rm -rf /var/lib/apt/lists/*

ENV BLENDER_BZ2_URL https://download.blender.org/release/Blender2.80/blender-2.80rc3-linux-glibc217-x86_64.tar.bz2 

RUN mkdir /usr/local/blender \
	&& curl -SL "$BLENDER_BZ2_URL" -o blender.tar.bz2 \
	&& tar -jxvf blender.tar.bz2 -C /usr/local/blender --strip-components=1 \
	&& rm blender.tar.bz2

RUN echo "#!/bin/bash\n\nxvfb-run -s \"-screen 0 1920x1080x24\" /usr/local/blender/blender \"\$@\"" > /blender
RUN chmod +x /blender

ENTRYPOINT ["/blender"]
