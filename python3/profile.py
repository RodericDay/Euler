'''
The purpose of this module is to simplify my life a little bit. To disable,
just ensure that you're not using the Euler (Python) build-system.

Two annoyances when working on PE problems were alternating between `kernprof`
and the Python interpreter when using `@profile` decorators, as well as the
occasional runaway function that goes on forever (it doesn't hijack the sublime
build process, so you need to `kill` it manually). Being able to verify correct
answers was a nice bonus.

This script attempts to seamlessly handle all annoying scenarios to allow one
to concentrate on solving problems.
'''

import os, argparse, re
import subprocess


class ProfilerDecoratorError(SyntaxError):
    def __str__(self):
        return "Found @profile decorator. Stopping execution!"

def check_output(cmd, timeout=1):
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=timeout)
        return output.decode().strip()
    except subprocess.TimeoutExpired:
        return "Timeout!"
    except subprocess.CalledProcessError as error:
        message = error.output.decode().strip()

    # we return outside of try/catch loop to avoid nested traceback
    if "NameError: name 'profile' is not defined" in message:
        raise ProfilerDecoratorError
    else:
        raise RuntimeError(message)


parser = argparse.ArgumentParser(description='Handle running problem scripts')
parser.add_argument('filename', type=str)
args = parser.parse_args()

# Collect all solutions as dict.
# Tip: Call by query (`.get(n)`) rather than index (`[n]`)
#      in case known solution is not available.
with open('../solutions.txt') as fp:
    solutions = {i : string.strip() for i, string in enumerate(fp) if string}

# What happens if we run *this* file?
# Run all the files with a very short fuse, see how far we get!
# Verify along the way.
if os.path.basename(args.filename) == __file__:

    for path in [path for path in os.listdir() if path.startswith('problem')]:
        try:
            idx = int(re.findall(r'problem(\d{5})', path)[0])
            ans = check_output(["python3", path], 0.1)
            sol = solutions.get(idx-1, 'none')
            print("{:>4}".format(idx), '✓' if ans==sol else '✗', ans)
        except RuntimeError as error:
            print(error)
            exit(1)
    exit()

# The alternative is that we are working on a specific file.
# In this case, all this script does is handle switching between regular python
# execution and profiled execution.
try:
    ans = check_output(["python3", args.filename], timeout=5)
    print(ans)
    exit()
except ProfilerDecoratorError:
    pass
except RuntimeError as error:
    print(error)
    exit(1)

# Try a fallback pass, with the profiler. It will swallow errors!
try:
    ans = check_output(["kernprof", "-lvo", "/dev/null", args.filename])
    print(ans)
except RuntimeError:
    print("Ensure file runs properly before adding profiler.")
    exit(1)
