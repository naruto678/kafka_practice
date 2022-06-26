
### Step 1: 
  wget https://dlcdn.apache.org/kafka/3.2.0/kafka_2.12-3.2.0.tgz -P '${KAFKA_PATH}/'

### Step 2: 
- unzip it with tar -xvzf <name of tar file >

### Start the zookeeper service 

Step 3: 
  cd into the bin directory of the unzipped tar file and run the followign commands to start the kafka-server at port 9092 . The zookeeper will run on 2021


cd bin 

and 
./zookeeper-server-start.sh ../config/zookeeper.properties &> /dev/null  & 
./kafka-server-start.sh ../config/server.properties  &> /dev/null & 


