# 11. MLOps Skilling Course

A 26-session practical skilling course covering the MLOps toolchain end to end:
experiment tracking, data versioning, monitoring, containerized deployment, CI/CD,
cloud ML platforms (AWS SageMaker, GCP Vertex AI), explainability, and a set of
domain capstones that combine everything into a single pipeline.

Each session is a self-contained, terminal-based Markdown guide that builds a small
project from scratch: an overview of what you will build and why, numbered steps
(virtual environment, pinned `requirements.txt`, folder structure, the scripts, the
commands to run and their expected output), a **Common errors and fixes** table, and
**Exercises**. Scripts are run as modules from the project root
(`python -m src.train`), and most guides include pytest tests.

## Working locally vs. in the cloud

Most sessions run fully locally with no account or credentials needed: MLflow, DVC,
Evidently, Deepchecks, SHAP, FastAPI/Flask, BentoML and FLAML are all open-source.
Sessions tied to a cloud platform (AWS SageMaker, GCP Vertex AI / Cloud Run /
Cloud Build, DagsHub, GKE) still run everything up to the cloud step locally, then
say clearly where costs start and end with a clean-up step. Read each guide's
**Prerequisites** line first.

## Delivery plan

| # | Session | CO |
|---|---|---|
| 1 | Versioning and Tracking Machine Learning Models using MLflow | CO1 |
| 2 | Implementing Data Versioning Using DVC | CO1 |
| 3 | Building a Shared Repository with DagsHub and MLflow for Collaborative MLOps | CO1 |
| 4 | Building and Automating Machine Learning Models Using AutoML with Vertex AI | CO1 |
| 5 | Monitoring Model Explainability and Data Drift using Evidently AI | CO2 |
| 6 | Creating and Deploying Containerized ML Applications using Docker, Flask/FastAPI, and Kubernetes on Google Cloud | CO2 |
| 7 | Developing and Deploying APIs for ML Models | CO2 |
| 8 | Building and Deploying ML-Powered Web Applications using Flask and AWS SageMaker | CO3 |
| 9 | Deploying Automated Machine Learning (AutoML) Services using AWS SageMaker | CO3 |
| 10 | CI for ML Models with GitHub Actions | CO3 |
| 11 | Ensuring Data and Model Integrity using Deepchecks | CO4 |
| 12 | Scalable end-to-end MLOps pipelines using Google Vertex AI, with smart analytics and real-time model monitoring | CO4 |
| 13 | End-to-end MLOps pipeline to deploy and monitor ML models and LLM-based applications on GCP | CO4 |
| 14 | Automated MLOps pipeline for retraining and deploying models using CI/CD with GCP tools | CO4 |
| 15 | End-to-End MLOps Pipeline for Smart Healthcare Monitoring | CO5 |
| 16 | MLOps Pipeline for Intelligent Surveillance System | CO5 |
| 17 | Automated Model Retraining System using Data Drift Detection | CO5 |
| 18 | Cloud-Based MLOps Pipeline using Google Cloud Vertex AI | CO5 |
| 19 | End-to-End MLOps Pipeline on Amazon Web Services | CO5 |
| 20 | MLOps for Medical Image Analysis using Deep Learning | CO5 |
| 21 | Real-Time IoT Predictive Maintenance using MLOps | CO5 |
| 22 | Explainable AI Pipeline with SHAP and Model Monitoring | CO5 |
| 23 | Automated ML Deployment using BentoML and Docker | CO5 |
| 24 | CI/CD Pipeline for Machine Learning using GitHub Actions | CO5 |
| 25 | AutoML-Based Smart Prediction System with Deployment | CO5 |
| 26 | MLOps Pipeline for Real-Time Fraud Detection | CO5 |

## Setup

Each guide creates its own project folder and virtual environment with Python 3.11
and installs exactly the versions it lists in its `requirements.txt`. Library versions
differ between sessions on purpose (for example, sessions that deploy to managed
scikit-learn containers pin the container's scikit-learn version), so keep one virtual
environment per session rather than one for the whole course.
