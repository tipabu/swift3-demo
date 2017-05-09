#!/bin/sh

set -e

run() {
    set -x
    export AWS_DEFAULT_PROFILE="${1:-swiftstack}"

    aws s3 ls

    aws s3 mb s3://test-bucket
    aws s3 ls

    echo "$2" | aws s3 cp - s3://test-bucket/test-object
    aws s3 ls s3://test-bucket

    aws s3 cp s3://test-bucket/test-object -

    aws s3 rm s3://test-bucket/test-object
    aws s3 rb s3://test-bucket
    { set +x; } 2> /dev/null
}

run swiftstack 'Hello, Boston!'
if [ "$1" == "--no-wait" ]; then
    echo
else
    read REPLY
fi
run swiftstack-v4 'Also supports v4 signatures'
if [ "$1" == "--no-wait" ]; then
    echo
else
    read REPLY
fi
run swiftstack-query 'And pre-signed URLs'
