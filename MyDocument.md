# Summary

## Steps and Techniques Used in This Project

#### 1. Exploratory data analysis (EDA)

1.1 Inspect the distribution of the dataset

1.2 Check if any column is obviously without meaning, or has only a single unique value

1.3 Study categorical variables: frequency, cardinality, plotting

1.4 Study continuous variables: are there outliers, what are the differences in distributions, etc.

#### 2. Preprocessing and Feature Engineering 

2.1 Handle Missing Values 

2.2 Handle outliers

2.3 Drop features 

2.4 Text processing 

2.5 Encoding categorical variables 

#### 3. Answering the challenges
#### 4. Tests

## Proposed Deployment

Use a git-based CI/CD pipeline:

For example: Code repo Github -> CI/CD framework Jenkins -> Kubernetes

Orchastration tool:
`Airflow is a great tool to manage the schedule and dependencies of pipelines 

Example pipeline in the `airflow` directory. 

Run `docker-compose up` inside airflow directory to see the example. Default username: airflow, default password: airflow 

Here is what it looks like: <insert picture>


# Considerations

1. Adding sklearn library 
2. Text processing could be more clean 

# Learnings



