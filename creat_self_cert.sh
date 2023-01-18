#!/bin/bash

IP="192.168.10.11"
SUBJECT_CA="/C=RU/ST=Russia/L=Moscow/O=himinds/OU=CA/CN=$IP"
SUBJECT_SERVER="/C=RU/ST=Russia/L=Moscow/O=himinds/OU=Server/CN=$IP"
SUBJECT_CLIENT="/C=RU/ST=Russia/L=Moscow/O=himinds/OU=Client/CN=$IP"
DIR=$(pwd)

function generate_CA () {
   echo "$SUBJECT_CA"
   openssl req -x509 -nodes -sha256 -newkey rsa:2048 -subj "$SUBJECT_CA"  -days 365 -keyout ca.key -out ca.crt
}

function generate_server () {
   echo "$SUBJECT_SERVER"
   openssl req -nodes -sha256 -new -subj "$SUBJECT_SERVER" -keyout server.key -out server.csr
   openssl x509 -req -sha256 -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365
}

function generate_client () {
   echo "$SUBJECT_CLIENT"
   openssl req -new -nodes -sha256 -subj "$SUBJECT_CLIENT" -out client.csr -keyout client.key 
   openssl x509 -req -sha256 -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365
}

function copy_keys_to_broker () {
   echo "$DIR"
   sudo cp ca.crt "$DIR"/mosquitto/config/ca_certificates/
   sudo cp server.crt "$DIR"/mosquitto/config/ca_certificates/
   sudo cp server.key "$DIR"/mosquitto/config/ca_certificates/
}

function del_keys_pwd () {
   echo "$DIR"
   rm "$DIR"/*.crt
   rm "$DIR"/*.key
   rm "$DIR"/*.csr
}

generate_CA
generate_server
generate_client
copy_keys_to_broker
del_keys_pwd