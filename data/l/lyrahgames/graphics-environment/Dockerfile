from lyrahgames/cpp-test-tools:latest

label maintainer="markuspawellek@gmail.com"

arg VCS_REF
arg BUILD_DATE
label \
  org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/lyrahgames/docker-graphics-environment.git"

run \
  apt-get update && \
  apt-get install -y \
    freeglut3 freeglut3-dev \
    glew-utils libglew2.0 libglew-dev \
    qt5-default \
  && rm -rf /var/lib/apt/lists/*

# install latest glm library
workdir /tmp
run git clone https://github.com/g-truc/glm.git --depth=1 --branch master --single-branch glm
workdir glm/build
run \
  cmake -D CMAKE_BUILD_TYPE=Release .. && \
  cmake --build . && \
  cmake --build . --target install
workdir /
run rm -rf /tmp/glm

# install latest Eigen library
workdir /tmp
run git clone https://github.com/eigenteam/eigen-git-mirror.git --depth=1 --branch master --single-branch eigen
workdir eigen/build
run \
  cmake -D CMAKE_BUILD_TYPE=Release .. && \
  cmake --build . && \
  cmake --build . --target install
workdir /
run rm -rf /tmp/eigen