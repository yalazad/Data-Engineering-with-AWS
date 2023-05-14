CREATE EXTERNAL TABLE IF NOT EXISTS `yaa`.`customer_landing` (
  `serialNumber` string,
  `shareWithPublicAsOfDate` bigint,
  `birthDay` date,
  `registrationDate` bigint,
  `shareWithResearchAsOfDate` bigint,
  `customerName` string,
  `email` string,
  `lastUpdateDate` bigint,
  `phone` string,
  `shareWithFriendsAsOfDate` bigint
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'ignore.malformed.json' = 'FALSE',
  'dots.in.keys' = 'FALSE',
  'case.insensitive' = 'TRUE',
  'mapping' = 'TRUE'
)
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://udacity-yaa/customers/landing/'
TBLPROPERTIES ('classification' = 'json');