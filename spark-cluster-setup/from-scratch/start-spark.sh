#!/bin/bash

echo "$SPARK_WORKLOAD"

if [ "$SPARK_WORKLOAD" == "master" ];
then

    /opt/spark/bin/spark-class org.apache.spark.deploy.master.Master

elif [ "$SPARK_WORKLOAD" == "worker" ];
then

    /opt/spark/bin/spark-class org.apache.spark.deploy.worker.Worker $SPARK_MASTER

else
    echo "Undefined Workload Type $SPARK_WORKLOAD, must specify: master, worker, submit"
fi

