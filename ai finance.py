import tkinter as tk
from tkinter import ttk, messagebox

# Mock finance advice function
def get_finance_advice(user_type, question):
    question = question.lower()

    if user_type == "Student":
        tone = "use a friendly and simple tone"
    else:
        tone = "use a professional and detailed tone"

    if "save" in question:
        return f"As a {user_type.lower()}, to {tone}, try setting aside at least 20% of your monthly income into a savings account."
    elif "tax" in question:
        return f"Regarding taxes, {tone}, make sure to keep track of your deductible expenses and file your returns on time."
    elif "invest" in question:
        return f"For investments, {tone}, consider low-risk options like index funds if you're starting out."
    else:
        return "I'm here to help with savings, taxes, and investments. Could you please specify your question?"

# Callback when the button is pressed
def on_submit():
    user_type = user_type_var.get()
    question = question_entry.get()

    if not user_type or not question.strip():
        messagebox.showwarning("Input Error", "Please select a user type and enter a question.")
        return

    response = get_finance_advice(user_type, question)
    response_text.set(response)

# GUI Setup
root = tk.Tk()
root.title("Personal Finance Chatbot")
root.geometry("500x400")
root.resizable(False, False)

# Labels
tk.Label(root, text="Personal Finance Chatbot", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, text="Select User Type:").pack(pady=(10, 2))

# User type selection
user_type_var = tk.StringVar()
user_type_menu = ttk.Combobox(root, textvariable=user_type_var, state="readonly")
user_type_menu["values"] = ("Student", "Professional")
user_type_menu.pack()

# Question input
tk.Label(root, text="Your Question:").pack(pady=(20, 2))
question_entry = tk.Entry(root, width=60)
question_entry.pack()

# Submit button
submit_btn = tk.Button(root, text="Get Advice", command=on_submit)
submit_btn.pack(pady=15)

# Response output
tk.Label(root, text="Chatbot Response:").pack(pady=(20, 2))
response_text = tk.StringVar()
response_label = tk.Label(root, textvariable=response_text, wraplength=450, justify="left")
response_label.pack(padx=10)

# Start the app
root.mainloop()
