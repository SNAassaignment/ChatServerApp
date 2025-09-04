import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x400")
app.title("Scrollable Frame Example")

# Create a scrollable frame
scroll_frame = ctk.CTkScrollableFrame(app)
scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Add items inside the scrollable frame
for i in range(30):
    ctk.CTkLabel(scroll_frame, text=f"Item {i+1}").pack(pady=5, padx=10)

app.mainloop()
