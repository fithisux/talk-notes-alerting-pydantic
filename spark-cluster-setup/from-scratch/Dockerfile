FROM python:3.13-trixie as builder
LABEL python_version=python3.13

# Add Dependencies for PySpark
RUN apt-get update
RUN apt -y install openjdk-21-jdk-headless

# Fix the value of PYTHONHASHSEED
# Note: this is needed when you use Python 3.3 or greater
ENV SPARK_VERSION=spark-4.1.1 \
PYTHONHASHSEED=1

RUN wget --no-verbose -O apache-spark.tgz "https://archive.apache.org/dist/spark/${SPARK_VERSION}/${SPARK_VERSION}-bin-hadoop3.tgz" \
&& mkdir -p /opt/spark \
&& tar -xf apache-spark.tgz -C /opt/spark --strip-components=1 \
&& rm apache-spark.tgz

ENV SPARK_HOME=/opt/spark
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64

WORKDIR /opt/spark/

ENV PATH=$SPARK_HOME/bin:$JAVA_HOME/bin:$PATH

EXPOSE 4040 7077 8080 8081

COPY start-spark.sh /

CMD ["/bin/bash", "/start-spark.sh"]