import tkinter as tk

# Function to evaluate the expression entered
def evaluate_expression():
    try:
        result = eval(entry.get())
        label_result.config(text=f"Result: {result}")
    except:
        label_result.config(text="Error!")

# Main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x200")

# Entry widget to take input
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Button to evaluate the expression
button = tk.Button(root, text="Calculate", command=evaluate_expression)
button.pack(pady=5)

# Label to display the result
label_result = tk.Label(root, text="Result: ", font=('Arial', 14))
label_result.pack(pady=10)

# Start the event loop
root.mainloop()
