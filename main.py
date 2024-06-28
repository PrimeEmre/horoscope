import tkinter as tk
from tkinter import *
from tkinter import messagebox
class Horoscope:
    def __init__(self, root):
        # Setting the screen for BMI
        self.root = root
        self.root.title("Discover Your Horoscope")
        self.root.minsize(width=500, height=500)
        self.root.config(padx=50, pady=30)


    # Creating a label for the title
        self.title_label = Label(text="Discover Your Horoscope", font=('Noto Serif', 20), bg='cyan', fg='black')
        self.title_label.pack(pady=20)

        # Creating a label for the entry prompt
        self.Month = Label(text='Enter your Birth Month,and Year', font=('Merriweather', 12), bg='gold', fg='red')
        self.Month.pack(pady=10)

        # Creating an entry widget for user input
        self.horoscope_Month = Entry( font=('Merriweather', 12), bg='Aqua', fg='black')
        self.horoscope_Month.pack()
        # prompt is text#
        self.Birth_day = Label( text='Enter your Birth day', font=('Merriweather', 12), bg='slateblue', fg='white')
        self.Birth_day.pack(pady=20)
        self.horoscope_day = Entry( font=('Merriweather', 12), bg='silver', fg='black')
        self.horoscope_day.pack()

        # now we are going to create a button#
        self.button = Button(text='Find your Horoscope', font=('Inconsolata', 12), bg='black', fg='white',command= self.enter_Horoscope)
        self.button.pack(pady=20)

    def run(self):
        self.root.mainloop()

    # Now we are goig to create a functoin to claculate the usser's Horoscope #
    def enter_Horoscope(self):
        # Now we are going to identify the user's birthday and birth month a#
        self.Month = int(self.horoscope_Month.get())
        self.Birth_day = int(self.horoscope_day.get())
        self.Horoscope_name = ''
        '''♈ Aries (Ram): March 21–April 19-
    ♉ Taurus (Bull): April 20–May 20-
    ♊ Gemini (Twins): May 21–June 21-
    ♋ Cancer (Crab): June 22–July 22-
    ♌ Leo (Lion): July 23–August 22-
    ♍ Virgo (Virgin): August 23–September 22-
    ♎ Libra (Balance): September 23–October 23-
    ♏ Scorpius (Scorpion): October 24–November 21
    ♐ Sagittarius (Archer): November 22–December 21
    ♑ Capricornus (Goat): December 22–January 19
    ♒ Aquarius (Water Bearer): January 20–February 18-
    ♓ Pisces (Fish): February 19–March 20-'''
        match  self.Month:
                #January#
                case 1:
                    # Month is January horoscope can be Aquarius or Capricornus.

                    if self.Birth_day >= 20:
                        self.Horoscope_name = 'Aquarius (Water Bearer)'
                    else:
                        self.Horoscope_name='Sagittarius (Archer):'
               #February#
                case 2:
                    if self.Birth_day >= 19:
                        self.Horoscope_name = 'Pisces (Fish)'
                    else:
                        self.Horoscope_name = 'Aquarius (Water Bearer)'
                    #March#
                case 3:
                    if self.Birth_day >= 21:
                        self.Horoscope_name = 'Aries (Ram)'
                    else:
                        self.Horoscope_name = 'Pisces (Fish)'

                        #April#
                case 4:
                    if self.Birth_day >= 20:
                        self.Horoscope_name = 'Taurus (Bull)'
                    else:
                        self.Horoscope_name = 'Aries (Ram)'


                  #May#
                case 5:
                    if self.Birth_day >= 21:
                        self.Horoscope_name = ' Gemini (Twins)'
                    else:
                        self.Horoscope_name = 'Taurus (Bull)'

                    #June#
                case 6:
                    if self.Birth_day >= 22:
                        self.Horoscope_name = 'Cancer'
                    else:
                        self.Horoscope_name = 'Taurus (Bull)'
                    # July #
                case 7:
                    if self.Birth_day >= 23:
                        self.Horoscope_name = 'Leo (Lion)'
                    else:
                        self.Horoscope_name = 'Cancer'

                        #Augst#
                case 8:
                    if self.Birth_day >= 23:
                        self.Horoscope_name = 'Virgo (Virgin)'
                    else:
                        self.Horoscope_name = 'Leo (Lion)'

                    #September#
                case 9:
                    if self.Birth_day >= 23:
                        self.Horoscope_name = 'Libra (Balance)'
                    else:
                        self.Horoscope_name = 'Virgo (Virgin)'
               #October#
                case 10:
                    if self.Birth_day >= 24:
                        self.Horoscope_name = 'Scorpius (Scorpion)'
                    else:
                        self.Horoscope_name = 'Libra (Balance)'
               #November#
                case 11:
                    if self.Birth_day >= 19:
                        self.Horoscope_name = 'Sagittarius (Archer)'
                    else:
                        self.Horoscope_name = 'Scorpius (Scorpion)'

                    #December #
                case 12:
                    if self.Birth_day >= 22:
                        self.Horoscope_name = 'Capricornus (Goat)'
                    else:
                        self.Horoscope_name = 'Scorpius (Scorpion)'

        messagebox.showinfo("Horoscope", "Your Horoscope is "+self.Horoscope_name )

if __name__ == "__main__":
    root = tk.Tk()
    app = Horoscope(root)
    app.run()


