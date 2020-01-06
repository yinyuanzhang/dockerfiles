FROM ubuntu:18.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y git-core build-essential openssl libssl-dev cmake python3-pip tzdata
RUN pip3 install conan
WORKDIR /app
COPY . .
RUN conan install --build=missing -s compiler.libcxx=libstdc++11 .
RUN cmake CMakeLists.txt -DCMAKE_BUILD_TYPE=RELEASE -DNO_GPU=ON
RUN make -j$(nproc)
WORKDIR /app/bin
RUN cp -R ../resources/* . && chmod +x run.sh && sed -i 's/creepMiner$/creepMiner "\$@"/g' run.sh
ENTRYPOINT [ "./run.sh" ]
CMD [ "--config=/data/mining.conf" ]
