FROM artyjay/base_linux_dev:latest
LABEL maintainer="R.Johnson"

## Custom remote for herbert with prebuilt binaries not publicly available
RUN conan remote add herbert https://api.bintray.com/conan/artyjay/herbert --insert

## Pull in the conanfile.py script to make sure we capture the correct current dependencies
COPY conanfile.py conanfile.py

## Pre-load GCC 8.2 deps
RUN echo 2 | update-alternatives --config cc \
 && conan install conanfile.py --build missing -s compiler=gcc -s compiler.version=8 -s compiler.libcxx=libstdc++11 -s build_type=Release \
 && conan install conanfile.py --build missing -s compiler=gcc -s compiler.version=8 -s compiler.libcxx=libstdc++11 -s build_type=RelWithDebInfo \ 
 && conan install conanfile.py --build missing -s compiler=gcc -s compiler.version=8 -s compiler.libcxx=libstdc++11 -s build_type=Debug 

## Pre-load Clang 7 deps
RUN echo 1 | update-alternatives --config cc \
 && conan install conanfile.py --build missing -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libstdc++11 -s build_type=Release \
 && conan install conanfile.py --build missing -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libstdc++11 -s build_type=RelWithDebInfo \ 
 && conan install conanfile.py --build missing -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libstdc++11 -s build_type=Debug 

## Clean up generated stuff
RUN rm /conanfile.py \
 && rm /conanbuildinfo.* \
 && rm /conaninfo.txt \
 && rm /graph_info.json