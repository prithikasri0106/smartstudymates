import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from pdf_reader import extract_text_from_pdf
from summarizer import summarize_text
import os

def upload_and_summarize():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Text files", "*.txt")])
    if not file_path:
        return

    if file_path.endswith(".pdf"):
        raw_text = extract_text_from_pdf(file_path)
    else:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_text = f.read()

    if not raw_text.strip():
        messagebox.showwarning("Empty File", "No content found to summarize.")
        return

    summary = summarize_text(raw_text)

    summary_box.delete(1.0, tk.END)
    summary_box.insert(tk.END, summary)

    # Save summary
    base_name = os.path.basename(file_path).split('.')[0]
    with open(f"data/summaries/{base_name}_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
    messagebox.showinfo("Saved", "Summary saved to data/summaries/")

# GUI
app = tk.Tk()
app.title("Smart StudyMate")
app.geometry("800x500")

label = tk.Label(app, text="Smart StudyMate - Summarize Your Notes", font=("Helvetica", 16))
label.pack(pady=10)

upload_btn = tk.Button(app, text="Upload & Summarize Notes", command=upload_and_summarize, bg="#381164", fg="white", padx=10, pady=5)
upload_btn.pack(pady=10)

summary_box = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=90, height=20)
summary_box.pack(padx=10, pady=10)

app.mainloop()
