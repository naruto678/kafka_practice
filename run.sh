#!/bin/bash
set -x 


KAFKA_PATH=`pwd`/libs

#wget https://archive.apache.org/dist/kafka/3.0.0/kafka_2.13-3.0.0.tgz -P $KAFKA_PATH


#tar -xvzf $KAFKA_PATH/*.tgz

DIR_NAME=`ls $KAFKA_PATH | grep -v .tgz` 

KAFKA_BIN_PATH=${KAFKA_PATH}/${DIR_NAME}'/bin'


${KAFKA_BIN_PATH}/zookeeper-server-start.sh ${KAFKA_BIN_PATH}/../config/zookeeper.properties &> /dev/null & 
${KAFKA_BIN_PATH}/kafka-server-start.sh ${KAFKA_BIN_PATH}/../config/server.properties &> /dev/null & 





set +x 
