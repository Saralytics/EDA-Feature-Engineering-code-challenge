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

Run `docker-compose up` inside airflow directory to see the example. Default username: airflow, default password: airflow. Filter by tag 'ml' to easily find the job named `ml-etl-pipeline`.

Here is what it looks like: 
![alt text](https://github.com/Saralytics/myproject/blob/main/pictures/airflow_tree_view.png)

![alt text](https://github.com/Saralytics/myproject/blob/main/pictures/airflow_graph_view.png)


# Assumptions

When normalizing all salaries to hourly bases: 

- Assumption: 8 working hours per day, 22 working days per month 

- Annual salary -> salary / (22*12*8)

- Daily salary -> salary / (8)


# Considerations

1. Adding sklearn library 

**Apart from manually select features, we can analyze feature importance automatically using machine learning techniques or feature selection libraries, which is not covered in this notebook.**
removign outliers

2. Text processing could be more clean 
right now I use simplified assumption 

bag of words, TF-IDF, word embeddings,

entity recognition , text summarization

and we can further perform lemmatization: so communicate, communication, communicating will be lemmatized to the same word: communicate 

3. **Heuristic: if a column has more than 50% null values, drop that column, otherwise we try to impute**

4. Categorical variables encoding: I used one-hot encoding in the notebook, however there are many different types of encoding we can use. For instance, target encoding strategy will encode a categorical value based on the target value.

# Learnings

Always progress in small steps, after making even a small change, make sure the outcome is as expected before progressing

Useful to use excel/googlesheet to study at a small sample of data 

There are many techniques in NLP 





