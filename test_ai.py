import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

print("line 9")
# Configure the API key
genai.configure(api_key=os.getenv("API_KEY"))

def test_gemini_call():
    print("beginning of test_gemini_call")
    start = time.time()
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content("Hello, Gemini!")
        print("Gemini Response:", response.text)
        assert response.text is not None and len(response.text) > 0
    except Exception as e:
        print(f"Error calling Gemini: {e}")
        raise
    print("executed in: ", time.time() - start)

if __name__ == "__main__":
    print("Running Gemini API demo...")
    test_gemini_call()
    print("Gemini API demo completed.")