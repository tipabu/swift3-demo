#!/usr/bin/env python
from __future__ import print_function
import io, boto3

session = boto3.Session(profile_name='swiftstack-v4')
s3 = session.resource('s3', endpoint_url='http://saio.dev')
list(s3.buckets.all())

bucket = s3.create_bucket(Bucket='test-bucket')
list(s3.buckets.all())

bucket.upload_fileobj(Key='test-object', Fileobj=io.BytesIO(b'Hello, Boston!'))
list(bucket.objects.all())

key = bucket.Object('test-object')
key.get()['Body'].read()

for bucket in s3.buckets.all():
    for key in bucket.objects.all():
        key.delete()
    bucket.delete()

list(s3.buckets.all())
