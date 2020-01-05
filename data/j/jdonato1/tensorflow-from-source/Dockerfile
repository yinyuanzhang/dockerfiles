# jdonato1/tensorflow-from-source
# Jorge Donato / jmdonato1@sbcglobal.net 
#
# Build an Ubuntu environment that can use bazel to build tensorflow
#
# This is intended for compiling tensorflow for Poorman's Kaggle 
# (poormans-kaggle).  Specifically, it builds tensorflow for your
# CPU.  Newer libraries of tensorflow (>=1.6.0) require a CPU with
# AVX instructions if you are to use the precompiled binaries.  
# For older CPUs, the best approach is to compile from source.
# This will take a long time if using only one CPU. 
#
# (Using more than one CPU for compile is left as an exercise for
# the reader.  If you do get it to work, let me know -Jorge)

FROM ubuntu:bionic

COPY rc.local /etc/rc.local

COPY tf_build /root/tf_build

RUN chmod 755 /etc/rc.local /root/tf_build

#######################################################
# from https://www.tensorflow.org/install/source

  ###########################################################################################################
  # from https://docs.bazel.build/versions/master/install-ubuntu.html#using-bazel-custom-apt-repository

	# Install bazel first.  Use the apt method to do this
	# See https://docs.bazel.build/versions/master/install-ubuntu.html#using-bazel-custom-apt-repository

	# now installed by ./tf_build 

  # Done installing bazel (you will thank me later)
  ####################################################



# NOTE: About the compilation there are "over 9000" things to be done to 
# compile tensorflow (more in the order of 11,000 or so).  On a slow 1 
# CPU machine of 11,000 or so).  On a slow 1 CPU machine, it took 8 hours
# to compile.  It is a slow compilation.  Do not get frustrated and stop 
# bazel.   It *IS* working.  Just start in the evening and go home.

# We are skipping the test because it can take hours to run just the test.  
# Just go stright to business.
		
# Download tensorflow source
# This happens now in ./tf_build

CMD ["/etc/rc.local"]
