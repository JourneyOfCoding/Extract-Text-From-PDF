# Import the pdfplumber library using this command --> pip install pdfplumber

import pdfplumber

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Initialize an empty string to store all extracted text
        all_text = ""
        
        # Extracting each page of the PDF
        for page in pdf.pages:
            # Extract text from the current page
            page_text = page.extract_text()
            
            # Concatenate the extracted text with the existing text, separated by a newline character
            all_text += page_text + "\n"
            
        # Return the concatenated text
        return all_text
    
# Path to the PDF file
pdf_path = "dummy.pdf"

# Call the function to extract text from the PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Check if text extraction was successful
if extracted_text:
    # Print the extracted text
    print(extracted_text)
else:
    print("Text extraction failed.")
