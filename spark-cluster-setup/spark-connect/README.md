# Code Spark Structured Streaming Article

There is an [article](https://fithis2001.medium.com/processing-kafka-streams-with-spark-connect-db26216b8b33) for this.

The code is adapted from the wonderful repository of [Gary Stafford](https://github.com/garystafford/streaming-sales-generator)

Before launching the cluster you need to create a bunch of folders

* Spark configuration folder (to control the configuration) `/localvolumes/all_conf`
* Spark logging folder (to view logs) `/localvolumes/all_logs`
* The jars folder (for spark connect) `/localvolumes/jars`
* Out working directory (Spark Connect puts there the output) `/localvolumes/sc-work-dir`

You also need to copy the [spark-defaults.conf](spark-defaults.conf) into `/localvolumes/all_conf`

and also download for spark connect the jar spark-connect_2.13-4.0.1.jar from [here](https://mvnrepository.com/artifact/org.apache.spark/spark-connect) and place it in `localvolumes/jars`.

Start your docker deployment 

```
docker compose up
```


You can now run the test notebooks or the [run_bare_spark.py](run_bare_spark.py) through the command (on Windows)

```
docker run -it --network=spark-connect_spark-stack -v %cd%\localvolumes\sc-work-dir:/opt/spark/work-dir:rw -v %cd%\localvolumes\all_conf\spark-defaults.conf:/opt/spark/conf/spark-defaults.conf -v %cd%\run_bare_spark.py:/opt/spark/run_bare_spark.py apache/spark:4.0.1-scala2.13-java17-python3-r-ubuntu /opt/spark/bin/spark-submit  /opt/spark/run_bare_spark.py
```

Shut down your deployment with

```
docker compose down -v
```

and cleanup logs in `/localvolumes/all_logs`