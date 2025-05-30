## 02 API Deployment

#### Objective

This document explains the most important aspects of 02_api_deployment.py.

#### Instructions for Code Execution

Open 02_api_deployment.py in your Cloudera AI Session. Familiarize yourself with the code. Then open mlops.py and also familiarize yourself with the code.

Next, reutrn to 02_api_deployment.py and press the play button in order to run the whole script. You will be able to observe code output on the right side of your screen.

#### Code Highlights

* Line 46: the "ModelDeployment" class is imported from the "mlops" util. This util has been placed in the "/home/cdsw" folder.  

* Line 49: the Cloudera AI API client is instantiated. The API provides you with over 100 Python methods to execute actions such as creating projects, launching jobs, and a lot more. In this example, the API is used to "list_projects()".

* Line 62: the API Client is passed as an argument to the ModelDeployment instance. The mlops.py util includes a few methods that extend and override API methods. Typically, Cloudera AI Machine Learning Engineers create Python Interfaces to build custom MLOps pipelines as required by their use case.

* Line 68: the latest MLFlow Experiment Run is used to register the Model in the Cloudera AI MLFlow Registry.

* Lines 74, 78, 81: the registered Model is used to create a new Cloudera AI Model Deployment. The Model is first created, then built, and finally deployed.

#### Summary

In this lab you used Cloudera AI APIv2 allows you to programmatically execute actions within Cloudera AI Workspaces. You can use the API with plain curl CLI statements, or the Python Wrapper which is a lib that is preinstalled in every Cloudera Runtime. The API can be used both from 3rd party systems that are external to the Cloudera AI Workspace, and within the Cloudera AI Workspace.

Cloudera AI Data Scientists leverage the API to build MLOPs Pipelines. In this lab you used a simple Python Interface to override API methods in order to build a standardized MLOps pipeline to register an Experiment Run in the MLFlow Registry, and then deploy an API Endpoint for model serving.

#### Related Articles

* To learn more about Cloudera AI Model Deployments:
  * [Cloudera AI Model Deployment with MLFlow and APIv2 Article](https://community.cloudera.com/t5/Community-Articles/CML-Model-Deployment-with-MLFlow-and-APIv2/ta-p/385656)
  
* To learn more about the Cloudera AI API:
  * [Cloudera AI APIv2](https://docs.cloudera.com/machine-learning/cloud/api/topics/ml-api-v2.html)
  * [Cloudera AI REST API Reference](https://docs.cloudera.com/machine-learning/cloud/rest-api-reference/index.html)
  * [Cloudera AI API v2 AMP](https://github.com/cloudera/CML_AMP_APIv2)
