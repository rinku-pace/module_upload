# -*- coding: utf-8 -*-

"""Main module."""
__author__ = "Rinku Kumar"
__status__ = "Development"

import logging
import os

import boto3
import botocore

s3client = boto3.client(
    "s3",
    aws_access_key_id=os.environ["S3_AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["S3_AWS_SECRET_ACCESS_KEY"],
    region_name=os.environ["S3_AWS_REGION"],
)
bucket_name = os.environ["S3_AWS_BUCKET"]


def upload_file_to_s3(file_obj, folder_name=None):

    try:

        if folder_name:
            path = folder_name + "/" + file_obj.filename
        else:
            path = file_obj.filename
        acl = "public-read"
        s3client.upload_fileobj(
            file_obj,
            bucket_name,
            path,
            ExtraArgs={"ACL": acl, "ContentType": file_obj.content_type},
        )
        url = "https://{0}.s3.amazonaws.com/{1}".format(bucket_name, path)
        return url

    except botocore.exceptions.ClientError as e:

        # This is a catch all exception.
        logging.error(str(e))
        return ""
