# Devops
Contains yaml files for the kubernetes deployment

Pre-requisites:
You should have a atleast single node cluster. I tried this on the Ubuntu installed in the VirtualBox.
For cluster setup, I used microk8s with ingress enabled.
Basic experience with linux terminal and commands

Setup:
1. Install ubuntu in the virtual box along with root access.
2. Then update the repo using apt-get update.
3. Install microk8s using the command snap install microk8s --classic
4. Enable the ingress controller provided by microk8s using the command microk8s enable ingress
5. Then apply the deployment using the file java-tomcat-ingress.yaml
6. Then access the two different apps in the browser by entering localhost/apple and localhost/mango
