#!/bin/bash

kubectl create configmap --from-file prometheus.yml prometheus-configuration
kubectl create configmap --from-file alert-manager.yaml alert-configmap
kubectl create configmap --from-file rules.yaml rules-config
kubectl create sa prometheus
kubectl create token prometheus
