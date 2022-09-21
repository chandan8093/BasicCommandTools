# Document Followed:
-https://devdojo.com/ruanbekker/setup-a-3-node-mongodb-replica-set-on-ubuntu

# Adding Private Adress To Hosts(change private IP)
sudo tee /etc/hosts
10.163.68.26 prod-mongodb-arbiter
10.163.68.12 prod-mongodb-1
10.163.68.9  prod-mongodb-2


log "Configure Mongodb"
sudoim /etc/mongod.conf
net:
  port: 27017
  bindIp: 127.0.0.1,10.163.68.26
operationProfiling:
  mode: "slowOp"
  slowOpThresholdMs: 50

security:
  authorization: enabled
  keyFile: /var/lib/mongodb-pki/keyfile

replication:
  replSetName: my-arbiter-replicaset

log "Note: change Bindip Private Adress"


log "Verify that the process has started"
sudo systemctl status mongod

Verify that the port is listening:
sudo netstat -tulpn | grep -E '(State|2950)'

#Initialize the MongoDB Replica Set:
>mongo --host 127.0.0.1 --port 27017
>use admin
>rs.initiate()
