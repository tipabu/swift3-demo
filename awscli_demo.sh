#!/bin/sh

set -e

run() {
    set -x
    export AWS_DEFAULT_PROFILE="${1:-swiftstack}"

    aws s3 ls

    aws s3 mb s3://test-bucket
    aws s3 ls

    echo 'Hello, world!' | aws s3 cp - s3://test-bucket/test-object
    aws s3 ls s3://test-bucket

    aws s3 cp s3://test-bucket/test-object -

    aws s3 rm s3://test-bucket/test-object
    aws s3 rb s3://test-bucket
    { set +x; } 2> /dev/null
}

run swiftstack
echo
run swiftstack-v4
echo
run swiftstack-query
