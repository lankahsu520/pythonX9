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
import boto3
from pythonX9 import *
import botocore

AWS_SERVICE_S3="s3"
REGION_US_WEST_1='us-west-1'

class awsX9_ctx(pythonX9):
	def s3_create_bucket(self, s3_bucket_name):
		self.s3_error_code = 0
		self.s3_bucket = None
		try:
			self.s3_bucket_name=s3_bucket_name
			self.s3_bucket = self.s3cli.create_bucket(Bucket=s3_bucket_name, CreateBucketConfiguration={'LocationConstraint': self.region})
			DBG_IF_LN(self, "create_bucket (s3://{})".format( s3_bucket_name ))
		except botocore.exceptions.ClientError as e:
			error_code = int(e.response['Error']['Code'])
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, s3_bucket_name ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = int(e.response['Error']['Code'])
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, s3_bucket_name ))
			self.s3_error_code = error_code
		return self.s3_bucket

	def s3_check_bucket(self, s3_bucket_name):
		self.s3_error_code = 0
		try:
			self.s3_response = self.s3cli.head_bucket(Bucket=s3_bucket_name)
			DBG_IF_LN(self, "head_bucket (s3://{})".format( s3_bucket_name ))
		except botocore.exceptions.ClientError as e:
			error_code = int(e.response['Error']['Code'])
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, s3_bucket_name ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = int(e.response['Error']['Code'])
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, s3_bucket_name ))
			self.s3_error_code = error_code
		return self.s3_error_code

	def s3_get_bucket_location(self, s3_bucket_name):
		self.s3_error_code = 0
		try:
			self.s3_response = self.s3cli.get_bucket_location(Bucket=s3_bucket_name)
			DBG_IF_LN(self, "get_bucket_location (s3://{})".format( s3_bucket_name ))
		except botocore.exceptions.ClientError as e:
			error_code = int(e.response['Error']['Code'])
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, s3_bucket_name ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = int(e.response['Error']['Code'])
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
			error_code = int(e.response['Error']['Code'])
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_from: {})".format( e.__str__(), error_code, s3_bucket_from ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = int(e.response['Error']['Code'])
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_from: {})".format( e.__str__(), error_code, s3_bucket_from ))
			self.s3_error_code = error_code
		return self.s3_response

	def s3_delete_object(self, s3_bucket_name, s3_object_name):
		self.s3_error_code = 0
		try:
			self.s3_response = self.s3cli.delete_object(Bucket=s3_bucket_name, Key=s3_object_name)
			DBG_IF_LN(self, "delete_object (s3://{}/{})".format(s3_bucket_name, s3_object_name));
		except botocore.exceptions.ClientError as e:
			error_code = int(e.response['Error']['Code'])
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {}, s3_object_name: {})".format( e.__str__(), error_code, s3_bucket_name, s3_object_name ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = int(e.response['Error']['Code'])
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {}, s3_object_name: {})".format( e.__str__(), error_code, s3_bucket_name, s3_object_name ))
			self.s3_error_code = error_code
		return self.s3_response

	def s3_get_object(self, s3_bucket_name, s3_object_name):
		self.s3_error_code = 0
		try:
			self.s3_response = self.s3cli.get_object(Bucket=s3_bucket_name, Key=s3_object_name)
			DBG_IF_LN(self, "get_object (s3://{}/{})".format(s3_bucket_name, s3_object_name));
		except botocore.exceptions.ClientError as e:
			error_code = int(e.response['Error']['Code'])
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {}, s3_object_name: {})".format( e.__str__(), error_code, s3_bucket_name, s3_object_name ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = int(e.response['Error']['Code'])
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
			error_code = int(e.response['Error']['Code'])
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, s3_bucket_name ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = int(e.response['Error']['Code'])
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, s3_bucket_name ))
			self.s3_error_code = error_code
		return self.s3_response

	def s3_put_object(self, s3_bucket_name, s3_object_name, local_name):
		self.s3_error_code = 0
		try:
			self.s3_response = self.s3cli.put_object(Body=local_name, Bucket=s3_bucket_name, Key=s3_object_name)
			DBG_IF_LN(self, "put_object (./{} -> s3://{}/{})".format(local_name, s3_bucket_name, s3_object_name));
		except botocore.exceptions.ClientError as e:
			error_code = int(e.response['Error']['Code'])
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, self.s3_bucket_name ))
			self.s3_error_code = error_code
		except ClientError as e:
			error_code = int(e.response['Error']['Code'])
			DBG_ER_LN(self, "{} (error_code:{}, s3_bucket_name: {})".format( e.__str__(), error_code, self.s3_bucket_name ))
			self.s3_error_code = error_code
		return self.s3_response

	def release(self):
		self.is_quit = 1

	def __init__(self, aws_service=AWS_SERVICE_S3, region=REGION_US_WEST_1, **kwargs):
		if ( isPYTHON(PYTHON_V3) ):
			super().__init__(**kwargs)
		else:
			super(awsX9_ctx, self).__init__(**kwargs)

		self._kwargs = kwargs
		self.region = region
		self.aws_service = aws_service
		if ( self.aws_service == "s3" ):
			self.s3src = boto3.resource("s3")
			self.s3cli = boto3.client("s3")
		DBG_IF_LN(self, "(region: {}, aws_service: {})".format( region, aws_service ))

