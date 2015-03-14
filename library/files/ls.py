#!/usr/bin/python

import os
from os import listdir
import re


def main():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True),
            filter=dict(required=False),
            result=dict(required=False, default='all', choices=['first', 'all'])
        )
    )

    path = module.params.get('path')
    path = os.path.expanduser(path)

    directory_content = [f for f in listdir(path)]
    filter = module.params.get('filter')
    if filter:
        pattern = re.compile(filter)
        directory_content = [f for f in directory_content if pattern.match(f)]

    should_modify_return_result = module.params.get('result')
    if should_modify_return_result == 'first' and len(directory_content) > 0:
        directory_content = directory_content[0]

    module.exit_json(content=directory_content)


from ansible.module_utils.basic import *

main()