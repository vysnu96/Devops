#!/bin/bash
git clone https://github.com/nginxinc/kubernetes-ingress.git --branch v3.7.0
cd kubernetes-ingress
kubectl apply -f deployments/common/ns-and-sa.yaml
kubectl apply -f deployments/rbac/rbac.yaml
kubectl apply -f examples/shared-examples/default-server-secret/default-server-secret.yaml
kubectl apply -f deployments/common/nginx-config.yaml
kubectl apply -f deployments/common/ingress-class.yaml
kubectl apply -f https://raw.githubusercontent.com/nginxinc/kubernetes-ingress/v3.7.0/deploy/crds.yaml
kubectl apply -f deployments/deployment/nginx-ingress.yaml
kubectl create -f deployments/service/nodeport.yaml