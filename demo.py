#!/usr/bin/env python
from __future__ import print_function
import argparse
import code
import sys
import traceback

parser = argparse.ArgumentParser()
parser.add_argument('python_file')
parser.add_argument('--no-wait', action='store_false', dest='wait')
args = parser.parse_args()

buffer = []
interrupted = False
with open(args.python_file, 'rt') as fp:
    for line in fp:
        if line.startswith('#!'):
            continue  # ignore shebang
        line = line.strip('\n')
        print('%s %s' % ('\n...' if buffer else '>>>', line), end='')
        buffer.append(line)
        try:
            compiled = code.compile_command('\n'.join(buffer))
            if compiled is None:
                continue
            if args.wait:
                try:
                    input()
                except KeyboardInterrupt:
                    interrupted = True
                    break
                except:
                    pass
            else:
                print()  # Need a newline
            result = eval(compiled)
            if result is not None:
                print(result, end='')
            buffer = []
        except:
            e, v, tb = sys.exc_info()
            traceback.print_exception(e, v, tb.tb_next)
            buffer = []

if args.wait and not interrupted:
    print('>>> quit', end='')
    try:
        input()
    except:
        pass
