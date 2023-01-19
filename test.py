import subprocess


test_cases = {
    "1 2": "3",
    "4 2": "6",
    "-1 5": "4",
    "-1 -5": "-6",
    "0 0": "0",
    " 0 0 ": "0",
}

for input, expected_error in test_cases.items():
    process = subprocess.Popen(['python', 'main.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True,
                               bufsize=0
   )
    process.stdin.write(input)
    stdout, stderr = process.communicate()
    if ( expected_error == stdout.strip()):
        passed = "Yes"
    else:
        passed = "NO"
    print(f'input: {input.strip()}, expected: {expected_error}, actual: {stdout.strip()}, passed: {passed}, errr: {stderr}')

print("\n\nTest error cases\n\n")

test_error_cases = {
    "": "EOFError: EOF when reading a line",
}

for input, expected_error in test_error_cases.items():
    process = subprocess.Popen(['python', 'main.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True,
                               bufsize=0
                               )
    process.stdin.write(input)
    stdout, stderr = process.communicate()
    if expected_error in stderr.strip():
        passed = "Yes"
    else:
        passed = "NO"
    print(f'input: {input.strip()}, passed: {passed}, expected: {expected_error},  error: {stderr.strip()}')

