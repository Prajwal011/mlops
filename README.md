Steps to run project

1. From repository "" copy contents of template.py and run in vscode(it'll create all files necessary).
2. Create virtual env

    2a. create a conda env using :
        conda create -n proj_name python=3.10.6 -y

    2b. Activate conda using:
        conda activate proj_name
4. Copy requirements.txt and run it: 
  pip install -r requirements.txt
5. Copy paste content from each file and folder from repository. Make changes in config/config.yaml navigate and change 
```
mlflow_info:
    tracking_uri: ## visit https://dagshub.com/ create account and follow given steps to generate uri https://dagshub.com/docs/integration_guide/mlflow_tracking/ 
    tracking_username: dagshub_username
    tracking_password: dagshub_password
```
