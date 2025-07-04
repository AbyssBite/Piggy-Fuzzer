import time


def monitor(func, *args, **kwargs) -> dict:
    """
    Measures response duration and detects anomalies.

    Returns:
        dict: {
            'duration': float (in seconds),
            'response': any output or error,
            'timeout': bool,
            'crash': bool
        }
    """
    start = time.time()
    result = None
    timeout = False
    crash = False

    try:
        result = func(*args, **kwargs)
        if isinstance(result, bytes) and len(result.strip()) == 0:
            timeout = True
    except Exception as e:
        crash = True
        result = {"error": str(e)}

    duration = round(time.time() - start, 5)

    return {
        "duration": duration,
        "response": result,
        "timeout": timeout,
        "crash": crash,
    }
