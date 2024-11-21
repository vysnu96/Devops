#!/bin/bash
kubectl create configmap --from-file prometheus.yml prometheus-configuration
kubectl create configmap --from-file alertmanager.yml alert-config
kubectl create configmap --from-file rules.yaml rules-config
kubectl create sa prometheus
kubectl create token prometheus