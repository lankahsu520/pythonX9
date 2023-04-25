# -*- coding: utf-8 -*-
"""
 ***************************************************************************
 * Copyright (C) 2023, Lanka Hsu, <lankahsu@gmail.com>, et al.
 *
 * This software is licensed as described in the file COPYING, which
 * you should have received as part of this distribution.
 *
 * You may opt to use, copy, modify, merge, publish, distribute and/or sell
 * copies of the Software, and permit persons to whom the Software is
 * furnished to do so, under the terms of the COPYING file.
 *
 * This software is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY
 * KIND, either express or implied.
 *
 ***************************************************************************
"""
#https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
#pip3 install boto3
#pip3 install --target ./python boto3
import boto3
from pythonX9 import *
import botocore

AWS_SERVICE_S3="s3"
AWS_SERVICE_DYNAMODB="dynamodb"
REGION_US_WEST_1='us-west-1'

class awsP9_ctx(pythonX9):

	# A low-level client representing Amazon Simple Storage Service (S3)
	# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
	def s3_create_bucket(self, s3_bucket_name):
		self.s3_error_code = 0
		self.s3_bucket = None
		try:
			self.s3_bucket_name=s3_bucket_name
			self.s3_bucket = self.s3cli.create_bucket(Bucket=s3_bucket_name, CreateBucketConfiguration={'LocationConstraint': self.region})
			DBG_IF_LN(self, "create_bucket (s3://{})".format( s3_bucket_name ))
		except botocore.exceptions.ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, s3_bucket_name ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, s3_bucket_name ))
			self.s3_error_code = error_code
		return self.s3_bucket

	def s3_check_bucket(self, s3_bucket_name):
		self.s3_error_code = 0
		try:
			self.s3_response = self.s3cli.head_bucket(Bucket=s3_bucket_name)
			DBG_IF_LN(self, "head_bucket (s3://{})".format( s3_bucket_name ))
		except botocore.exceptions.ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, s3_bucket_name ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, s3_bucket_name ))
			self.s3_error_code = error_code
		return self.s3_error_code

	def s3_get_bucket_location(self, s3_bucket_name):
		self.s3_error_code = 0
		try:
			self.s3_response = self.s3cli.get_bucket_location(Bucket=s3_bucket_name)
			DBG_IF_LN(self, "get_bucket_location (s3://{})".format( s3_bucket_name ))
		except botocore.exceptions.ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, s3_bucket_name ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, s3_bucket_name ))
			self.s3_error_code = error_code
		return self.s3_response

	def s3_copy_object(self, s3_bucket_from, s3_object_from, s3_bucket_to, s3_object_to):
		self.s3_error_code = 0
		try:
			copy_source = {
				'Bucket': s3_bucket_from,
				'Key': s3_object_from
			}
			self.s3_bucket = self.s3src.Bucket(s3_bucket_to)
			self.s3_bucket.copy(copy_source, s3_object_to)
			DBG_IF_LN(self, "copy (s3://{}/{} -> s3://{}/{})".format(s3_bucket_from, s3_object_from, s3_bucket_to, s3_object_to));
		except botocore.exceptions.ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_from: {})".format( e.__str__(), error_code, s3_bucket_from ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_from: {})".format( e.__str__(), error_code, s3_bucket_from ))
			self.s3_error_code = error_code
		return self.s3_response

	def s3_delete_object(self, s3_bucket_name, s3_object_name):
		self.s3_error_code = 0
		try:
			self.s3_response = self.s3cli.delete_object(Bucket=s3_bucket_name, Key=s3_object_name)
			DBG_IF_LN(self, "delete_object (s3://{}/{})".format(s3_bucket_name, s3_object_name));
		except botocore.exceptions.ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {}, s3_object_name: {})".format( e.__str__(), error_code, s3_bucket_name, s3_object_name ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {}, s3_object_name: {})".format( e.__str__(), error_code, s3_bucket_name, s3_object_name ))
			self.s3_error_code = error_code
		return self.s3_response

	def s3_get_object(self, s3_bucket_name, s3_object_name):
		self.s3_error_code = 0
		try:
			self.s3_response = self.s3cli.get_object(Bucket=s3_bucket_name, Key=s3_object_name)
			DBG_IF_LN(self, "get_object (s3://{}/{})".format(s3_bucket_name, s3_object_name));
		except botocore.exceptions.ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {}, s3_object_name: {})".format( e.__str__(), error_code, s3_bucket_name, s3_object_name ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {}, s3_object_name: {})".format( e.__str__(), error_code, s3_bucket_name, s3_object_name ))
			self.s3_error_code = error_code
		return self.s3_response

	def s3_pull_object(self, s3_bucket_name, s3_object_name, local_name):
		self.s3_error_code = 0
		try:
			#self.s3cli.download_file(s3_bucket_name, s3_object_name, local_name)
			with open(local_name, 'wb') as f:
				self.s3cli.download_fileobj(s3_bucket_name, s3_object_name, f)
			DBG_IF_LN(self, "download_fileobj (s3://{}/{} -> ./{})".format(s3_bucket_name, s3_object_name, local_name));
		except botocore.exceptions.ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, s3_bucket_name ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, s3_bucket_name ))
			self.s3_error_code = error_code
		return self.s3_response

	def s3_put_object(self, s3_bucket_name, s3_object_name, local_name):
		self.s3_error_code = 0
		try:
			self.s3_response = self.s3cli.put_object(Body=local_name, Bucket=s3_bucket_name, Key=s3_object_name)
			DBG_IF_LN(self, "put_object (./{} -> s3://{}/{})".format(local_name, s3_bucket_name, s3_object_name));
		except botocore.exceptions.ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, self.s3_bucket_name ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, self.s3_bucket_name ))
			self.s3_error_code = error_code
		return self.s3_response

	# A low-level client representing Amazon DynamoDB
	# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html
	#db_create_table(TableName="Music", pk="Artist", sk="SongTitle")
	def db_create_table(self, TableName="", pk="", sk=""):
		self.db_response = ""
		try:
			if (TableName == ""):
				DBG_ER_LN(self, "TableName is Null !!!" )
			else:
				self.db_response = self.dbcli.create_table(
					AttributeDefinitions= [{
							'AttributeName': pk,
							'AttributeType': 'S'
						}, {
							'AttributeName': sk,
							'AttributeType': 'S'
						}
					],
					TableName=TableName,
					KeySchema=[{
							'AttributeName': pk,
							'KeyType': 'HASH'
						}, {
							'AttributeName': sk,
							'KeyType': 'RANGE'
						}
					],
					ProvisionedThroughput={
						'ReadCapacityUnits': 5,
						'WriteCapacityUnits': 5
					},
				)
			self.db_describe_table(TableName=TableName, status="CREATING")
			DBG_DB_LN(self, "{}". format(DBG_TXT_DONE) )
		except botocore.exceptions.ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, TableName: {})".format( e.__str__(), error_code, TableName ))
			self.db_error_code = error_code
		except ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, TableName: {})".format( e.__str__(), error_code, TableName ))
			self.db_error_code = error_code
		return self.db_response

	def db_delete_table(self, TableName=""):
		self.db_response = ""
		try:
			if (TableName == ""):
				DBG_ER_LN(self, "TableName is Null !!!" )
			else:
				self.db_describe_table(TableName=TableName, status="ACTIVE")
				self.db_response = self.dbcli.delete_table(TableName=TableName)
				retry = 10
				while (retry>0) and (self.db_describe_table(TableName=TableName) != ""):
					sleep(400/1000)
					retry-=1
				DBG_DB_LN(self, "{}". format(DBG_TXT_DONE) )
		except botocore.exceptions.ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, TableName ))
			self.db_error_code = error_code
		except ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, TableName ))
			self.db_error_code = error_code
		return self.db_response

	def db_describe_table(self, TableName="", status=""):
		self.db_response = ""
		try:
			if (TableName == ""):
				DBG_ER_LN(self, "TableName is Null !!!" )
			else:
				self.db_response = self.dbcli.describe_table(TableName=TableName)
				#DBG_WN_LN(self, "{}".format(self.db_response) )
				if ( status != "" ):
					retry = 10
					while (retry>0) and (self.db_response['Table']['TableStatus'] == status):
						self.db_response = self.db_describe_table(TableName=TableName)
						sleep(400/1000)
						retry-=1
				DBG_DB_LN(self, "{}". format(DBG_TXT_DONE) )
		except botocore.exceptions.ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, TableName ))
			self.db_error_code = error_code
		except ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, TableName ))
			self.db_error_code = error_code
		return self.db_response

	def db_list_tables(self, StartTableName="", limit=100):
		self.db_response =[]
		try:
			if (StartTableName == ""):
				self.db_response = self.dbcli.list_tables(Limit=limit)
			else:
				self.db_response = self.dbcli.list_tables(ExclusiveStartTableName=StartTableName, Limit=limit)
			DBG_DB_LN(self, "{}". format(DBG_TXT_DONE) )
		except botocore.exceptions.ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, StartTableName: {})".format( e.__str__(), error_code, StartTableName ))
			self.db_error_code = error_code
		except ClientError as e:
			error_code = e.response['Error']['Code']
			DBG_ER_LN(self, "{} (error_code:{}, StartTableName: {})".format( e.__str__(), error_code, StartTableName ))
			self.db_error_code = error_code
		return self.db_response

	def release(self):
		self.is_quit = 1

	def __init__(self, aws_service=AWS_SERVICE_S3, region=REGION_US_WEST_1, **kwargs):
		if ( isPYTHON(PYTHON_V3) ):
			super().__init__(**kwargs)
		else:
			super(awsP9_ctx, self).__init__(**kwargs)

		self._kwargs = kwargs
		self.region = region
		self.aws_service = aws_service

		DBG_IF_LN(self, "(region: {}, aws_service: {})".format( region, aws_service ))
		for service in aws_service:
			if ( service == "s3" ):
				self.s3src = boto3.resource("s3")
				self.s3cli = boto3.client("s3")
			elif ( service == "dynamodb" ):
				self.dbcli = boto3.client("dynamodb")
