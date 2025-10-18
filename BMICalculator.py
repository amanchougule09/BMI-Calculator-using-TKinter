import tkinter as tk
from tkinter import messagebox

# ===== Function to Calculate BMI =====
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # cm → meters
        bmi = weight / (height ** 2)
        label_result.config(text=f"{bmi:.2f}")

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
            color = "#1E90FF"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
            color = "#28A745"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "#FFC107"
        else:
            category = "Obese"
            color = "#DC3545"

        # Update message label
        label_status.config(text=f"You are {category}", fg=color)

    except ValueError:
        label_status.config(text="")  # clear message if error
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

# ====== Main Window ======
root = tk.Tk()
root.title("Smart BMI Calculator")
root.geometry("420x480")
root.config(bg="#E6F0FF")

# ====== Outer Frame (Card) ======
main_frame = tk.Frame(root, bg="white", bd=1, relief="solid")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=360, height=420)

# ====== Title Label ======
title_label = tk.Label(main_frame, text="SMART BMI CALCULATOR",
                       font=("Poppins", 16, "bold"), fg="#0047AB", bg="white")
title_label.pack(pady=20)

# ====== Weight Input ======
lbl_weight = tk.Label(main_frame, text="Enter your weight (kg)",
                      font=("Poppins", 12), bg="white", fg="#333")
lbl_weight.pack(pady=(5,0))
entry_weight = tk.Entry(main_frame, font=("Poppins", 12), justify="center",
                        width=18, bd=0, relief="flat", highlightthickness=2,
                        highlightbackground="#0078D7", highlightcolor="#0078D7")
entry_weight.pack(pady=5, ipady=5)

# ====== Height Input ======
lbl_height = tk.Label(main_frame, text="Enter your height (cm)",
                      font=("Poppins", 12), bg="white", fg="#333")
lbl_height.pack(pady=(5,0))
entry_height = tk.Entry(main_frame, font=("Poppins", 12), justify="center",
                        width=18, bd=0, relief="flat", highlightthickness=2,
                        highlightbackground="#0078D7", highlightcolor="#0078D7")
entry_height.pack(pady=5, ipady=5)

# ====== Calculate Button ======
calculate_btn = tk.Button(main_frame, text="Calculate BMI", font=("Poppins", 12, "bold"),
                          bg="#0078D7", fg="white", activebackground="#005EA2",
                          activeforeground="white", bd=0, relief="flat",
                          cursor="hand2", command=calculate_bmi)
calculate_btn.pack(pady=20, ipadx=10, ipady=5)

# ====== Result Section ======
result_title = tk.Label(main_frame, text="Your BMI:", font=("Poppins", 12, "bold"),
                        bg="white", fg="#333")
result_title.pack(pady=(10,0))

label_result = tk.Label(main_frame, text="--", font=("Poppins", 24, "bold"),
                        fg="#0047AB", bg="white")
label_result.pack(pady=5)

# ====== BMI Status Message ======
label_status = tk.Label(main_frame, text="--", font=("Poppins", 14, "bold"),
                        bg="white", fg="#0047AB")
label_status.pack(pady=5)

# ====== Footer ======
footer = tk.Label(main_frame, text="Tip: Maintain a balanced diet and exercise regularly",
                  font=("Poppins", 9), bg="white", fg="#666")
footer.pack(side="bottom", pady=10)

# ====== Run App ======
root.mainloop()
