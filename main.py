from tkinter import *
import webbrowser
import pygame
import about
import achievements

pygame.mixer.init()

def start_game():
    import game
    game.run_game()


def login():
    button_frame_color = "#24094e"
    window = Tk()
    window.overrideredirect()
    app_width = 1009
    app_height = 680
    screen_width = window.winfo_screenwidth() # width of the screen
    screen_height = window.winfo_screenheight() # height of the screen

    center_x = (screen_width / 2) - (app_width / 2)  # find the location of app on the x coordinate
    #center_y = (screen_height / 2) - (app_height / 2)  # find the location of app on the y coordinate

    window.geometry("{}x{}+{}+{}".format(app_width, app_height, int(center_x), 3))
    #window.maxsize(1280, 720)
    #window.minsize(900, 500)

    # Define image
    bgPhoto = PhotoImage(file="files/Foto1.png")
    # put on the background
    photoLabel = Label(window, image=bgPhoto, borderwidth=0)
    photoLabel.place(x=0, y=0, relheight=1, relwidth=1)

    buttonFrame = Frame(photoLabel, bg=button_frame_color, borderwidth=0)
    buttonFrame.place(relx=0.5, rely=0.48, anchor=CENTER)

    start_button_image = PhotoImage(file="files/button1 (3).png")
    start_hover_image = PhotoImage(file="files/hover_button.png")
    about_hover_image = PhotoImage(file="files/hover_button2.png")
    like_hover_image = PhotoImage(file="files/hover_button3.png")
    achievement_hover_image = PhotoImage(file="files/hover_button4.png")

    # <<<<<< START BUTTON >>>>>>
    def startCommand():
        pygame.mixer.music.load("files/click_04.wav")
        pygame.mixer.music.play(0)

        window.destroy()
        start_game()

    startButton = Button(buttonFrame,
                         command=startCommand,
                         image=start_button_image,
                         borderwidth=0,
                         bg=button_frame_color,
                         activebackground=button_frame_color

                         #bg="#699CF1",
                         #fg="black",
                         #text="Başla",
                         #width=14,
                         #height=2,
                         #font=("arial", 15, "bold")
                         )
    startButton.grid(row=0, column=0)

    def start_button_hover(e):

        startButton.config(image=start_hover_image)

    def start_button_leave(e):
        startButton.config(image=start_button_image)

    startButton.bind("<Enter>", start_button_hover)
    startButton.bind("<Leave>", start_button_leave)

    about_button_image = PhotoImage(file="files/button1 (4).png")

    # <<<<<< ABOUT BUTTON >>>>>>
    aboutButton = Button(buttonFrame,
                         #text="Oyun Haqqında",
                         command=about.aboutCommand,
                         image=about_button_image,
                         borderwidth=0,
                         bg=button_frame_color,
                         activebackground=button_frame_color)
    aboutButton.grid(row=1, column=0)

    def about_button_hover(e):
        aboutButton.config(image=about_hover_image)

    def about_button_leave(e):
        aboutButton.config(image=about_button_image)

    aboutButton.bind("<Enter>", about_button_hover)
    aboutButton.bind("<Leave>", about_button_leave)


    # <<<<<<< LIKE US ON MS STORE >>>>>>>

    like_button_image = PhotoImage(file="files/button1 (5).png")
    def likeButton():
        pygame.mixer.music.load("files/click_04.wav")
        pygame.mixer.music.play(0)

        #url = "https://www.google.com/"
        url = "https://www.microsoft.com/store/productId/9PHKKZGRQ0L1"
        webbrowser.open(url, new=0, autoraise=True)

    likeButton = Button(buttonFrame,
                        image=like_button_image,
                        borderwidth=0,
                        command=likeButton,
                        background=button_frame_color,
                        activebackground=button_frame_color)
    likeButton.grid(row=2, column=0)

    def like_button_hover(e):
        likeButton.config(image=like_hover_image)

    def like_button_leave(e):
        likeButton.config(image=like_button_image)

    likeButton.bind("<Enter>", like_button_hover)
    likeButton.bind("<Leave>", like_button_leave)

    # <<<<<<< achievements >>>>>>>
    achievement_button_image = PhotoImage(file="files/button1 (7).png")
    def achievementsCommand():
        pygame.mixer.music.load("files/click_04.wav")
        pygame.mixer.music.play(0)
        achievements.run_achievement()


    achievementsButton = Button(buttonFrame,
                                image=achievement_button_image,
                                borderwidth=0,
                                command=achievementsCommand,
                                bg=button_frame_color,
                                activebackground=button_frame_color)
    achievementsButton.grid(row=3, column=0)

    def achievement_button_hover(e):

        achievementsButton.config(image=achievement_hover_image)

    def achievement_button_leave(e):
        achievementsButton.config(image=achievement_button_image)

    achievementsButton.bind("<Enter>", achievement_button_hover)
    achievementsButton.bind("<Leave>", achievement_button_leave)



    window.title("Quiz")
    window.mainloop()

login()


