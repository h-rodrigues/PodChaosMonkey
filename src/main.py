import random
import sys
from kubernetes import client, config
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


victim_pod_running = []
namespace = sys.argv[1] 

# Load kubeconfig 
config.load_incluster_config()
#Use for passing the kubeconfig local environment
#config.load_kube_config()

#call API
client = client.CoreV1Api()

#Get All pods in The Namespace 

def get_victim_pod(client, namespace):
        pod_list = client.list_namespaced_pod(namespace)

        return pod_list.items

#Delete The selected POD 
def delete_victim_pod(client, victim_pod):
    return client.delete_namespaced_pod(
        name=victim_pod.metadata.name,
        namespace=victim_pod.metadata.namespace
    )
    
   

def main( ):

        print(f"The Monkey will be loose in the namespace: {namespace}")
        
        victim_pod = get_victim_pod(client, namespace)
        
        if victim_pod:
            print(f"The Monkey found this pods to play") 

            for item in victim_pod:
                print(item.metadata.name + " " + item.status.phase)

            print(f"The Monkey is choosing a pod to play") 

            target_pod = random.choice(victim_pod)
            
            print(f"The Monkey selected this {target_pod.metadata.name} pod to play , say Goodbye to the pod")

            delete_pod = delete_victim_pod(client, target_pod)

        else:
            print(f"The Monkey didn't found any pod in the namespace: {namespace} Monkey is sad and says Goodbye")


if __name__ == '__main__':
    main()    