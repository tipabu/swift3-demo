#!/usr/bin/env python
from __future__ import print_function
import boto, requests

s3 = boto.connect_s3(profile_name='swiftstack', host='saio.dev')
s3.auth_region_name = 'US'

buckets = s3.get_all_buckets()
print(buckets)

bucket = s3.create_bucket('test-bucket')
print(s3.get_all_buckets())

key = bucket.new_key('object')
key.set_contents_from_string('Hello, world!')
print(bucket.get_all_keys())

print(requests.get(s3.generate_url(3600, 'GET', 'test-bucket', 'object')).content)

for key in bucket.get_all_keys():
    key.delete()

bucket.delete()
print(s3.get_all_buckets())
