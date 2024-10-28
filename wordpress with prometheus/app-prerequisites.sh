#!/bin/bash

kubectl create configmap --from-file prometheus.yml prometheus-configuration
kubectl create sa prometheus
kubectl create token prometheus