#!/bin/bash

set -x 


./kafka_2.13-3.0.0/bin/kafka-server-stop.sh

./kafka_2.13-3.0.0/bin/zookeeper-server-stop.sh 

set +x 
