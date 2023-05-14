import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
import re
from pyspark.sql import functions as SqlFuncs

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 Customer landing
S3Customerlanding_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://udacity-yaa/customers/landing/"],
        "recurse": True,
    },
    transformation_ctx="S3Customerlanding_node1",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = Filter.apply(
    frame=S3Customerlanding_node1,
    f=lambda row: (not (row["shareWithResearchAsOfDate"] == 0)),
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node Drop Duplicates
DropDuplicates_node1677276760569 = DynamicFrame.fromDF(
    ApplyMapping_node2.toDF().dropDuplicates(["email", "customerName"]),
    glueContext,
    "DropDuplicates_node1677276760569",
)

# Script generated for node S3 customer trusted
S3customertrusted_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropDuplicates_node1677276760569,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://udacity-yaa/customers/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="S3customertrusted_node3",
)

job.commit()
