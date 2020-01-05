#!/usr/bin/env python

import pickle
import requests
import os


def write_file(outfile, content):
    with open(outfile, "w") as filey:
        filey.writelines(content)


# Load in the yuuge list of Docker images
containers = pickle.load(open("containers_2.pkl", "rb"))

# Make a data folder
os.system("mkdir -p data")

start = 0
empty_count = 0
found_count = 0
for c in range(start, len(containers)):

    container = containers[c]

    if "/" not in container:
        continue

    collection, repo = container.split("/", 1)
    dockerfile = None

    letter_dir = os.path.join("data", collection[0])
    collection_dir = os.path.join(letter_dir, collection)
    output_dir = os.path.join(collection_dir, repo)
    docker_file = "%s/Dockerfile" % output_dir

    if os.path.exists(docker_file):
        continue

    # Now look for the Dockerfile
    url = "https://hub.docker.com/v2/repositories/%s/dockerfile/" % (container)

    response = requests.get(url)
    if response.status_code == 200:

        dockerfile = response.json()["contents"]

        # no dockerfile provided on Docker Hub
        if not dockerfile:
            dockerfile = None
            empty_count += 1

    # If we have something, write it!
    if dockerfile is not None:
        found_count += 1
        print("Result %s for %s!" % (found_count, container))

        # Create the output directory, if doesn't exist
        for outdir in [letter_dir, collection_dir, output_dir]:
            if not os.path.exists(outdir):
                os.mkdir(outdir)

        write_file(docker_file, dockerfile)

# empty_count
# 323306

# found_count
# 99826
