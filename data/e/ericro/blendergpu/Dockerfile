FROM nvidia/cuda:9.0-runtime
#inspired by https://github.com/yuyou/blender/blob/master/7.5/Dockerfile
MAINTAINER eric <er@iex.ec>

ENV BLENDER_MAJOR 2.79
ENV BLENDER_VERSION 2.79b
ENV BLENDER_BZ2_URL http://mirror.cs.umn.edu/blender.org/release/Blender$BLENDER_MAJOR/blender-$BLENDER_VERSION-linux-glibc219-x86_64.tar.bz2

RUN apt-get update && \
	apt-get install -y \
		curl wget nano \
		bzip2 libfreetype6 libgl1-mesa-dev \
		libglu1-mesa \
		libxi6 \
		libxrender1 && \
	apt-get -y autoremove && \
	rm -rf /var/lib/apt/lists/*

RUN mkdir /usr/local/blender && \
	curl -SL "$BLENDER_BZ2_URL" -o blender.tar.bz2 && \
	tar -jxvf blender.tar.bz2 -C /usr/local/blender --strip-components=1 && \
	rm blender.tar.bz2

RUN ln -s /usr/local/blender/blender /usr/bin/blender


COPY set_gpu.py /tmp/set_gpu.py
COPY benchmark_279_denoise_disney.blend /tmp/


CMD blender --background --python /tmp/set_gpu.py /tmp/benchmark_279_denoise_disney.blend --render-output /tmp/ --render-frame 1
# For the next line, use "-v /tmp:/iexec" in the docker run command line to output the image created in /tmp og the host 
#CMD blender --background --python /tmp/set_gpu.py /tmp/benchmark_279_denoise_disney.blend --render-output /iexec/ --render-frame 1
