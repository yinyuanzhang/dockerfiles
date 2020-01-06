FROM python:3.8.0-slim-buster

ENV PYTHONUNBUFFERED 1

ENV PYTHON_LIBRARY_PATH /opt/venv
ENV PATH ${PYTHON_LIBRARY_PATH}/bin:${PATH}

ENV LIBRARY_PATH /usr/local/lib
ENV LD_LIBRARY_PATH /usr/local/lib
ENV LIBRARY_INCLUDE_PATH /usr/local/include

# Install apt dependencies
# Put apt dependencies here that are needed by all build paths
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        git \
        iproute2 \
        libgmp-dev \
        libffi-dev \
        libmpc-dev \
        libmpfr-dev \
        libssl-dev \
	&& rm -rf /var/lib/apt/lists/*

# Setup virtualenv
RUN python -m venv ${PYTHON_LIBRARY_PATH}

# Charm
# NOTE: The vitual environment of the Charm image is copied into virtual
# environment of this image. This seems to be a fragile approach, as collisions
# between packages can occur. For instance, if pip is upgraded before the copy
# step, pip will not work.
# TODO: Look into using wheels instead of virtual environments.
COPY --from=initc3/charm-crypto:4893024-python3.8-slim-buster \
                $LIBRARY_INCLUDE_PATH/pbc \
                $LIBRARY_INCLUDE_PATH/pbc
COPY --from=initc3/charm-crypto:4893024-python3.8-slim-buster \
                $LIBRARY_PATH/libpbc.so.1.0.0 \
                $LIBRARY_PATH/libpbc.so.1.0.0
RUN set -ex \
    && cd $LIBRARY_PATH \
    && ln -s libpbc.so.1.0.0 libpbc.so \
    && ln -s libpbc.so.1.0.0 libpbc.so.1
COPY --from=initc3/charm-crypto:4893024-python3.8-slim-buster \
                ${PYTHON_LIBRARY_PATH} \
                ${PYTHON_LIBRARY_PATH}

# Install Python dependencies here that are absolutely required by setup.py for
# better cache performance. These should be changed rarely, as they cause
# long rebuild times.
RUN pip install --upgrade pip \
    cffi \
    Cython \
    gmpy2 \
    psutil \
    pycrypto \
    pyzmq \
    zfec

# FLINT
COPY --from=initc3/flint2:4d687a6-buster \
                $LIBRARY_INCLUDE_PATH/flint \
                $LIBRARY_INCLUDE_PATH/flint
COPY --from=initc3/flint2:4d687a6-buster \
                $LIBRARY_PATH/libflint.a \
                $LIBRARY_PATH/libflint.a
COPY --from=initc3/flint2:4d687a6-buster \
                $LIBRARY_PATH/libflint.so.13.5.2 \
                $LIBRARY_PATH/libflint.so.13.5.2
RUN set -ex \
    && cd $LIBRARY_PATH \
    && ln -s libflint.so.13.5.2 libflint.so \
    && ln -s libflint.so.13.5.2 libflint.so.13

# NTL
COPY --from=initc3/ntl:11.4.1-buster $LIBRARY_INCLUDE_PATH/NTL $LIBRARY_INCLUDE_PATH/NTL
COPY --from=initc3/ntl:11.4.1-buster $LIBRARY_PATH/libntl.a $LIBRARY_PATH/libntl.a

# Rust
ENV RUSTUP_HOME /usr/local/rustup
ENV CARGO_HOME /usr/local/cargo
COPY --from=initc3/rust-frozen:2019.11.21-slim-buster $RUSTUP_HOME $RUSTUP_HOME
COPY --from=initc3/rust-frozen:2019.11.21-slim-buster $CARGO_HOME $CARGO_HOME
ENV PATH "${CARGO_HOME}/bin:${PATH}"
