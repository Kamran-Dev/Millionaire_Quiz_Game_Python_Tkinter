from tkinter import *
import pygame

import game

pygame.mixer.init()



def close_the_game():
    import game
    game.closeit()


def run_main():
    import main
    main.login()


def game_over_command():

    game_over_window = Tk()
    game_over_window.overrideredirect(True)
    background_color = "#790ea1"

    width = 560
    height = 360

    screen_width = game_over_window.winfo_screenwidth()  # width of the screen
    screen_height = game_over_window.winfo_screenheight()  # height of the screen

    about_center_x = (screen_width / 2) - (width / 2)  # find the location of app on the x coordinate
    about_center_y = (screen_height / 2) - (height / 2)  # find the location of app on the y coordinate
    game_over_window.geometry("{}x{}+{}+{}".format(width, height, int(about_center_x), int(about_center_y)-45))

    game_over_window.config(background=background_color,
                            borderwidth=2,
                            relief=RAISED)

    game_over_frame = Frame(game_over_window, bg=background_color)
    game_over_frame.place(relx=0.5, rely=0.48, anchor=CENTER)

    game_over_label = Label(game_over_frame,
                            text="☹ OYUN BİTDİ! ☹",
                            background=background_color,
                            foreground="WHITE",
                            font=("System", 35, "bold"))
    game_over_label.grid(row=0, column=0, pady=10)
    amount = 32000
    player_win = Label(game_over_frame,
                              text="Qazanılan məbləğ",
                              background=background_color,
                              foreground="WHITE",
                              font=("arial", 20, "bold"))
    player_win.grid(row=1, column=0, pady=5)
    #amount_player_win.pack(pady=5)

    amount_player_win = Label(game_over_frame,
                       text=game.amount_win,
                       background=background_color,
                       foreground="#f8a616",
                       font=("Terminal", 25, "bold"))
    amount_player_win.grid(row=2, column=0, pady=5)



    # <<<<<<< BACK TO MENU BUTTON >>>>>>>
    def main_menu_command():
        pygame.mixer.music.load("files/click_04.wav")
        pygame.mixer.music.play(0)
        print("Part1")
        game_over_window.destroy()
        print("Part2")
        close_the_game()
        print("Part3")
        run_main()

    back_to_menu_button = Button(game_over_frame,
                                 command=main_menu_command,
                                 text="Əsas səhifə",
                                 #bg="#43A41B",
                                 bg="#61EC28",
                                 font=("arial", 15, "bold"))
    back_to_menu_button.grid(row=3, column=0, pady=5)
    #back_to_menu_button.pack(pady=5)


    # <<<<<<< EXIT BUTTON >>>>>>>
    def exit_button_command():
        game_over_window.destroy()
        quit()

    exit_button_image = PhotoImage(file="files/button1 (6).png")
    exit_button = Button(game_over_frame,
                         #image=exit_button_image,
                         text="Çıxış",
                         bg="#61EC28",
                         command=exit_button_command,
                         font=("italic", 15, "bold")
                         )
    exit_button.image = exit_button_image
    # exit_button.pack(ipady=5)
    exit_button.grid(row=4, column=0, pady=5)
    game_over_window.mainloop()
