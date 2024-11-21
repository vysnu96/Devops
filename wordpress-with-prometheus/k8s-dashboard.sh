#!/bin/bash
kubectl apply -n portainer -f https://downloads.portainer.io/ce2-21/portainer.yaml
kubectl apply -f https://downloads.portainer.io/ce2-21/portainer-agent-k8s-nodeport.yaml