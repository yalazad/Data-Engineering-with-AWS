# Data Pipelines with Airflow ( AWS )

> ## Udacity Data Engineer Nano Degree

## Project Overview
A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

They have decided to bring you into the project and expect you to create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. They have also noted that the data quality plays a big part when analyses are executed on top the data warehouse and want to run tests against their datasets after the ETL steps have been executed to catch any discrepancies in the datasets.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.

## Technical Overview
Project is implemented in AWS Cloud and uses the following, 
1. S3 Storage Buckets
1. AWS Redshift
1. Airflow
1. Python

## Goal
Build ETL Workflow using Airflow which should perform below tasks,
1. Read data from AWS S3 Buckets
1. Create & Load tables in AWS Redshift
1. Perform Data Quality Checks

## Project Specification

### **General**  
| CRITERIA                                                          | MEETS SPECIFICATIONS                                                                                                                                                       |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The dag and plugins do not give an error when imported to Airflow | DAG can be browsed without issues in the Airflow UI                                                                                                                        |
| All tasks have correct dependencies                               | The dag follows the data flow provided in the instructions, all the tasks have a dependency and DAG begins with a start_execution task and ends with a end_execution task. |

### **Dag configuration**  
| CRITERIA                               | MEETS SPECIFICATIONS                                                                                                                                                                                 |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Default_args object is used in the DAG | DAG contains default_args dict, with the following keys:   <ul> <li> Owner </li> <li> Depends_on_past </li> <li> Start_date </li> <li> Retries </li> <li> Retry_delay </li> <li> Catchup </li> </ul> |
| Defaults_args are bind to the DAG      | The DAG object has default args set                                                                                                                                                                  |
| The DAG has a correct schedule         | The DAG should be scheduled to run once an hour                                                                                                                                                      |
### **Staging the data**  
| CRITERIA                                                                           | MEETS SPECIFICATIONS                                                                                                         |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Task to stage JSON data is included in the DAG and uses the RedshiftStage operator | There is a task that to stages data from S3 to Redshift. (Runs a Redshift copy statement)                                    |
| Task uses params                                                                   | Instead of running a static SQL statement to stage the data, the task uses params to generate the copy statement dynamically |
| Logging used                                                                       | The operator contains logging in different steps of the execution                                                            |
| The database connection is created by using a hook and a connection                | The SQL statements are executed by using a Airflow hook                                                                      |

### **Loading dimensions and facts**  
| CRITERIA                                                                                           | MEETS SPECIFICATIONS                                                                                                         |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Set of tasks using the dimension load operator is in the DAG                                       | Dimensions are loaded with on the LoadDimension operator                                                                     |
| A task using the fact load operator is in the DAG                                                  | Facts are loaded with on the LoadFact operator                                                                               |
| Both operators use params                                                                          | Instead of running a static SQL statement to stage the data, the task uses params to generate the copy statement dynamically |
| The dimension task contains a param to allow switch between append and insert-delete functionality | The DAG allows to switch between append-only and delete-load functionality                                                   |

### **Data Quality Checks**  
| CRITERIA                                                                                         | MEETS SPECIFICATIONS                                                                            |
|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| A task using the data quality operator is in the DAG and at least one data quality check is done | Data quality check is done with correct operator                                                |
| The operator raises an error if the check fails pass                                             | The DAG either fails or retries n times                                                         |
| The operator is parameterized                                                                    | Operator uses params to get the tests and the results, tests are not hard coded to the operator |

### **Suggestions to Make Your Project Stand Out!**  
* Simple and dynamic operators, as little hard coding as possible
* Effective use of parameters in tasks
* Clean formatting of values in SQL strings
* Load dimensions with a subdag

## Project expected output
![alt text](./Working_DAG_with_correct_dependencies.png "Airflow")

## Initial DAG look
![alt text](./Project_DAG_in_Airflow_UI.png "Airflow")

## Final Airflow DAG
Below are the initial analysis on the expected output and python program templates provided, 
* Redshift tables are created outside of airflow. Looking at the ```create_tables.sql``` confirms it as CREATE statements are pure SQL not initialized to python variable and file extension is ```.sql``. 

* Following changes are made to the udacity expected output to perform everything in airflow itself.

    * Tasks to create Redshift tables are added
    * Used SUBDAG for dimension node and it does following: 

        * Create dimension table
        * Load dimension table
        * Verify table is not empty
