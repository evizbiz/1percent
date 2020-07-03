#!/usr/bin/env python

def rt53stat():
  import boto.route53
  conn = boto.route53.connect_to_region('us-west-2')

def s3stat():
  import boto3
  s3 = boto3.resource('s3')
  #s3.ServiceResource()
  for bucket in s3.buckets.all(): print(bucket.name)

def ec2stat():
  ec2 = boto3.resource('ec2')

def aws_lambda(region='us-east-1', marker=''):
  import boto3
  client = boto3.client('lambda', region_name=region)
  resp = client.list_functions()
  return resp

if __name__ == '__main__':
  resp = aws_lambda()
  print(resp)

