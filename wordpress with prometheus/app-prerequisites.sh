#!/bin/bash

kubectl create configmap --from-file prometheus.yml prometheus-configuration
kubectl create configmap --from-file alertmanager.yml alert-config
kubectl create configmap --from-file rules.yaml rules-config
kubectl create sa prometheus
kubectl create token prometheus
git clone https://github.com/kubernetes/kube-state-metrics.git /root/kube
kubectl apply -f /root/kube/examples/standard
