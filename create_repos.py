import requests
import json


ARTIFACTORY_URL = "https://trialo3gzzj.jfrog.io/artifactory"
API_USER = "eden.zanani@walla.com"
API_PASSWORD = "APFw2X9cqpuJUktNi1rn6yzCAN"

HEADERS = {"Content-Type": "application/json"}

def create_repo(repo_key, repo_type="docker"):
    url = f"{ARTIFACTORY_URL}/api/repositories/{repo_key}"
    if repo_type == "docker":
        payload = {"rclass":"local", "packageType":"docker", "repoLayoutRef":"simple-default"}
    else:
        payload = {"rclass":"local", "packageType":"generic"}
    resp = requests.put(url, auth=(API_USER, API_PASSWORD), headers=HEADERS, data=json.dumps(payload))
    if resp.status_code in [200, 201]:
        print(f"Repository {repo_key} created successfully!")
    elif resp.status_code == 400 and "already exists" in resp.text:
        print(f"Repository {repo_key} already exists.")
    else:
        print(f"Error creating {repo_key}: {resp.status_code} {resp.text}")

if __name__ == "__main__":
    create_repo("docker-local", "docker")
    create_repo("generic-local", "generic")

  
