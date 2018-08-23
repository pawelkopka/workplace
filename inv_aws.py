#!/usr/bin/env python
import json
import boto3


def main():
    ec2 = boto3.resource('ec2')

    filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]

    instances = ec2.instances.filter(Filters=filters)

    hosts = []

    for instance in instances:
        hosts.append(instance.public_ip_address)

    inventory = {'aws': {
        'hosts': hosts,
        'vars': {
            'ansible_ssh_private_key_file': 'pycon-key.pem',
            'ansible_user': 'ubuntu'
        }
    }}
    print json.dumps(inventory)


if __name__ == "__main__":
    main()