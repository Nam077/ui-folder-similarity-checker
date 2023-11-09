import os
from tkinter import filedialog, END

import customtkinter as ctk
from PIL import Image

current_dir = os.path.dirname(os.path.abspath(__file__))


class Result:
    def __init__(self, name, similarity, length1, length2, rate):
        self.name = name
        self.similarity = similarity
        self.length1 = length1
        self.length2 = length2
        self.rate = rate


class ResultScrollPanel(ctk.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.command = command
        self.item_list = []

    def clear_all(self):
        for item in self.item_list:
            item.destroy()
        self.item_list = []

    def add_item(self, result):
        item_frame = ctk.CTkFrame(self, border_width=1)
        item_frame.grid(row=len(self.item_list), column=0, sticky="nsew", padx=5, pady=5)

        # Subframe for image
        image_frame = ctk.CTkFrame(item_frame, border_width=0)
        image_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        image = ctk.CTkImage(Image.open(os.path.join(current_dir, "images", "documentation.png")), size=(40, 40))
        label_image_1 = ctk.CTkLabel(image_frame, text="", image=image, compound="left", padx=5, anchor="w")
        label_image_1.grid(row=0, column=0, sticky="nsew")
        label_image_2 = ctk.CTkLabel(image_frame, text="", image=image, compound="left", padx=5, anchor="w")
        label_image_2.grid(row=0, column=1, sticky="nsew")

        label_name_frame = ctk.CTkFrame(item_frame, border_width=0)
        label_name_frame.grid(row=0, column=1, padx=(0, 5), pady=5, sticky="nsew")  # Adjusted padx
        label_name = ctk.CTkLabel(label_name_frame, text=f"Name: {result.name}")
        label_name.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        label_similarity_frame = ctk.CTkFrame(item_frame, border_width=0)
        label_similarity_frame.grid(row=0, column=2, padx=(0, 5), pady=5, sticky="nsew")  # Adjusted padx
        label_similarity = ctk.CTkLabel(label_similarity_frame, text=f"Similarity: {result.similarity}")
        label_similarity.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        label_length1_frame = ctk.CTkFrame(item_frame, border_width=0)
        label_length1_frame.grid(row=0, column=3, padx=(0, 5), pady=5, sticky="nsew")  # Adjusted padx
        label_length1 = ctk.CTkLabel(label_length1_frame, text=f"Length1: {result.length1}")
        label_length1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        label_length2_frame = ctk.CTkFrame(item_frame, border_width=0)
        label_length2_frame.grid(row=0, column=4, padx=(0, 5), pady=5, sticky="nsew")  # Adjusted padx
        label_length2 = ctk.CTkLabel(label_length2_frame, text=f"Length2: {result.length2}")
        label_length2.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        label_rate_frame = ctk.CTkFrame(item_frame, border_width=0)
        label_rate_frame.grid(row=0, column=5, padx=(0, 5), pady=5, sticky="nsew")  # Adjusted padx
        label_rate = ctk.CTkLabel(label_rate_frame, text=f"Rate: {result.rate}")
        label_rate.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        for col in range(6):
            item_frame.columnconfigure(col, weight=1)

        self.item_list.append(item_frame)

    def remove_item(self, type, link, name):
        for item_frame in self.item_list:
            label = item_frame.winfo_children()[0]
            label_text = label.cget("text")
            if f"Name: {name}" == label_text:
                item_frame.destroy()
                self.item_list.remove(item_frame)
                return

    def set_items(self, items):
        self.clear_all()
        for item in items:
            self.add_item(item)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Custom Tkinter")
        self.geometry("850x700")

        # Tạo top frame
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        # Thiết lập trọng số cho hàng 1 để bottom_frame lấy hết chiều cao còn lại
        self.grid_rowconfigure(1, weight=1)

        self.bottom_frame = ctk.CTkFrame(self)

        self.bottom_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.pick_folder_1 = ctk.CTkButton(
            self.top_frame,
            text="Chose Folder 1",
            fg_color="#f0f0f0",
            text_color="#000000",
            hover_color="#e0e0e0",
            font=ctk.CTkFont(size=14, weight="bold"),
            image=ctk.CTkImage(Image.open(os.path.join(current_dir, "images", "folder.png")), size=(20, 20)),
            command=self.pick_folder_1,
            height=50
        )
        self.pick_folder_1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.pick_folder_2 = ctk.CTkButton(
            self.top_frame,
            text="Chose Folder 2",
            fg_color="#f0f0f0",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#000000",
            hover_color="#e0e0e0",
            image=ctk.CTkImage(Image.open(os.path.join(current_dir, "images", "folder.png")), size=(20, 20)),
            command=self.pick_folder_2)
        self.pick_folder_2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.compare = ctk.CTkButton(
            self.top_frame,
            text="Compare Folders",
            fg_color="#f0f0f0",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#000000",
            hover_color="#e0e0e0",
            image=ctk.CTkImage(Image.open(os.path.join(current_dir, "images", "folder.png")), size=(20, 20)),
            command=lambda: print("Chose Folder 2"))
        self.compare.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
        self.result = ctk.CTkLabel(
            self.top_frame,
            fg_color="#f0f0f0",
            height=50,
            text_color="#000000",
            corner_radius=5,
            text="No result",
            font=ctk.CTkFont(size=14, weight="bold"),
        )
        self.result.grid(row=0, column=3, sticky="nsew", padx=10, pady=10)

        self.start = ctk.CTkButton(
            self.top_frame,
            text="Start",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#69d686",
            text_color="#000000",
            hover_color="#69d686",

            image=ctk.CTkImage(Image.open(os.path.join(current_dir, "images", "play.png"))),
            command=self.start)
        self.start.grid(row=0, column=4, sticky="nsew", padx=10, pady=10)

        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.columnconfigure(1, weight=1)
        self.top_frame.columnconfigure(2, weight=1)
        self.top_frame.columnconfigure(3, weight=1)
        self.top_frame.columnconfigure(4, weight=1)

        self.bottom_frame.grid_columnconfigure(0, weight=1)

        self.scrollable_label_button_frame = ResultScrollPanel(master=self.bottom_frame, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.bottom_frame.grid_rowconfigure(0, weight=1)

        # Additional frame for displaying more results or information
        self.additional_frame = ctk.CTkFrame(self.bottom_frame, )  # Set background color if needed
        self.additional_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # have 3 columns folder 1 name, folder 2 name, similarity
        self.input_folder1 = ctk.CTkEntry(self.additional_frame, placeholder_text="Folder 1: C:/Users/Thanh/Downloads")
        self.input_folder1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.input_folder2 = ctk.CTkEntry(self.additional_frame, placeholder_text="Folder 2: C:/Users/Thanh/Downloads")
        self.input_folder2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        for col in range(2):
            self.additional_frame.columnconfigure(col, weight=1)

        #     thêm 20 dữ liệu vào scrollable_label_button_frame
        for i in range(20):
            self.scrollable_label_button_frame.add_item(Result(
                f"index{i}.ts",
                f"{i}",
                f"{i}",
                f"{i}",
                f"{i}"

            ))

    def pick_folder_1(self):
        path_1 = filedialog.askdirectory()
        self.input_folder1.delete(0, END)
        self.input_folder1.insert(0, path_1)

    def pick_folder_2(self):
        path_2 = filedialog.askdirectory()
        self.input_folder2.delete(0, END)
        self.input_folder2.insert(0, path_2)

    def start(self):
        rate = 0.9
        color = "#f0f0f0"
        if rate > 0.8:
            color = "red"
        self.result.configure(text=f"Rate: {rate}", fg_color=color)


if __name__ == '__main__':
    app = App()
    app.mainloop()
