from m3chat_sdk.client import M3ChatClient
from m3chat_sdk.types import RequestParams

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def test_get_response():
    client = M3ChatClient({"stream": False})
    params: RequestParams = {
        "model": "mistral",
        "content": "Hello, how are you?"
    }

    try:
        response = client.get_response(params)
        assert response is not None and len(response) > 0
        print(f"{GREEN}Test 1 passed{RESET}")
    except Exception as e:
        print(f"{RED}Test 1 failed: {e}{RESET}")

def test_invalid_model():
    client = M3ChatClient()
    params: RequestParams = {
        "model": "invalid-model",
        "content": "Hello"
    }

    try:
        client.get_response(params)
        print(f"{RED}Test 2 failed: did not raise error for invalid model{RESET}")
    except ValueError:
        print(f"{GREEN}Test 2 passed{RESET}")
    except Exception as e:
        print(f"{RED}Test 2 failed with unexpected error: {e}{RESET}")

if __name__ == "__main__":
    test_get_response()
    test_invalid_model()
