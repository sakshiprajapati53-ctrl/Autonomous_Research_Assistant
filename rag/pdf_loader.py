import pdfplumber  # research papers ke liye optimized extraction 

def extract_text_from_pdf(
        file_path: str
):
    # store complex text
    text = ""

    # open the pdf
    with pdfplumber.open(file_path) as pdf:  # Why with? Automatic cleanup.Without it memory leak risk
       
        # loop through pages
        for page in pdf.pages: # each page process
           
            # extract page text
            page_text = page.extract_text()
           
            #avoid none error
            if page_text:  # when ever extraction fails then return none
                text += page_text + "\n"  # improve new line readability

    return text