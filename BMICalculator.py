import tkinter as tk
from tkinter import messagebox, Canvas, ROUND

# ===== Function to Calculate BMI =====
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # convert cm to meters
        bmi = weight / (height ** 2)
        label_result.config(text=f"{bmi:.2f}")

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight 😕"
            color = "#1E90FF"
        elif 18.5 <= bmi < 24.9:
            category = "Normal 😊"
            color = "#28A745"
        elif 25 <= bmi < 29.9:
            category = "Overweight 😐"
            color = "#FFC107"
        else:
            category = "Obese 😟"
            color = "#DC3545"

        label_status.config(text=category, fg=color)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

# ====== Main Window ======
root = tk.Tk()
root.title("Smart BMI Calculator")
root.geometry("420x480")
root.config(bg="#e6f0ff")

# ====== Outer Frame ======
main_frame = tk.Frame(root, bg="white", bd=2, relief="flat")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=360, height=400)

# ====== Title Label ======
title_label = tk.Label(main_frame, text="SMART BMI CALCULATOR", 
                       font=("Poppins", 15, "bold"), fg="#0047AB", bg="white")
title_label.pack(pady=20)

# ====== Weight Input ======
lbl_weight = tk.Label(main_frame, text="Enter your weight (kg)", 
                      font=("Poppins", 12), bg="white", fg="#333")
lbl_weight.pack(pady=5)
entry_weight = tk.Entry(main_frame, font=("Poppins", 12), justify="center", 
                        width=15, bd=2, relief="groove")
entry_weight.pack(pady=5)

# ====== Height Input ======
lbl_height = tk.Label(main_frame, text="Enter your height (cm)", 
                      font=("Poppins", 12), bg="white", fg="#333")
lbl_height.pack(pady=5)
entry_height = tk.Entry(main_frame, font=("Poppins", 12), justify="center", 
                        width=15, bd=2, relief="groove")
entry_height.pack(pady=5)

# ====== Calculate Button (Rounded Effect) ======
def rounded_button(canvas, x, y, width, height, radius, color, text, command):
    canvas.create_oval(x, y, x+radius*2, y+radius*2, fill=color, outline=color)
    canvas.create_oval(x+width-radius*2, y, x+width, y+radius*2, fill=color, outline=color)
    canvas.create_rectangle(x+radius, y, x+width-radius, y+radius*2, fill=color, outline=color)
    btn = tk.Button(canvas, text=text, command=command, bg=color, fg="white",
                    font=("Poppins", 12, "bold"), relief="flat", cursor="hand2", activebackground=color)
    btn.place(x=x, y=y, width=width, height=radius*2)

canvas = Canvas(main_frame, width=300, height=60, bg="white", highlightthickness=0)
canvas.pack(pady=15)
rounded_button(canvas, 50, 10, 200, 50, 25, "#0078D7", "Calculate BMI", calculate_bmi)

# ====== Result Section ======
result_title = tk.Label(main_frame, text="Your BMI:", font=("Poppins", 12, "bold"), 
                        bg="white", fg="#333")
result_title.pack(pady=(10, 0))

label_result = tk.Label(main_frame, text="--", font=("Poppins", 24, "bold"), 
                        fg="#0047AB", bg="white")
label_result.pack(pady=5)

label_status = tk.Label(main_frame, text="", font=("Poppins", 14, "bold"), 
                        bg="white")
label_status.pack(pady=10)

# ====== Footer ======
footer = tk.Label(main_frame, text="Tip: Maintain a balanced diet and exercise regularly 💡", 
                  font=("Poppins", 9), bg="white", fg="#666")
footer.pack(side="bottom", pady=10)

# ====== Run App ======
root.mainloop()
