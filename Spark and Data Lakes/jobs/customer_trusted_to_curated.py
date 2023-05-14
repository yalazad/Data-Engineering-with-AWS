import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 stepTrainer landing
S3stepTrainerlanding_node1677282376713 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://udacity-yaa/step_trainer/landing/"],
        "recurse": True,
    },
    transformation_ctx="S3stepTrainerlanding_node1677282376713",
)

# Script generated for node S3 customer trusted
S3customertrusted_node1677281895632 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://udacity-yaa/customers/trusted/"],
        "recurse": True,
    },
    transformation_ctx="S3customertrusted_node1677281895632",
)

# Script generated for node Renamed keys for Join
RenamedkeysforJoin_node1677282446739 = ApplyMapping.apply(
    frame=S3stepTrainerlanding_node1677282376713,
    mappings=[
        ("sensorReadingTime", "long", "`(right) sensorReadingTime`", "long"),
        ("serialNumber", "string", "`(right) serialNumber`", "string"),
        ("distanceFromObject", "int", "`(right) distanceFromObject`", "int"),
    ],
    transformation_ctx="RenamedkeysforJoin_node1677282446739",
)

# Script generated for node Join
Join_node2 = Join.apply(
    frame1=S3customertrusted_node1677281895632,
    frame2=RenamedkeysforJoin_node1677282446739,
    keys1=["serialNumber"],
    keys2=["`(right) serialNumber`"],
    transformation_ctx="Join_node2",
)

# Script generated for node Drop Fields
DropFields_node1677282802891 = DropFields.apply(
    frame=Join_node2,
    paths=[
        "`(right) sensorReadingTime`",
        "`(right) serialNumber`",
        "`(right) distanceFromObject`",
    ],
    transformation_ctx="DropFields_node1677282802891",
)

# Script generated for node Drop Duplicates
DropDuplicates_node1677282832721 = DynamicFrame.fromDF(
    DropFields_node1677282802891.toDF().dropDuplicates(["email"]),
    glueContext,
    "DropDuplicates_node1677282832721",
)

# Script generated for node S3 Customer curated
S3Customercurated_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropDuplicates_node1677282832721,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://udacity-yaa/customers/curated/",
        "partitionKeys": [],
    },
    transformation_ctx="S3Customercurated_node3",
)

job.commit()
