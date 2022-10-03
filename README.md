
**The Monkey**

This is my approach of the exercise PodChaosMonkey.

The app is build in python, and uses the [Kubernetes Python Client](https://github.com/kubernetes-client/python).

To test this application please, follow the setup process

# Setup the Test Enviorment

The Helm Chart will deploy a simple app running the nginx container, with 5 replicas.

```
helm upgrade -i --create-namespace -n workloads apptest ./chart_app
```


# Build Container

Build the Docker image

```
docker build -t monkey:v2 .
```


# Deploy Monkey

Before deploying the helm chart, please validate the values of the chart:
* If the app namespace is different than workloads, change the value.
* Adjust the schedule of the cron job, accordingly.
* Add the docker registry where the container was pushed.

```
helm upgrade -i --create-namespace -n monkey monkey ./chart_monkey
```


# Destroy 

```
helm uninstall apptest
helm uninstall monkey
```

