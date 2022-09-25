from tkinter import *
import pygame
import win32com.client as win32
pygame.mixer.init()

def aboutCommand():
    pygame.mixer.music.load("files/04.click.wav")
    pygame.mixer.music.play(0)
    aboutWindow = Toplevel()
    main_color = "#24094e"
    heading_color = "#f8a616"
    aboutWindow.config(bg=main_color, borderwidth=2,
                                  relief=RAISED)
    aboutWindow.overrideredirect(True)

    about_width = 820
    about_height = 450

    screen_width = aboutWindow.winfo_screenwidth()  # width of the screen
    screen_height = aboutWindow.winfo_screenheight()  # height of the screen

    about_center_x = (screen_width / 2) - (about_width / 2)  # find the location of app on the x coordinate
    about_center_y = (screen_height / 2) - (about_height / 2)  # find the location of app on the y coordinate
    aboutWindow.geometry("{}x{}+{}+{}".format(about_width, about_height, int(about_center_x), int(about_center_y)))


    text0 = "QAYDALAR"
    text1 = "Oyunda göstərilən pul mükafatı həqiqi deyil və sadəcə oyun üçün nəzərdə tutulmuşdur.\n" \
            "Oyun 15 sualdan ibarətdir. Hər sual üçün 4 variant mövcuddur, variantlardan yalnız biri doğrudur.\n" \
            "Oyun zamanı 3 kömək haqqınız var və hər birindən yalnız 1 dəfə istifadə etmək olur.\n" \
            "15 suala düzgün cavab verən iştirakçı, oyunun qalibi olur.\n" \
            "İlk 5 sual asan, sonrakı 5 sual bir az çətin və son 5 sual isə daha çətin səviyyələnmişdir."

    about_label = Label(aboutWindow,
                        font=("arial", 14, "bold"),
                        text=text0,
                        foreground=heading_color,
                        background=main_color)
    about_label.grid(row=0, column=0, padx=5, pady=5)

    about_label = Label(aboutWindow, font=("arial", 14), text=text1,
                        foreground="WHITE", background=main_color)
    about_label.grid(row=1, column=0, padx=5)

    text15 = "HAQQINDA"
    text2 = "Oyun boş vaxtlarınızda biliklərinizi təkrar etmək və yeni biliklər öyrənmək üçün əla vasitədir.\n"\
            "Oyunda Müxtəlif mövzulara aid suallar yer alıb."

    about_label15 = Label(aboutWindow,
                          font=("arial", 14, "bold"),
                          text=text15,
                          foreground=heading_color,
                          background=main_color)
    about_label15.grid(row=2, column=0, padx=5, pady=5)

    about_label2 = Label(aboutWindow,
                         font=("arial", 14),
                         text=text2,
                         foreground="WHITE",
                         background=main_color)
    about_label2.grid(row=3, column=0, padx=5)

    text3 = "ƏLAQƏ"
    about_label3 = Label(aboutWindow, font=("arial", 15, "bold"), text=text3,
                         foreground=heading_color, background=main_color)
    about_label3.grid(row=4, column=0, pady=5)

    text4 = "Tələb və təklifləriniz üçün bizə yazın:"
    about_label4 = Label(aboutWindow, font=("arial", 15), text=text4,
                         foreground="WHITE", background=main_color)
    about_label4.grid(row=5, column=0)

    def email_button_command():
        olApp = win32.Dispatch('Outlook.Application')
        olNS = olApp.GetNameSpace('MAPI')
        # construct email item object
        mailItem = olApp.CreateItem(0)
        mailItem.Subject = 'Tələb və təkliflər'
        mailItem.BodyFormat = 1
        mailItem.To = '<electro.anonym@gmail.com>'
        mailItem.Sensitivity = 2
        mailItem.Display()
        mailItem.Save()

    email_button = Button(aboutWindow,
                          text="electro.anonym@gmail.com",
                          font=("arial", 14, "bold"),
                          background=main_color,
                          activebackground=main_color,
                          foreground="GREEN",
                          activeforeground="GREEN",
                          command=email_button_command)
    email_button.grid(row=6, column=0)


    # BUTTON
    def exit_command():
        pygame.mixer.music.load("files/04.click.wav")
        pygame.mixer.music.play(0)
        aboutWindow.destroy()

    exit_button_image = PhotoImage(file="files/exit_button_about.png")
    exit_button_hover_image = PhotoImage(file="files/exit_button_about_dots.png")
    exit_button = Button(aboutWindow,
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

    aboutWindow.mainloop()


