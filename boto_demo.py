#!/usr/bin/env python
from __future__ import print_function
import boto, requests

s3 = boto.connect_s3(profile_name='swiftstack', host='saio.dev')
s3.auth_region_name = 'US'

s3.get_all_buckets()
bucket = s3.create_bucket('test-bucket')
bucket
s3.get_all_buckets()
key = bucket.new_key('test-object')
key
key.set_contents_from_string('Hello, Boston!')
bucket.get_all_keys()
requests.get(s3.generate_url(3600, 'GET', 'test-bucket', 'test-object')).content

for bucket in s3.get_all_buckets():
    for key in bucket.get_all_keys():
        key.delete()
    bucket.delete()

s3.get_all_buckets()
