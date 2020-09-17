node ('jenkins-node') {

    stage('Build docker image') {
        sh "docker build -t custom_nginx:1.19.10 <path to Dockerfile"
    }

    stage('Deploy container') {
        sh "docker run -p 80:80 --name custom_nginx_container custom_nginx:1.19.10"
    }

    stage('Deploy container into the cluster') {
        sh "kubectl apply -f deploy.yaml"
        sh "kubectl describe deployment customnginx-deployment"
        sh "kubectl get pods -l app=customnginx"
    }

    stage('Execute postscripts') {
        sh "python3 <path to scripts>/logging.py"
        sh "python3 <path to scripts>/monitoring.py"
    }
}



/* Stages

1. Build the docker image
2. Deploy it
3. Deploy it with kubernetes
4. Execute post scripts
