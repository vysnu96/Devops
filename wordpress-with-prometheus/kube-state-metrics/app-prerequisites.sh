#!/bin/bash
git clone https://github.com/kubernetes/kube-state-metrics.git /root/kube
kubectl apply -f /root/kube/examples/standard
