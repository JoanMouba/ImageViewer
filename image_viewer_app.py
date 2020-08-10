import tkinter as tk
from PIL import ImageTk
from PIL import Image


class ImageViewerApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x500")
        self.grid()
        self.current_label = None
        self.current_image_number = 2
        self.button_forward = None
        self.button_backward = None
        self.images = []
        self.create_widgets()

    # CALLBACKS
    def forward(self):
        self.my_label.grid_forget()
        self.my_label = tk.Label(self, image=self.images[self.current_image_number+1])
        self.current_image_number = self.current_image_number + 1
        print("current image: ", self.current_image_number, len(self.images))
        self.my_label.grid(row=0, column=0, columnspan=3)

        self.btn_back = tk.Button(self, text="<<", command=self.backward)
        self.btn_quit = tk.Button(self, text="QUIT", command=self.master.quit)
        if (self.current_image_number == len(self.images)-1):
            self.btn_forward = tk.Button(self, text=">>", state=tk.DISABLED, command=self.forward)
        else:
            self.btn_forward = tk.Button(self, text=">>", state=tk.ACTIVE, command=self.forward)
        self.btn_back.grid(row=10, column=0)
        self.btn_quit.grid(row=10, column=1)
        self.btn_forward.grid(row=10, column=2)
        self.status_bar = tk.Label(self, relief=tk.SUNKEN, anchor=tk.E, text="Image {} of {}".format(self.current_image_number+1, len(self.images)))
        self.status_bar.grid(row=11, column=0, columnspan=3, sticky=tk.W+tk.E)
        return

    def backward(self):
        self.my_label.grid_forget()
        self.my_label = tk.Label(self, image=self.images[self.current_image_number-1])
        self.current_image_number = self.current_image_number - 1
        print("current image: ", self.current_image_number, len(self.images))
        self.my_label.grid(row=0, column=0, columnspan=3)

        self.btn_forward = tk.Button(self, text=">>", command=self.forward)
        self.btn_quit = tk.Button(self, text="QUIT", command=self.master.quit)
        if (self.current_image_number == 0):
            self.btn_back = tk.Button(self, text="<<", state=tk.DISABLED, command=self.backward)
        else:
            self.btn_back = tk.Button(self, text="<<", state=tk.ACTIVE, command=self.backward)
        self.my_label.grid(row=0, column=0, columnspan=3)
        self.btn_back.grid(row=10, column=0)
        self.btn_quit.grid(row=10, column=1)
        self.btn_forward.grid(row=10, column=2)
        self.status_bar = tk.Label(self, relief=tk.SUNKEN, anchor=tk.E, text="Image {} of {}".format(self.current_image_number+1, len(self.images)))
        self.status_bar.grid(row=11, column=0, columnspan=3, sticky=tk.W+tk.E)
        return


    def create_widgets(self):
        # Define Images
        my_image_1 =  ImageTk.PhotoImage(Image.open("images/service_cv_pro_v1.png"))
        my_image_2 =  ImageTk.PhotoImage(Image.open("images/service_cv_pro_v2.png"))
        my_image_3 =  ImageTk.PhotoImage(Image.open("images/service_cv_pro_v3.png"))
        my_image_4 =  ImageTk.PhotoImage(Image.open("images/service_cv_pro_v4.png"))
        my_image_5 =  ImageTk.PhotoImage(Image.open("images/service_cv_pro_v5.png"))
        self.images.append(my_image_1)
        self.images.append(my_image_2)
        self.images.append(my_image_3)
        self.images.append(my_image_4)
        self.images.append(my_image_5)

        # DEFINE WIDGETS
        # Labels
        self.my_label = tk.Label(self, image=self.images[self.current_image_number])
        self.my_label.image_name = self.images[self.current_image_number]
        self.my_label.grid(row=0, column=0, columnspan=3)
        # Status bar
        self.status_bar = tk.Label(self, text="Image {} of {}".format(self.current_image_number+1, len(self.images)),
                                   bd=1, relief=tk.SUNKEN, anchor=tk.E)
        # Buttons
        self.btn_back = tk.Button(self, text="<<", command=self.backward)
        self.btn_quit = tk.Button(self, text="QUIT", command=self.master.quit)
        self.btn_forward = tk.Button(self, text=">>", command=self.forward)

        # PUT WIDGETS ON THE FRAME
        self.btn_back.grid(row=10, column=0, padx=60)
        self.btn_quit.grid(row=10, column=1)
        self.btn_forward.grid(row=10, column=2, pady=10)
        self.status_bar.grid(row=11, column=0, columnspan=3, sticky=tk.W+tk.E)

root = tk.Tk()
root.title("Epignosis Image Viewer")
icon_bitmap = 'E:/FamilleMouba/CreationsEntreprise/CentreDeFormation/PythonCourse/Calculator/joeicon.png'
#root.iconbitmap(icon_bitmap)
app = ImageViewerApplication(master=root)
app.mainloop()

if __name__ == '__main__':
    print("IMAGEVIEWER GUI...")
