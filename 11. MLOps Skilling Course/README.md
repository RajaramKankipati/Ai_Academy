# 11. MLOps Skilling Course

A 26-session practical skilling course covering the MLOps toolchain end to end:
experiment tracking, data versioning, monitoring, containerized deployment, CI/CD,
cloud ML platforms (AWS SageMaker, GCP Vertex AI), explainability, and a set of
domain capstones that combine everything into a single pipeline.

Each notebook is a self-contained, step-by-step lab: a short "what you'll build and
why" intro, numbered steps with runnable code, and a wrap-up of what to try next.

## Working locally vs. in the cloud

Most sessions run fully locally with no account or credentials needed — MLflow, DVC,
Evidently, Deepchecks, SHAP, FastAPI/Flask, and FLAML AutoML are all open-source and
installable via `poetry install`. A handful of sessions are inherently tied to a
specific cloud platform (AWS SageMaker, GCP Vertex AI, DagsHub, a Kubernetes cluster).
For those, the notebook contains complete, correct code plus a clearly marked
**"Prerequisites"** cell listing the account/credentials/hardware you need — read that
cell first, since the code will not run without them in this repository's sandbox.

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
| 10 | Implementing CI/CD Pipelines with GitHub Actions for MLOps | CO3 |
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

## Follow-along guides

Some sessions have a companion terminal-based walkthrough alongside the notebook, for
practicing the raw commands yourself instead of running them from Python:

- [`2b. DVC Follow-Along Guide.md`](2b.%20DVC%20Follow-Along%20Guide.md) — DVC basics,
  the `get`/`import`/`update` data-management commands, and a multi-stage pipeline
  tutorial, as a plain sequence of shell commands with explanations.
- [`3b. DagsHub Collaborative MLOps Follow-Along Guide.md`](3b.%20DagsHub%20Collaborative%20MLOps%20Follow-Along%20Guide.md) —
  a two-person team workflow (Alice versions the dataset with DVC, trains, and
  pushes; Bob pulls the code *and* the data, reviews, extends, and they jointly
  promote the winning model) using DagsHub, GitHub, DVC, and MLflow together, with
  an explanation of what each tool is responsible for and why none of them
  substitutes for the others.

## Setup

```bash
poetry install
poetry run jupyter notebook
```

Sessions that need extra packages beyond the base `poetry install` (DVC, Evidently,
Deepchecks, SHAP, FLAML, BentoML, boto3, google-cloud-aiplatform) say so in their own
first code cell — install them as you reach that session rather than all up front.
