import sys
import subprocess
import tempfile
import argparse

def run_c(code):
    with tempfile.NamedTemporaryFile(suffix=".c", delete=False) as f:
        f.write(code.encode())
        f.flush()
        output = ""
        try:
            exe_file = f.name[:-2] + ".exe"
            compile_result = subprocess.run(
                ["gcc", f.name, "-o", exe_file],
                capture_output=True, text=True
            )
            if compile_result.returncode != 0:
                return compile_result.stderr
            run_result = subprocess.run([exe_file], capture_output=True, text=True)
            output = run_result.stdout + run_result.stderr
        except Exception as e:
            output = str(e)
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--code", required=True)
    args = parser.parse_args()
    result = run_c(args.code)
    print(result)
