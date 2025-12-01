import sys
import builtins
import traceback
import argparse

def make_safe_builtins():
    safe_list = [
        'abs','all','any','bool','chr','divmod','enumerate','float','int',
        'len','list','map','max','min','pow','range','repr','reversed','round',
        'str','sum','zip','print'
    ]
    safe = {k: getattr(builtins, k) for k in safe_list if hasattr(builtins, k)}
    safe['print'] = print
    return safe

def run_code(code):
    globs = {"__builtins__": make_safe_builtins()}
    try:
        exec(code, globs, None)
    except Exception:
        traceback.print_exc()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--code", required=True)
    args = parser.parse_args()
    run_code(args.code)
