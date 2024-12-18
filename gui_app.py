# gui_app.py
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from morse_translater import text_to_morse
from grammar_parser import parse_sentence

def translate_and_display():
    sentence = sentence_entry.get()
    
    # Parse the sentence
    parse_result = parse_sentence(sentence)
    
    if parse_result["is_valid"]:
        tokens_with_pos = parse_result["tokens"]
        parse_tree = parse_result["tree"]
        print("Parse Tree:")
        parse_tree.pretty_print()  # Print the parse tree
        
        # Translate to Morse code
        morse_code = text_to_morse(sentence)
        
        # Format tokens and their parts of speech
        tokens_str = "\n".join([f"{token}: {pos}" for token, pos in tokens_with_pos.items()])
        result_text = f"Tokens and Parts of Speech:\n{tokens_str}\n\nMorse Code Translation:\n{morse_code}"
    else:
        tokens_with_pos = parse_result["tokens"]
        tokens_str = "\n".join([f"{token}: {pos}" for token, pos in tokens_with_pos.items()])
        result_text = (
            f"The sentence does not follow proper grammar.\nError: {parse_result['error']}\n\n"
            f"Tokens and Parts of Speech:\n{tokens_str}"
        )
    
    result_text_widget.config(state=tk.NORMAL)
    result_text_widget.delete("1.0", tk.END)
    result_text_widget.insert(tk.END, result_text)
    result_text_widget.config(state=tk.DISABLED)


# Set up the GUI window
root = tk.Tk()
root.title("Morse Code Translator with Grammar Check")

# Input field for sentence
sentence_label = tk.Label(root, text="Enter a sentence:")
sentence_label.pack()

sentence_entry = tk.Entry(root, width=50)
sentence_entry.pack()

# Button to trigger translation
translate_button = tk.Button(root, text="Translate", command=translate_and_display)
translate_button.pack()

# Scrollable text widget for displaying results
result_text_widget = ScrolledText(root, wrap=tk.WORD, width=60, height=20, state=tk.DISABLED)
result_text_widget.pack()

# Run the GUI event loop
root.mainloop()
