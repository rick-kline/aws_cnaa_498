# LSE Demand Planning
A Cloud native ML application build

<b>I. Introduction</b>
<br>Electric Utilities or load serving entities (LSE) are responsible for providing load or energy demand forecast up to seven days into the future. The higher the accuracy, the more acurrately the regional transmission operators, (RTOs) can manage the overall transmission and electricty grid. In addition to contributing to grid safety and management, accurate forcast allow for better planning, better internal load management, reduced risk, informed whole sale energy purchase and sales and appropriate risk management and hedging related to supply and demand. While there are a multitude of factors to be consider better energy forecasting and demand planning by load serving entities can lead to increased profit, safety and customer care. 
<br>
There has been considerable research in the area of demand planning for LSEs and it should be noted that load forecasting is not a trivial exercise requiring considerable public and private data to achieve high accuracy. This project does not attempt to achieve the levels of accuracy that may be provided by more robust or commercial solutions, instead the goal of this project is to demonstrate an end to end, cloud native serverless MVP solution allowing for short term demand forcast using tools and services available on the Amazon Web Services platform.
<br>
Due to the size and availability of the required data, the solution focuses on the PJM RTO territory and specifically the DUQ zone of Duquesne Light Company LSE as shown in the graphic below. Duquesne Light serves energy loads in Pittsburge, PA and surrounding areas.
<br>
<br>![pjm_duq_territory](https://user-images.githubusercontent.com/64938088/120936066-ebb77500-c6d3-11eb-85bb-bff83be3ad8e.PNG)
<br>
<br>II. Data Sources
Two primary data sources have been secured with continued, intermittent data extraction from DataMiner2 API, the API provided by PJM RTO and historical and current weather data sourced for the API provided on openweathermap.org.  
<br>
<b>II. Functional / Technical Specification</b>
<br>
<br> As noted in the diagram below, the operational data store and data pipeline is responsible for extracting the data from the APIs and persisyting that data in Dynamo DB an AWS NoSQL db. Two primary lambda functions pull data from the APIs passing the extracted data to the final API responsible for interacting with the DynamoDB one table architecture. The lambdas responsible for sourcing the data are triggered by cloudwatch events at appropriate times of the day when additional data is available. These two lambdas triger the CRUD lambda as final processing to load the data via eithe a PUT or UPDATE operation. 
<br>
<br>![Serverless_operational_data_store_pipeline](https://user-images.githubusercontent.com/64938088/120934295-c888c780-c6cb-11eb-8e82-47422eea9b54.PNG)
<br>
<br>Noted in the graphic below, are the high level details of the Serverless ETL and Data Staging process. Initially an AWS Glue crawler crawls the DynamoDB table instantiating the initial table in the Glue catalog. At this point the data is not available to Athena. Subsequently two Glue jobs are required to secure, transform and load the data to S3 buckets in both Parquet and JSOn formats. The resulting buckets/files are again crawled making the source data available to Athena via the Glue data catalog. Finally, due to the presentation of the data available from Dynamo DB, an Athena view id created making the complete data set available and queryable in a clean and usable format.
<br>
<br>![serverless_etl_data_staging](https://user-images.githubusercontent.com/64938088/120934516-8ad86e80-c6cc-11eb-96dc-024abd7aa555.PNG)

<br>III. Modeling & Inference
<br> The jupyter notebook, (DUQ-Demand-Planning) available in this repository demostrates the consumption of the data available in the Athena serverless datawarehouse for the purpose of data preparation and model construction. Initially the data is prepared and a model is constructed manually taking into acccount the quadratic relationship between temperature and energy demand and also the interactions between energy demand by month and season, day of week and hour of day. The manually constructed model generates a MAPE for out of sample prediction of 10.0. Much nore could be done from a modeling perspective toimprove accuracy. Finally, the data is prepared for in a Sagemaker, AutoML / AutoPilot model development. The Autopilot experiment is created and executed in JupyterLab via Sagemaker Studio. The resulting model is deployed with an model endpoint created. Also shown in the notebook is the invocation of enpoint to request predictions for the out-of-sample- test data withheld from the training data. Noted in the notebook, the autoML generated model produces a MAPE of approximately 20.    


<br>IV. Conclusion
<br> This project demostrates an end-to-end cloud native serverless ML application build utilizing AWS Cloud native tools, functionality and services. The solution utilizes AWS lambda functions to source API data and interact with dynamoDB in building an operational data store. The data is further extracted and transformed for use by AWS Glue crawlers, AWS Gle jobs and the AWS Glue data catalog. The data is presented to the end user via AWS Athena serverless database / warehouse constructed on S3 data. Finally an AutoPilot XGboost model is created and deployed along with an endpoint allowing for prediction request. Both the manually created model and the AutoPilot model are in need of improvement however the model building process in both cases has provide considerable insight regarding how each might be improved.    
