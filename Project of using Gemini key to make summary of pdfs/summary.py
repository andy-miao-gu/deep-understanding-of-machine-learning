import google.generativeai as genai
import os
from pdffiletotextfile import pdf_to_text
from dotenv import load_dotenv
load_dotenv()

def get_gemini_response(prompt_text):
    """
    Sends a text prompt to the Gemini model and returns the response.

    Args:
        prompt_text (str): The prompt to send to the model.

    Returns:
        str: The text response from the Gemini model.
    """
    # Configure the client with your API key
    # It's best practice to set GEMINI_API_KEY as an environment variable
    # e.g., export GEMINI_API_KEY="YOUR_API_KEY" in your terminal
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY environment variable not set."
        
    genai.configure(api_key=api_key)

    # Initialize the model
    # You can choose a different model, like "gemini-2.5-pro" or "gemini-2.5-flash"
    model = genai.GenerativeModel('gemini-2.5-flash')

    # Generate content
    response = model.generate_content(prompt_text)

    return response.text

# Example usage:
if __name__ == "__main__":
    # Example usage:
    data=os.listdir("forAndy")
    print(data)
    #
    for each in range(0, 10):
        pdf_file = f"/Users/andymiaogu/Desktop/folder/deep understanding of machine learning/Project of using Gemini key to make summary of pdfs/forAndy/{data[each]}"  # Replace with your PDF file name
        
        text = pdf_to_text(pdf_file)
            
        user_prompt = f"summarize this paper in 1 lines but make this summary less or equals to 15 words{text}"
        response_text = get_gemini_response(user_prompt)
        print(response_text)
        with open("summary.txt","a") as f:
            f.write(f"{response_text} \n")