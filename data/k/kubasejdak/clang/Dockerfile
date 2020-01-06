FROM kubasejdak/cmake:latest
LABEL maintainer="Kuba Sejdak"

# Settings.
ARG CLANG_VERSION=9

RUN apt-get update

# Install clang, clang-tools, clang-format, clang-tidy and llvm.
RUN apt-get install -y clang-${CLANG_VERSION} \
                       clang-tools-${CLANG_VERSION} \
                       clang-format-${CLANG_VERSION} \
                       clang-tidy-${CLANG_VERSION} \
                       llvm-${CLANG_VERSION}

# Add conan profile.
COPY clang-9 /root/.conan/profiles
RUN rm /root/.conan/profiles/default
RUN ln -s /root/.conan/profiles/clang-9 /root/.conan/profiles/default
