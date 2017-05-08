#!/usr/bin/env python
from __future__ import print_function
import io, boto3

session = boto3.Session(profile_name='swiftstack')
s3 = session.resource('s3', endpoint_url='http://saio.dev')

print(list(s3.buckets.all()))

bucket = s3.create_bucket(Bucket='test-bucket')
print(list(s3.buckets.all()))

bucket.upload_fileobj(Key='test-object', Fileobj=io.BytesIO(b'Hello, world!'))
print(list(bucket.objects.all()))

key = bucket.Object('test-object')
print(key.get()['Body'].read())

key.delete()
print(list(bucket.objects.all()))

bucket.delete()
print(list(s3.buckets.all()))
