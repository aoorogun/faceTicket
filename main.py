import tkinter as tk
import util
import cv2
from PIL import Image, ImageTk
class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")

        self.login_button_main_window = util.get_button(self.main_window, 'login', 'green', self.login, fg="black")
        self.login_button_main_window.place(x=750, y=300)

        self.register_new_user_button_main_window = util.get_button(self.main_window, 'register new user', 'grey', 
                                                                    self.register_new_user, fg = 'black')
        self.register_new_user_button_main_window.place(x=750, y=400)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        self.most_recent_capture_arr = frame

        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)

        imgtk = ImageTk.PhotoImage(image = self.most_recent_capture_pil)

        self._label.imgtk = imgtk
        self._label.configure(image = imgtk)

        self._label.after(20, self.process_webcam)



    def login(self):
        pass
    
    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1200x520+370+120")

        self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Accept', 'green', self.accept_register_new_user_window, fg="black")
        self.accept_button_register_new_user_window.place(x=750, y=300)

        
        self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Try Again', 'black', self.try_again_register_new_user_window, fg="red")
        self.try_again_button_register_new_user_window.place(x=750, y=400)

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)
        
        self.add_img_to_label(self.capture_label)

        self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=150)

        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window,'Please input username:')
        self.text_label_register_new_user.place(x=750, y=70)

    def try_again_register_new_user_window(self):
        self.register_new_user.destroy()

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image = self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image = imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()

        self._label.after(20, self.process_webcam)

    def start(self):
        self.main_window.mainloop()

    def accept_register_new_user_window(self):
        pass

    
    def try_again_register_new_user_window(self):
        pass

if __name__ == "__main__":
    app = App()
    app.start()