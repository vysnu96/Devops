#!/bin/bash

kubectl create configmap --from-file prometheus-configuration-k8s.yaml prometheus-configuration
kubectl create sa prometheus
kubectl create token prometheus