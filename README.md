🚀 Grafana + AKS Deployment Summary -project 🧭 1. Launch AKS Cluster

Go to Azure Portal → Kubernetes Services
Create and launch your AKS cluster
🖥️ 2. Prepare the VM sudo su apt update apt install docker.io -y

🔧 3. Install Azure CLI curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

⚙️ 4. Install kubectl curl -LO https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256" echo "$(cat kubectl.sha256) kubectl" | sha256sum --check



🔗 5. Connect to AKS Cluster az aks get-credentials --resource-group --name

📦 6. Install Prometheus + Grafana via Helm helm repo add prometheus-community https://prometheus-community.github.io/helm-charts helm repo update helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace



✅ 7. Verify Pods Are Running kubectl --namespace monitoring get pods -l "release=prometheus"

🛠️ 8. Create Azure Container Registry

Create ACR named aneeshcr in Azure Portal or via CLI
🐍 9. Clone and Build Python App git clone https://github.com/akshu20791/aks-python-app-project-prometheus-grafana/ cd aks-python-app-project-prometheus-grafana docker build --tag first-app:v2 . docker tag first-app:v2 aneeshcr.azurecr.io/first-app:v2 docker images



🔐 10. Authenticate and Push to ACR az acr login --name aneeshcr docker push aneeshcr.azurecr.io/first-app:v2

🔗 11. Attach ACR to AKS az aks update -n ANEESH-AKS -g --attach-acr aneeshcr

📄 12. Deploy App to AKS kubectl apply -f firstapp.yaml kubectl get pods kubectl apply -f firstappservice.yaml kubectl get svc

📡 13. Expose Grafana via LoadBalancer kubectl get svc -n monitoring kubectl edit svc prometheus-grafana -n monitoring

Change type: ClusterIP to type: LoadBalancer

🌐 14. Access Grafana kubectl get svc -n monitoring

Use the external IP shown to open Grafana in your browser.

🔐 15. Get Grafana Credentials kubectl get secret prometheus-grafana -n monitoring -o jsonpath="{.data.admin-password}" | base64 --decode ; echo



Username: admin


<img width="1756" height="869" alt="image" src="https://github.com/user-attachments/assets/c2a89331-15b7-4cea-a407-a157f7d38081" />
