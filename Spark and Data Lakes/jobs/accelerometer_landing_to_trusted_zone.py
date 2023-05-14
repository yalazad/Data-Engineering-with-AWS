import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Customer trusted
Customertrusted_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="yaa",
    table_name="customer_trusted",
    transformation_ctx="Customertrusted_node1",
)

# Script generated for node S3 Accelerometer landing
S3Accelerometerlanding_node1677265709827 = (
    glueContext.create_dynamic_frame.from_options(
        format_options={"multiline": False},
        connection_type="s3",
        format="json",
        connection_options={
            "paths": ["s3://udacity-yaa/accelerometer/landing/"],
            "recurse": True,
        },
        transformation_ctx="S3Accelerometerlanding_node1677265709827",
    )
)

# Script generated for node JoinTables
JoinTables_node2 = Join.apply(
    frame1=Customertrusted_node1,
    frame2=S3Accelerometerlanding_node1677265709827,
    keys1=["email"],
    keys2=["user"],
    transformation_ctx="JoinTables_node2",
)

# Script generated for node Drop Fields
DropFields_node1677265889234 = DropFields.apply(
    frame=JoinTables_node2,
    paths=[
        "phone",
        "email",
        "sharewithfriendsasofdate",
        "sharewithpublicasofdate",
        "sharewithresearchasofdate",
        "customername",
        "birthday",
        "serialnumber",
        "registrationdate",
        "lastupdatedate",
    ],
    transformation_ctx="DropFields_node1677265889234",
)

# Script generated for node S3 accelerometer trusted
S3accelerometertrusted_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1677265889234,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://udacity-yaa/accelerometer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="S3accelerometertrusted_node3",
)

job.commit()
