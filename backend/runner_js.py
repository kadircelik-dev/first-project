import sys
import subprocess
import tempfile
import argparse

def run_js(code):
    with tempfile.NamedTemporaryFile(suffix=".js", delete=False) as f:
        f.write(code.encode())
        f.flush()
        try:
            run_result = subprocess.run(
                ["node", f.name],
                capture_output=True, text=True
            )
            return run_result.stdout + run_result.stderr
        except Exception as e:
            return str(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--code", required=True)
    args = parser.parse_args()
    result = run_js(args.code)
    print(result)
