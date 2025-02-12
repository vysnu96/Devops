#!/bin/bash
kubectl create configmap --from-file prometheus.yml prometheus-configuration
kubectl create configmap --from-file alertmanager.yml alert-config
kubectl create configmap --from-file rules.yaml rules-config
kubectl create sa prometheus
TOKEN=$(kubectl create token prometheus)
sed -i "s|kubernetes-nodes-bearer-token|$TOKEN|g" prometheus.yml
