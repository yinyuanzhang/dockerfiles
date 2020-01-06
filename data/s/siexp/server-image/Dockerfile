FROM ubuntu:19.10

RUN apt-get update && apt-get upgrade -y

# Install build-essential
RUN apt-get install -y \
    cmake \
    build-essential \
    clang-8 \
    libboost-all-dev \
    libcurl4-openssl-dev \
    libwebsocketpp-dev \
    libmysqlcppconn-dev \
    libmysqlclient-dev \
    mysql-client \
    libcpprest-dev \
    zlib1g-dev \
    python-pip \
    wget \
    git \ 
    default-jdk

# swagger
RUN cd ~ && \
    wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.5/swagger-codegen-cli-2.4.5.jar -O swagger-codegen-cli.jar

# flyway
RUN cd ~ && \
    wget -qO- https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/6.0.8/flyway-commandline-6.0.8-linux-x64.tar.gz | tar xvz && \
    ln -s `pwd`/flyway-6.0.8/flyway /usr/local/bin && \
    rm -f flyway-commandline-6.0.8-linux-x64.tar.gz

# cpp-jwt
RUN cd ~ && \
    rm -rf cpp-jwt && \
    git clone -b master --single-branch https://github.com/arun11299/cpp-jwt.git && \
    cp -r cpp-jwt/include/jwt /usr/local/include/jwt && \
    sed -i 's/jwt\/json/nlohmann/g' /usr/local/include/jwt/jwt.hpp && \
    cd ~ && \
    rm -rf cpp-jwt

# sha256
RUN cd ~ && \
    rm -rf PicoSHA2 && \
    git clone -b master --single-branch https://github.com/okdshin/PicoSHA2.git && \
    cd PicoSHA2 && \
    cp picosha2.h /usr/local/include && \
    cd ~ && \
    rm -rf PicoSHA2

# pistache
RUN cd ~ && \
    rm -rf pistache && \
    git clone -b master --single-branch https://github.com/oktal/pistache.git && \
    cd pistache && \
    git submodule update --init --recursive && \
    mkdir build && \
    cd build && \
    cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release .. && \
    make && \
    make install && \
    cd ~ && \
    rm -rf pistache && \
    ldconfig

# hinnantdate depends on curl
RUN cd ~ && \
    rm -rf date && \
    git clone -b "v2.4.1" --single-branch https://github.com/HowardHinnant/date.git && \
    cd date && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install && \
    cd ~ && \
    rm -rf date && \
    ldconfig

# sqlpp11 depends on hinnantdate
RUN cd ~ && \
    rm -rf sqlpp11 && \
    git clone -b master --single-branch https://github.com/rbock/sqlpp11.git && \
    cd sqlpp11 && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j$(nproc) && \
    make install && \
    cd ~ && \
    pip install pyparsing && \
    rm -rf sqlpp11 && \
    ldconfig

# sqlpp11-connector-mysql
RUN cd ~ && \
    rm -rf sqlpp11-connector-mysql && \
    git clone -b master --single-branch https://github.com/rbock/sqlpp11-connector-mysql.git && \
    cd sqlpp11-connector-mysql && \
    mkdir build && \
    cd build && \
    cmake -DDATE_INCLUDE_DIR=/usr/local/include -DSQLPP11_INCLUDE_DIR=/usr/local/include .. && \
    make -j$(nproc) && \
    make install && \
    cd ~ && \
    rm -rf sqlpp11-connector-mysql && \
    ldconfig

# breakpad
RUN cd ~ && \
    rm -rf breakpad && \
    git clone -b master --single-branch https://github.com/google/breakpad.git && \
    cd breakpad && \
    git clone -b master --single-branch https://chromium.googlesource.com/linux-syscall-support src/third_party/lss && \
    ./configure && \
    make -j$(nproc) && \
    make install

