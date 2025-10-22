🚀 Grafana + AKS Deployment Summary -project 🧭 1. Launch AKS Cluster

Go to Azure Portal → Kubernetes Services
Create and launch your AKS cluster


🖥️ 2. On the ubuntu VM 
#sudo su 
#apt update 
#apt install docker.io -y

🔧 3. Install Azure CLI
# curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

⚙️ 4. Install kubectl 
# curl -LO https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl 
# curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
# echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check



🔗 5. Connect to AKS Cluster
# az login --use-device-code
Login here - https://microsoft.com/devicelogin and enter the code shows in the console and validate with username--> enter the subscription on the console
Run the cmd in ubuntu console which is  shows when you click on AKS connect (2 cmds)
# az account set --subscription <subsription id>
# az aks get-credentials --resource-group <RG name> --name <AKS name> --overwrite-existing

📦 6. Install Prometheus + Grafana via Helm
# snap install helm --classic
# helm repo add prometheus-community https://prometheus-community.github.io/helm-charts 
# helm repo update
# helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace


✅ 7. Verify Pods Are Running 
# kubectl --namespace monitoring get pods -l "release=prometheus"
or we can go to AKS --> workloads and check the namespace "monitoring"

🛠️ 8. Create Azure Container Registry

Create ACR named xxxx in Azure Portal or via CLI
🐍 9. Clone and Build Python App 
# git clone https://github.com/akshu20791/aks-python-app-project-prometheus-grafana/ 
# cd aks-python-app-project-prometheus-grafana 
# docker build --tag first-app:v2 . 
# docker tag first-app:v2 shaaksacr.azurecr.io/first-app:v2
# docker images --- > to check the fist-app images are created or not


🔐 10. Authenticate and Push to ACR 
# az acr login --name aneeshcr 
# docker push aneeshcr.azurecr.io/first-app:v2 ( make sure right image is pushing - this can be found in docker images cmd)

🔗 11. Attach ACR to AKS 
# az aks update -n ANEESH-AKS -g <RG name> --attach-acr <ACR name>

📄 12. Deploy App to AKS
# kubectl apply -f firstapp.yaml
# kubectl get pods 
# kubectl apply -f firstappservice.yaml 
# kubectl get svc

📡 13. Expose Grafana via LoadBalancer 
# kubectl get svc -n monitoring
# kubectl edit svc prometheus-grafana -n monitoring

Change type: ClusterIP to type: LoadBalancer

<img width="1498" height="1040" alt="image" src="https://github.com/user-attachments/assets/87842403-5104-4e1b-aff7-637cbce2eb5a" />


🌐 14. Access Grafana kubectl get svc -n monitoring

Use the external IP shown to open Grafana in your browser.

🔐 15. Get Grafana Credentials 
# kubectl get secret prometheus-grafana -n monitoring -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

Username: admin


<img width="1756" height="869" alt="image" src="https://github.com/user-attachments/assets/c2a89331-15b7-4cea-a407-a157f7d38081" />
