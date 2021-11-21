# Amazon Vine Analysis

## Project Overview - Amazon Vine Analysis

AWS options sample datasets containing reviews for specific products.  For this analysis we used the reviews from the "Video Games" category.  With the data set we use PySpark to perform the ETL process to extract the dataset, transform the data, connect to an AWS RDS instance, and load the transformed data into pgAdmin. Next, we use PySpark to determine if there is any bias toward favorable reviews from Vine members in the dataset. The  summary of the analysis will be submitted to the SellBy stakeholders.

## Resources
-  Data Files: 
https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Video_Games_v1_00.tsv.gz

- Schema:
https://github.com/mfreel14/Amazon_Vine_Analysis/blob/ad077da2cdc6d8f190a368d24ef8f171c73f4b51/challenge_schema.sql

-  Software/Languages: Pyspark, Pandas, SQL, AWS, Google Collab


# Challenge Summary

## Amazon Vine Analysis - Results

How many Vine reviews and non-Vine reviews were there?

The total number of Vine reviews was 94.

The total number of non-Vine reviews was 40,471.

<img width="848" alt="Screen Shot 2021-10-14 at 4 00 09 PM" src="https://user-images.githubusercontent.com/691355/137406772-a63db244-163e-41c3-a281-5a96e872fa8f.png">

How many Vine reviews were 5 stars? How many non-Vine reviews were 5 stars?

The total number of Vine reviews that had 5 stars was 48.

The total number of non-Vine reviews that had 5 stars was 24,808.

<img width="706" alt="Screen Shot 2021-10-14 at 4 04 35 PM" src="https://user-images.githubusercontent.com/691355/137407076-ea74b947-c572-40e3-b780-594b1ca682a2.png">

What percentage of Vine reviews were 5 stars? What percentage of non-Vine reviews were 5 stars?

The percentage of Vine reviews that had 5 stars was 51.064%.

The percentage of non-Vine reviews that had 5 stars was 38.702%.


<img width="982" alt="Screen Shot 2021-11-21 at 3 11 06 PM" src="https://user-images.githubusercontent.com/691355/142782707-aa5f432c-9e90-4819-8082-a97f1e2d513a.png">

