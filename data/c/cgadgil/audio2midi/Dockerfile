FROM ubuntu:16.04

EXPOSE 5000
RUN apt-get update && apt-get install -y wget curl tar bzip2 build-essential libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 libcairo2-dev x11vnc xvfb fluxbox python-opengl vlc screen
ENV PATH /root/miniconda3/bin/:${PATH}
ENV DISPLAY :20
ADD ./code /code
WORKDIR /code
RUN wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && /bin/bash ./Miniconda3-latest-Linux-x86_64.sh -b && rm ./Miniconda3-latest-Linux-x86_64.sh && conda install -y -c conda-forge aubio && conda install cython && conda install -y -c intel tensorflow && pip install --upgrade pip && pip install -r requirements.txt
RUN pip install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl
CMD ["/bin/bash"]
RUN mkdir ~/.vnc && x11vnc -storepasswd 1234 ~/.vnc/passwd
COPY entrypoint.sh /entrypoint.sh
