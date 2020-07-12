#!/usr/bin/env python
import json

def prices(svc='AmazonEC2'):
  import awspricing
  awsproce = awspricing.offer(svc)
  return awsprice

def rt53stat():
  import boto.route53
  conn = boto.route53.connect_to_region('us-west-2')
  domains = conn.get_zones()
  return domains

def s3stat():
  import boto3
  s3 = boto3.resource('s3')
  #s3.ServiceResource()
  all = []
  for bucket in s3.buckets.all(): all.append(bucket.name)
  return all

def ec2stat():
  import boto3
  ec2 = boto3.resource('ec2')
  return ec2

def aws_lambda(region='us-east-1', marker=''):
  import boto3
  client = boto3.client('lambda', region_name=region)
  resp = client.list_functions()
  return resp

if __name__ == '__main__':
  print("lambdas ....")
  resp = aws_lambda()
  print(resp, '\n')

  print("S3 buckets ....")
  buckets = s3stat()
  print(buckets, '\n')

  print("EC2 VMs ....")
  ec2 = ec2stat()
  print(ec2, '\n')

  print("Route53 domains ....")
  rt53 = rt53stat()
  print(rt53,'\n')

  #prcs = prices()
  #help(prcs)


