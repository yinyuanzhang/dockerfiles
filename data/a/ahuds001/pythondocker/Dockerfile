FROM ubuntu:latest
RUN apt-get update && apt-get install -y sudo \
					curl \
					vim \
					apt-utils \ 
					build-essential \
					wget	
RUN cd /usr/local && \
		wget https://repo.continuum.io/archive/Anaconda2-4.1.1-Linux-x86_64.sh -O /usr/local/anaconda.sh
RUN bash usr/local/anaconda.sh -b -p /usr/local/anaconda 
ENV PATH /usr/local/anaconda/bin:$PATH
RUN apt-get clean && apt-get autoclean
## Better Alternative to Mount Volume
## COPY /TalkingData /home/Documents/Kaggle/TalkingData
