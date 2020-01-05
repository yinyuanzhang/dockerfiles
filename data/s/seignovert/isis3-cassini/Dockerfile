FROM seignovert/usgs-isis3:latest

LABEL maintainer="Seignovert"

# Sync `Cassini` data
RUN rsync -azv --delete --partial \
    --exclude="testData/" \
    --exclude="kernels/" \
    isisdist.astrogeology.usgs.gov::isis3data/data/cassini/ \
    $ISIS3DATA/cassini/

# Add rsync aliases
RUN echo "\n\
    alias rsync_cassini_data='rsync -azv --delete --partial \
    --exclude=\"testData/\" \
    --exclude=\"kernels/\" \
    isisdist.astrogeology.usgs.gov::isis3data/data/cassini/ \
    $ISIS3DATA/cassini/'\n\
    alias rsync_cassini_kernels='rsync -azv --delete --partial \
    isisdist.astrogeology.usgs.gov::isis3data/data/cassini/kernels/ \
    $ISIS3DATA/cassini/kernels/'" >> $HOME/.bashrc
