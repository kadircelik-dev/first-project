import sys
import io

def execute_code(code_input):
    """
    Executes Python code safely and returns the output or error.
    """

    # Capture print() outputs
    output_buffer = io.StringIO()
    sys.stdout = output_buffer

    try:
        exec(code_input)
        result = output_buffer.getvalue()
    except Exception as e:
        result = f"Error: {str(e)}"

    # Restore normal stdout
    sys.stdout = sys.__stdout__

    return result if result.strip() else "(no output)"
