import pdfplumber
import os
def pdf_to_text(pdf_path):
    """
    Extracts text from a PDF file and saves it to a text file.

    Args:
        pdf_path (str): The path to the input PDF file.
        (str): The path to the output text file.
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    full_text += page_text + "\n"  # Add a newline for page separation
        
        # with open(, "w", encoding="utf-8") as f:
        #     f.write(full_text)
        print(f"Successfully extracted text from '{pdf_path}' and saved to .")
    except Exception as e:
        print(f"An error occurred: {e}")
    return full_text
if __name__=="__main__":  
    # Example usage:
    data=os.listdir("forAndy")
    print(data)
    #
    for each in range(1, 10):
        pdf_file = f"/Users/andymiaogu/Desktop/folder/deep understanding of machine learning/forAndy{data[each]}"  # Replace with your PDF file name
        output_text_file = f"Paper{each+1}.txt" # Desired output text file name
        pdf_to_text(pdf_file)