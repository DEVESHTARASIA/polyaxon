import argparse

from polyaxon_client.tracking import Job

from .dockerizer.init import cmd as init_cmd
from .dockerizer.build import cmd as build_cmd

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--cmd',
        type=str
    )
    args = parser.parse_args()
    arguments = args.__dict__

    cmd = arguments.pop('cmd')

    job = Job()
    if cmd == 'init':
        init_cmd(job=job)
    elif cmd == 'build':
        build_cmd(job=job)