# nlohmann json
RUN cd ~ && \
    rm -rf json && \
    git clone -b master --single-branch https://github.com/nlohmann/json.git && \
    cd json && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j$(nproc) && \
    make install && \
    cd ~ && \
    rm -rf json

# rapid json
RUN cd ~ && \
    rm -rf rapidjson && \
    git clone -b master --single-branch https://github.com/Tencent/rapidjson.git && \
    cd rapidjson && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j$(nproc) && \
    make install && \
    cd ~ && \
    rm -rf rapidjson

# yasmine
RUN cd ~ && \
    rm -rf yasmine && \
    rm -rf /usr/local/include/yasmine && \
    rm -rf /usr/local/include/essentials && \
    rm -rf /usr/local/include/hermes && \
    rm -rf /usr/local/lib/*yasmine* && \
    git clone -b "v1.4.1" --single-branch https://github.com/SeadexGmbH/yasmine.git && \
    cd yasmine && \
    mkdir build2 && \
    cd build2 && \
    cmake -DCMAKE_C_COMPILER=/usr/bin/clang-8 -DCMAKE_CXX_COMPILER=/usr/bin/clang++-8 .. && \
    make -j$(nproc) libyasmine && \
    cd libyasmine && \
    make install && \
    mv /usr/local/include/yasmine/essentials/include/essentials/ /usr/local/include/essentials/ && \
    mv /usr/local/include/yasmine/hermes/include/ /usr/local/include/hermes/ && \
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib && \
    ldconfig && \
    cd ~ && \
    rm -rf yasmine

# cpp-resdis
RUN cd ~ && \
    rm -rf cpp_redis && \
    git clone -b master --single-branch https://github.com/Cylix/cpp_redis.git && \
    cd cpp_redis && \
    git submodule init && \
    git submodule update && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j$(nproc) && \
    make install && \
    cd ~ && \
    rm -rf cpp_redis

# g3log
RUN cd ~ && \
    rm -rf /usr/local/include/g3log && \
    rm -rf /usr/local/lib/*g3log* && \
    rm -rf g3log && \
    git clone -b master --single-branch https://github.com/KjellKod/g3log.git && \
    cd g3log && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j$(nproc) && \
    make install && \
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib && \
    ldconfig && \
    cd ~ && \
    rm -rf g3log

# kafka
RUN cd ~ && \
    rm -rf librdkafka && \
    git clone -b master --single-branch https://github.com/edenhill/librdkafka.git && \
    cd librdkafka && \
    git submodule init && \
    git submodule update && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j$(nproc) && \
    make install && \
    cd ~ && \
    rm -rf librdkafka

RUN cd ~ && \
    rm -rf cppkafka && \
    git clone -b master --single-branch https://github.com/mfontanini/cppkafka.git && \
    cd cppkafka && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j$(nproc) && \
    make install && \
    cd ~ && \
    rm -rf cppkafka

# gtest
RUN cd ~ && \
    git clone -b master --single-branch https://github.com/google/googletest.git  && \
    cd googletest  && \
    mkdir build && \
    cd build && \
    cmake ..  && \
    make -j$(nproc) && \
    make install && \
    cd ~ && \
    rm -rf googletest

# libbcrypt
RUN cd ~ && \
    rm -rf libbcrypt && \
    git clone -b master --single-branch https://github.com/trusch/libbcrypt && \
    cd libbcrypt && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install && \
    ldconfig && \
    cd ~ && \
    rm -rf libbcrypt

# pcg-cpp for RNG
RUN cd ~ && \
    rm -rf pcg-cpp && \
    git clone -b master --single-branch https://github.com/imneme/pcg-cpp.git && \
    cd pcg-cpp && \
    make && \
    make install && \
    cd ~ && \
    rm -rf pcg-cpp

# patch sqlcppconn for C++17
RUN sed -i 's/throw (std::bad_alloc)/noexcept(false)/g' /usr/include/cppconn/exception.h && sed -i 's/throw()/noexcept/g' /usr/include/cppconn/exception.h
