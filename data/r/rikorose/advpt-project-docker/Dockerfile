FROM rikorose/gcc-cmake:gcc-4

RUN apt-get update && apt-get install -y --no-install-recommends \
    libboost-math-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/google/googletest/archive/release-1.8.0.tar.gz \
  && tar xf release-1.8.0.tar.gz \
  && cd googletest-release-1.8.0 \
  && cmake -DBUILD_SHARED_LIBS=ON . \
  && make \
  && cp -a googletest/include/gtest /usr/include \
  && cp -a googlemock/gtest/lib* /usr/lib \
  && cd .. \
  && rm -rf googletest-release-1.8.0

RUN wget https://github.com/nlohmann/json/releases/download/v2.0.8/json.hpp \
  && mv -u json.hpp /usr/include/json.hpp
