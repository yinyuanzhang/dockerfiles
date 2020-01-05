###   Start from the official poldracklab/mriqc   ###
# We'll modify just the function we need to.
ARG POLDRACK_MRIQC_VERSION=0.15.0
FROM poldracklab/mriqc:${POLDRACK_MRIQC_VERSION}

###   make it only use the "highres" anatomical images:   ####
#     and only the unique ones:

# In the file mriqc_run.py, find the lines in which we get
# the dataset, and:
#   1) add the contents of the .bidsignore file to the 'exclude' list
#      (not really needed, but just in case)
# In the file (bids.py), find the lines in which we get the images in
# the dataset, and:
#   2) only use the ones with "acquisition" = "highres" to make sure
#      we don't use scouts, "T1w-FSE" images, etc.

# Entry Point (for the poldracklab/mriqc image):
ARG poldrackmriqc_ep=/usr/local/miniconda/bin/mriqc
ENV ep=$poldrackmriqc_ep

RUN fileToEdit=$(find `dirname $ep`/../lib/python*/site-packages/mriqc/ -name mriqc_run.py) \
    && sed -i \
        -e "s#\( *\)layout = BIDSLayout#\
\1try:\n\
\1    with open(str(settings['bids_dir']) + \"/.bidsignore\",'r') as f:\n\
\1        lines = [line.rstrip() for line in f]\n\
\1except FileNotFoundError:\n\
\1    lines = []\n\
&#" \
        -e "s#\( *\)exclude=\[\(.\+\)\])#\1exclude=\[\2\]+lines)#" \
       $fileToEdit \
    && fileToEdit=$(dirname $ep)/../lib/python*/site-packages/mriqc/utils/bids.py \
    && sed -i \
        -e "s#\( *\)for btype in bids_type:#&\n\1    myFilter={'acquisition':'highres'} if btype=='T1w' else {}#" \
	-e "s#\( *\)\*\*basequery#\1\*\*{\*\*basequery, \*\*myFilter} #" \
       $fileToEdit


# Since we didn't define an ENTRYPOINT, our image will have the same ENTRYPOINT
#   as the base image.
