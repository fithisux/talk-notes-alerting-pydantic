
# General

This is an educational standalone Spark Cluster

It improves upon [Spark Cluster with Docker](https://github.com/mvillarrealb/docker-spark-cluster) with significant simplifications. The most important is that you can use the latest version of spark. See [Dockerfile](./Dockerfile)

# Installation

The following steps will make you run your spark cluster's containers.

## Pre requisites

* Docker installed

It has been tested with Rancher Desktop on Windows

**TODO:** Check podman! 


## Run the cluster

First build your image:

(you may need to run `dos2unix` command on `start-spark.sh`)

```sh
docker build -t my/spark .
```


The final step to create your test cluster will be to run the compose file so as to start the cluster:

```sh
docker-compose up -d
```

## Run your first spark app on the cluster

Create in the root folder a new folder called `result-dir`

First, run a spark driver container with the correct files linked.

```
docker run -it --network=app-tier -v %cd%/result-dir:/opt/spark/work-dir:rw -v %cd%\conf\spark-defaults.conf:/opt/spark/conf/spark-defaults.conf -v %cd%\run_bare_spark.py:/opt/spark/run_bare_spark.py my/spark bash
```

And the submit your job.

```
/opt/spark/bin/spark-submit  /opt/spark/run_bare_spark.py
```

Results will be hosted on result-dir.