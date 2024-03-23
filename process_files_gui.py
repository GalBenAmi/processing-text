import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import string
import os
#import PyPDF2
#def pdf_to_text(input_pdf, output_txt):
#    with open(input_pdf, 'rb') as file:
#        pdf_reader = PyPDF2.PdfFileReader(file)
#        text = ""
#        for page_num in range(pdf_reader.numPages):
#            text += pdf_reader.getPage(page_num).extractText()

#    with open(output_txt, 'w', encoding='utf-8') as output_file:
#        output_file.write(text)

    
    
def select_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text files", "*.txt")])

   
def defult_filename():
    name=file_name+"_Filterd by-"
    suffix={0:"Reversed",1:"HebrewChar",2:"EnglishChar",3:"Common",4:"Custom"}
    arr=[reverse_var.get(),hebrew_var.get(),english_var.get(),common_var.get(),custom_entry.get()]
    for t in [i for i, x in enumerate(arr) if x]:
        if(t==0):
            name=file_name+"_"+suffix[t]+"_Filterd by-"
            continue
        name+=f" {suffix[t]}"
    return name
def process_file_path():
    global file_name, file_type
    reverse_path=file_path[::-1]
    dot= reverse_path.index(".")
    bSlash= reverse_path.index("/")
    file_name = reverse_path[dot+1:bSlash]
    file_name=file_name[::-1]
    file_type=reverse_path[:dot]
    file_type= file_type[::-1]
    file_name= defult_filename()

def select_output_location():
    try:file_path
    except NameError:
        show_error_message("Plese select file first!")
    process_file_path()      
    global save_path 
    save_path= filedialog.asksaveasfilename(initialfile = file_name ,defaultextension=".txt", filetypes=[("Text files", "*.txt")])  

def start_processing():

    if file_path:
        if save_path:
            if english_var.get() or hebrew_var.get() or common_var.get() or reverse_var.get() or custom_entry.get():
                process_and_save(file_path, save_path)
                show_done_message()
            else:
                show_error_message("haven't chose what to process!")
        else:
            show_error_message("output locatian is missing!")
    else:
        show_error_message("input file is missing!")
            

def process_and_save(input_path, output_path):
    allowed_characters = set()
    heb=set("ךםןףץאבגדהוזחטיכלמנסעפצקרשת")
    if english_var.get():
        allowed_characters.update(set(string.ascii_letters))

    if hebrew_var.get():
        allowed_characters.update(heb)

    custom_chars = custom_entry.get()
    allowed_characters.update(set(custom_chars))
    def filter_chars(word):
        return ''.join(char for char in word if char in allowed_characters)
    def containts_heb(word):
        return any(i in word for i in heb)
    # Open the file in read mode with the specified encoding
    with open(input_path, 'r', encoding='utf-8') as file:
        # Read lines from the file and store them in an array
        lines = file.readlines()
    
    # Initialize an empty array to store processed lines
    processed_lines = []
    
    # Iterate through each line
    for line in lines:
        if (reverse_var.get()):
            # Split the line into an array of words and reverse the order of words
            words = line.split()[::-1]
        else:
            # Split the line into an array of words
            words = line.split()
        if (reverse_var.get()):
            # Reverse the order of characters in each word and filter based on allowed characters
             processed_words = [(filter_chars(word[::-1])if containts_heb(word) else filter_chars(word)) for word in words ]
        else:
            #  filter each word based on allowed characters
            processed_words = [filter_chars(word) for word in words]
        
        for word in processed_words:
            if len(word)==0:
                processed_words.remove(word)
                
        

        # Join the  processed words back into a line and append to the main array
        if len(processed_words)==1:
            if processed_words=="":
                continue
        processed_lines.append(' '.join(processed_words)+'\n')
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(processed_lines)
def show_error_message(ms):
    messagebox.showinfo("ERORR", f"{ms}")
def show_done_message():
    if(messagebox.askyesno("Done", "Processing is complete!\nDo you want to open the file?")):
        os.startfile(save_path)

# Create the main window
window = tk.Tk()
window.title("Text Filter GUI")
# Create a select file button
select_file_button = tk.Button(window, text="select file", command=select_file)
select_file_button.pack(pady=20)

# Create checkboxes for English alphabets
english_var = tk.BooleanVar()
english_checkbox = tk.Checkbutton(window, text="English Alphabet", variable=english_var)
english_checkbox.pack()

# Create checkboxes for Hebrew alphabet
hebrew_var = tk.BooleanVar()
hebrew_checkbox = tk.Checkbutton(window, text="Hebrew Alphabet", variable=hebrew_var)
hebrew_checkbox.pack()

# Create checkboxes for Common charachters
common_var = tk.BooleanVar()
common_checkbox = tk.Checkbutton(window, text="Common Charachters  , : - . \" ", variable=common_var)
common_checkbox.pack()

# Create checkboxes for reverse hebrew words
reverse_var = tk.BooleanVar()
reverse_checkbox = tk.Checkbutton(window, text="reverse hebrew words", variable=reverse_var)
reverse_checkbox.pack()

# Create an entry for custom allowed characters
custom_label = tk.Label(window, text="Custom Allowed Characters:")
custom_label.pack()

custom_entry = tk.Entry(window)
custom_entry.pack()

# creae select  output location button
select_output_location_button = tk.Button(window, text="select output location", command=select_output_location)
select_output_location_button.pack(pady=20)

# Create a button to start processing
start_button = tk.Button(window, text="Start Processing", command=start_processing)
start_button.pack(pady=20)

# Run the main loop
window.mainloop()
