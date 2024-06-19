import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ImageToPDFConverter(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Conversor de Imagens para PDF")
        self.geometry("500x300")  

        self.image_files = []
        self.pdf_path = ""

       
        self.selected_file_label = ctk.CTkLabel(self, text="Nenhum arquivo selecionado")
        self.selected_file_label.pack(pady=10)

        
        self.select_images_button = ctk.CTkButton(self, text="Selecionar Imagens", command=self.select_images)
        self.select_images_button.pack(pady=10)

        
        self.convert_button = ctk.CTkButton(self, text="Converter", command=self.convert, state="disabled")
        self.convert_button.pack(pady=10)

        
        self.save_button = ctk.CTkButton(self, text="Salvar PDF", command=self.save_pdf, state="disabled")
        self.save_button.pack(pady=10)

    def select_images(self):
        self.image_files = filedialog.askopenfilenames(
            title="Selecione as imagens",
            filetypes=[("Arquivos de Imagens", "*.jpg;*.jpeg;*.png"), ("Todos os Tipos", "*.*")]
        )
        if self.image_files:
            
            self.selected_file_label.configure(text=self.image_files[0] if len(self.image_files) == 1 else "Múltiplos arquivos selecionados")
            self.convert_button.configure(state="normal")  

    def convert(self):
        try:
            images = [Image.open(img) for img in self.image_files]
            images[0].save("temp.pdf", "PDF", resolution=100.0, save_all=True, append_images=images[1:])
            messagebox.showinfo("Concluído", "Imagens convertidas em PDF com sucesso!")
            self.save_button.configure(state="normal")  
        except Exception as e:
            messagebox.showerror("Erro", f"Falha na conversão: {e}")

    def save_pdf(self):
        self.pdf_path = filedialog.asksaveasfilename(
            title="Salvar PDF em",
            defaultextension=".pdf",
            filetypes=[("Arquivos PDF", "*.pdf")]
        )
        if self.pdf_path:
            os.rename("temp.pdf", self.pdf_path)
            messagebox.showinfo("Concluído", f"PDF salvo em: {self.pdf_path}")
            
            self.save_button.configure(state="disabled")
            self.convert_button.configure(state="disabled")

if __name__ == "__main__":
    app = ImageToPDFConverter()
    app.mainloop()
