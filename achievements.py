from tkinter import *
import pygame

# check the question Yuli Sezar. 61. Answer?

def run_achievement():
    main_color = "#24094e"
    heading_color = "#f8a616"
    pygame.mixer.music.load("files/click_04.wav")
    pygame.mixer.music.play(0)
    achievement_window = Toplevel()
    achievement_window.config(bg=main_color,
                              borderwidth=2,
                              relief=RAISED)
    achievement_window.overrideredirect(True)

    about_width = 450
    about_height = 550
    screen_width = achievement_window.winfo_screenwidth()  # width of the screen
    screen_height = achievement_window.winfo_screenheight()  # height of the screen

    about_center_x = (screen_width / 2) - (about_width / 2)  # find the location of app on the x coordinate
    about_center_y = (screen_height / 2) - (about_height / 2)  # find the location of app on the y coordinate
    achievement_window.geometry("{}x{}+{}+{}".format(about_width, about_height, int(about_center_x), int(about_center_y)))

    # Define image
    leaderboard_photo = PhotoImage(file="files/001.png")
    # put on the background
    photoLabel = Label(achievement_window, image=leaderboard_photo, borderwidth=0)
    photoLabel.image = leaderboard_photo
    photoLabel.place(x=0, y=0, relheight=1, relwidth=1)


    def exit_command():
        pygame.mixer.music.load("files/click_04.wav")
        pygame.mixer.music.play(0)
        achievement_window.destroy()

    exit_button_image = PhotoImage(file="files/exit_button_about.png")
    exit_button_hover_image = PhotoImage(file="files/exit_button_about_dots.png")
    exit_button = Button(achievement_window,
                         image=exit_button_image,
                         borderwidth=0,
                         activebackground=main_color,
                         background=main_color,
                         command=exit_command)
    exit_button.image = exit_button_image
    exit_button.grid(row=7, column=0, pady=10)

    def exit_button_hover(e):
        exit_button.config(image=exit_button_hover_image)

    def exit_button_leave(e):
        exit_button.config(image=exit_button_image)

    exit_button.bind("<Enter>", exit_button_hover)
    exit_button.bind("<Leave>", exit_button_leave)

    achievement_window.mainloop()