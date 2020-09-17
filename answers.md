# Challenge

## Answers

### Nginx 
Just added a new location/endpoint with the stub_status. It's available at the default.conf file.

### Docker
There are two versions of the Dockerfile. One using a custom prebuilt image (nginx:1.19.2-alpine) from Nginx Docker Hub repo where they use alpine which is a very lightweight Linux OS. The second is made from a blank alpine image and installing Nginx manually (I didn't manage to install the specified version because the latest available via commands is older)

I consider the Dockerfile that uses the prebuilt image is just better because it simplifies the process of the Nginx installation.

Then I move the default.conf local file to the path /etc/nginx/conf.d inside the container and redirect then, the access and error logs to stdout and stderr respectively.

Obviously I expose the port 80 to have connectivity in the local machine together with mapping ports in the docker run command.

Finally, to solve an error regarding nginx I created the path /run/nginx to avoid that.

### Kubernetes
Used minikube to create the cluster locally to test the deployment.

Once I got all the environment set, I started build the yaml file of the deploy. As demanded, you can specify the amount of cpu and memory the pods will be consuming.

You can see the code at the deploy.yaml file.

Once I got all set, I just had to apply the yaml into the cluster with kubectl.

### Monitoring
Just a short easy script with python where I used the requests library to get the body of the basic_status endpoint. Then split by lines, get the first one, split by the ":" character and then take the number.

### Logging
I got the logs executing the docker logs command specifying the container. Then I split by lines and then get the lines that starts by my local IP and then get the status code.

Both the monitoring and logging script i would put them on a cron to increase the automation of the process.

### CI/CD Pipeline
Honestly I would liked to test that on a real Jenkins or other CI/CD platform environment because I think I can show more of myself in a real Jenkins environment than in this Jenkinsfile. Just divided the pipeline on four stages (the sections you demanded me).

In each stage (Docker build , Docker deploy, Kubernetes deploy and postscripts) I executed basically, the commands I executed in my machine.

## Commands

-> Build the image (change directory to the root path of the repo)
		$ docker build -t custom_nginx:1.19.10 .

	-> Run the container
		$ docker run -p 80:80 --name custom_nginx_container custom_nginx:1.19.10

	-> Create the cluster with minikube
		$ sudo minikube start --driver=none

	-> Deploy the yaml file into the cluster
		$ kubectl apply -f deploy.yaml

	-> See deployment details
		$ kubectl describe deployment customnginx-deployment

	-> Get the status of the pods
		$ kubectl get pods -l app=customnginx

	-> Execute python monitoring script (I would put the script in a cron actually)
		$ python3 monitoring.py




