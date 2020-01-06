# this is a total ripoff job of rocker/r-parallel; except I remove
# a few packages that I never use and add a couple that I use all the time.

FROM rocker/r-base

MAINTAINER "Ricardo Graiff Garcia" ricardo@graiffgarcia.com

## System libraries
RUN apt-get update \
    && apt-get install -y \
       libopenmpi-dev \
       libzmq3-dev

## Legacy (snow is deprecated)
## RUN install.r snow doSNOW 

## MPI
## RUN install.r Rmpi

## Random Number Generation (RNG)
RUN install.r rlecuyer

## The foreach ecosystem
RUN install.r foreach iterators
RUN install.r doParallel doMC doRNG

## The future ecosystem (future itself is commented out because it's 
# one of furrr's dependencies)
# RUN install.r future
# RUN install.r future.apply
RUN install.r doFuture
RUN install.r future.callr
RUN install.r furrr

## RUN install.r BatchJobs future.BatchJobs   ## heavy set of dependencies
## RUN install.r batchtools future.batchtools ## heavy set of dependencies
## RUN install.r clustermq ## heavy set of dependencies

## Other stuff I use a lot
RUN install.r caret fastAdaboost e1071