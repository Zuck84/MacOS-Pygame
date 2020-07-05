"""
    when we want to increase offer: less taxes on companies/capitalists ==> +profit
        WHICH LEADS TO: +investment ==> -unemployment & +inflation (growth) ==> +offer ==> -growth ==> +unemployment & -inflation ==> [cycle starts again]
                                             ^
                                more education when a lot of tech/consolid capital (to favor employment or variable capital)


    when we want to increase demand: less taxes on workers ==> +demand ==> +profit
        WHICH LEADS TO: +investment ==> -unemployment & +inflation (growth) ==> +offer ==> -growth ==> +unemployment & -inflation ==> [cycle starts again]
                                              ^
                                more education when a lot of tech/consolid capital (to favor employment or variable capital)


    BIGGER BOOMS (BUT ALSO BIGGER RECESSIONS): less taxes on workers & companies ==> +demand and -unemployment ==> +profit(+investment) & +inflation (BIG BOOM)==> a lot more profit
                                                                                            ^
                                                            more education when a lot of tech/consolid capital (to favor employment or variable capital)

        WHICH LEADS TO:  a lot more offer ==> -growth(BIG RECESSION) ==> +unemployment & -inflation ==> [cycle starts again]





WHEN PROFIT IS NOT REINVESTED WE NEED TO REDISTRIBUTE IT TO WAGES TO INCREASE DEMAND

+inflation & -unemployment = +growth
-inflation & +unemployment = -growth
"""

"""
96.5 % of the population ==> 48.25 demand pts
3.5 % of the population ==> 1.75 demand pts
100% ==> 50
"""

import os
#os.system("clear")
os.system("cls")

import tkinter

def situation1_boom():
    os.system("cls")
    print("First Situation: \n")

    #General
    unemployment = 3.5
    unemployment = float(unemployment)

    inflation = 4.5
    inflation = float(inflation)

    total_wages = 80.4
    total_wages = float(total_wages)

    work_taxes = 40/100
    work_taxes = float(work_taxes)

    offer = inflation - unemployment
    offer = float(offer)

    demand = total_wages - total_wages * work_taxes
    demand = float(demand)

    """
    investment/unemployment = 8.4
    29.5/3.5 = 8.4

    investment/8.4 = unemployment

    8.4 * unemployment = investment
    """

    #Capitalists
    cap_taxes = 50/100
    cap_taxes = float(cap_taxes)

    total_profit = demand - offer
    total_profit = float(total_profit)

    investment = total_profit - total_profit * cap_taxes
    investment = float(investment)

    growth = demand + investment
    growth = float(growth)

    print("\n unemployment:", unemployment, "%", "\n inflation:", inflation, "%", "\n wages(total):", total_wages, "\n taxes on workers:", work_taxes * 100, "%", "\n offer:", offer, "\n demand:", demand, "\n taxes on capitalists:", cap_taxes * 100, "%", "\n total profit:", total_profit, "\n investment:", investment, "\n growth:", growth, "\n \n \n less than 5% of an unemployment means there isn't a lot while more than 3% of inflation means a lot")

    command = input("\n \n enter '*commands' to access to the list of different commands \n \n How would you react ? we want high growth and a good long term policy type >>> ")

    if command == "*laissez_faire":
        print("Growth:", growth)
        print("\n" "\n" "\n Perfect! We are at a period of boom in the economic cycle. \n More taxes would have just increased unemployment and lowered demand, profit and investment. There would have been a recession.")
        def menu():
            os.system("cls")
            situation = input("Choose a situation: \n \n enter b to try the boom \n enter r to try the recession \n enter hh to try high unemployment & high inflation \n enter ui to try low unemployment & low inflation n \n \n enter q to quit the program \n \n \n ==> ")

            if situation == "b":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation1_boom()


            elif situation == "r":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation2_recession()

            elif situation == "hh":
                print("HIGH UNEMPLOYMENT AND HIGH INFLATION")
            elif situation == "ui":
                print("LOW UNEMPLOYMENT AND LOW INFLATION")
            elif situation == "q":
                print("\n \n End of the program...")
            else:
                menu()

        menuorquit = input("\n \n \n \n \n Enter m to go back to menu \n Enter any key to quit the program \n \n \n ==> ")
        if menuorquit == "m":
            menu()
        else:
            print("\n \n End of the Program...")

    elif command == "*tax workers":
        increase_workers_taxes = float(input("Taxes are now at 40%, please type the increase (between 5 & 55) >>> "))

        new_work_tax = work_taxes + increase_workers_taxes/100
        new_work_tax = float(new_work_tax)

        new_demand = total_wages - new_work_tax * total_wages
        new_demand = float(new_demand)

        new_profit = new_demand - offer
        new_profit = float(new_profit)

        new_investment = new_profit - cap_taxes * new_profit
        new_investment = float(new_investment)

        new_growth = new_investment + new_demand
        new_growth = float(new_growth)

        new_unemployment = unemployment + (investment/3 - new_investment/3)
        new_unemployment = float(new_unemployment)
        if new_unemployment > 40:
            new_unemployment = 40

        new_inflation = 8 - new_unemployment
        new_inflation = float(new_inflation)
        if new_inflation < 1:
            new_inflation = 1

        print("\n \n \n Impact of your policy:")
        print("new taxes on workers:", new_work_tax * 100, "%","\n unemployment:", new_unemployment, "\n inflation:", new_inflation, "\n wages(total):", total_wages, "\n offer:", offer, "\n demand:", new_demand, "\n taxes on capitalists:", cap_taxes * 100, "%", "\n total profit:", new_profit, "\n investment:", new_investment, "\n growth:", new_growth)
        print("\n \n Your economic policy has been desastrous on this situation, growth and buying power went down and unemployment increased. There is a recession because of you.")

        def menu():
            os.system("cls")
            situation = input("Choose a situation: \n \n enter b to try the boom \n enter r to try the recession \n enter hh to try high unemployment & high inflation \n enter ui to try low unemployment & low inflation n \n \n enter q to quit the program \n \n \n ==> ")

            if situation == "b":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation1_boom()


            elif situation == "r":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation2_recession()

            elif situation == "hh":
                print("HIGH UNEMPLOYMENT AND HIGH INFLATION")
            elif situation == "ui":
                print("LOW UNEMPLOYMENT AND LOW INFLATION")
            elif situation == "q":
                print("\n \n End of the program...")
            else:
                menu()

        menuorquit = input("\n \n \n \n \n Enter m to go back to menu \n Enter any key to quit the program \n \n \n ==> ")
        if menuorquit == "m":
            menu()
        else:
            print("\n \n End of the Program...")


    elif command == "*tax capitalists":
        increase_cap_taxes = input("\n \n Taxes are now at 50% on capitalists, how much do you want to increase them (between 5 & 45)? >>> ")
        increase_cap_taxes = float(increase_cap_taxes)

        new_cap_taxes = cap_taxes + increase_cap_taxes/100
        new_cap_taxes = float(new_cap_taxes)

        new_unemployment = unemployment + increase_cap_taxes/4
        new_unemployment = float(new_unemployment)
        if new_unemployment > 40:
            new_unemployment = 40

        new_inflation = 8 - new_unemployment
        new_inflation = float(new_inflation)
        if new_inflation < 1:
            new_inflation = 1

        new_offer = new_inflation - new_unemployment
        new_offer = float(new_offer)
        if new_offer < 1.5:
            new_offer = 1.5

        new_wages = total_wages - new_cap_taxes * 100
        new_wages = float(new_wages)

        new_demand = new_wages - work_taxes
        new_demand = float(new_demand)

        new_profit = new_demand - new_offer
        new_profit = float(new_profit)

        new_investment = new_profit - new_cap_taxes
        new_investment = float(new_investment)

        new_growth = new_investment + new_demand

        if new_growth < 0.5:
            new_growth = 0.5

        if new_wages < 0.04:
            new_wages = 0.04

        if new_investment < 0.25:
            new_investment = 0.25

        if new_profit  < 0.1:
            new_profit = 0.1

        if new_demand < 0.1:
            new_demand = 0.1

        print("new tax on capitalists:", new_cap_taxes * 100, "% \n \n unemployment:", new_unemployment, "\n inflation:", new_inflation, "\n wages:", new_wages, "\n offer:", new_offer, "\n demand:", new_demand, "\n total profit:", new_profit, "\n investment:", new_investment, "\n \n growth:", new_growth)
        print("\n \n \n Your economic policy has been desastrous on this situation, growth and buying power went down and unemployment increased. There is a recession because of you.")

        def menu():
            os.system("cls")
            situation = input("Choose a situation: \n \n enter b to try the boom \n enter r to try the recession \n enter hh to try high unemployment & high inflation \n enter ui to try low unemployment & low inflation n \n \n enter q to quit the program \n \n \n ==> ")

            if situation == "b":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation1_boom()


            elif situation == "r":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation2_recession()

            elif situation == "hh":
                print("HIGH UNEMPLOYMENT AND HIGH INFLATION")
            elif situation == "ui":
                print("LOW UNEMPLOYMENT AND LOW INFLATION")
            elif situation == "q":
                print("\n \n End of the program...")
            else:
                menu()

        menuorquit = input("\n \n \n \n \n Enter m to go back to menu \n Enter any key to quit the program \n \n \n ==> ")
        if menuorquit == "m":
            menu()
        else:
            print("\n \n End of the Program...")

    elif command == "*tax everyone":

        print("\n \n You are going to choose how much you want to tax capitalists and then workers.")

        increase_workers_taxes = float(input("Taxes on workers are now at 40%, please type the increase (between 5 & 55) >>> "))

        increase_cap_taxes = (float(input("\n Taxes are now at 50% on capitlists, how much do you want to increase them (between 5 & 45)? >>> ")))

        new_work_tax = work_taxes + increase_workers_taxes/100
        new_work_tax = float(new_work_tax)

        new_cap_taxes = cap_taxes + increase_cap_taxes/100
        new_cap_taxes = float(new_cap_taxes)

        new_demand = total_wages - new_work_tax * total_wages
        new_demand = float(new_demand)

        new_unemployment = unemployment + increase_cap_taxes/4
        new_unemployment = float(new_unemployment)
        if new_unemployment > 40:
            new_unemployment = 40

        new_inflation = 8 - new_unemployment
        new_inflation = float(new_inflation)
        if new_inflation < 1:
            new_inflation = 1

        new_offer = new_inflation - new_unemployment
        new_offer = float(new_offer)
        if new_offer < 1:
            new_offer = 1

        new_wages = total_wages - new_cap_taxes * 100
        new_wages = float(new_wages)

        new_demand = new_wages - new_work_tax
        new_demand = float(new_demand)

        new_profit = new_demand - new_offer
        new_profit = float(new_profit)

        new_investment = new_profit - new_cap_taxes
        new_investment = float(new_investment)

        new_growth = new_investment + new_demand

        print("new tax on capitalists:", new_cap_taxes * 100, "% \n \n unemployment:", new_unemployment, "\n inflation:", new_inflation, "\n wages:", new_wages, "\n offer:", new_offer, "\n demand:", new_demand, "\n total profit:", new_profit, "\n investment:", new_investment, "\n \n growth:", new_growth)
        print("\n \n \n Your economic policy has been desastrous on this situation, growth and buying power went down and unemployment increased. There is a recession because of you.")

        def menu():
            os.system("cls")
            situation = input("Choose a situation: \n \n enter b to try the boom \n enter r to try the recession \n enter hh to try high unemployment & high inflation \n enter ui to try low unemployment & low inflation n \n \n enter q to quit the program \n \n \n ==> ")

            if situation == "b":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation1_boom()


            elif situation == "r":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation2_recession()

            elif situation == "hh":
                print("HIGH UNEMPLOYMENT AND HIGH INFLATION")
            elif situation == "ui":
                print("LOW UNEMPLOYMENT AND LOW INFLATION")
            elif situation == "q":
                print("\n \n End of the program...")
            else:
                menu()

        menuorquit = input("\n \n \n \n \n Enter m to go back to menu \n Enter any key to quit the program \n \n \n ==> ")
        if menuorquit == "m":
            menu()
        else:
            print("\n \n End of the Program...")

    elif command == "*subventions capitalists":

        #SHORT TERM
        lower_capitalists_tax = input("Taxes are now at 50% on capitalists, how much do you want to reduce them? (choose a number between 5 & 49) >>> ")
        lower_capitalists_tax = float(lower_capitalists_tax)

        new_cap_taxes = cap_taxes - lower_capitalists_tax/100
        new_cap_taxes = float(new_cap_taxes)

        new_demand = demand
        new_demand = float(new_demand)

        new_unemployment = unemployment - lower_capitalists_tax/4
        new_unemployment = float(new_unemployment)
        if new_unemployment < 2.5:
            new_unemployment = 2.5

        new_inflation = 8 - new_unemployment
        new_inflation = float(new_inflation)
        if new_inflation < 5:
            new_inflation = 5

        new_offer = new_inflation - new_unemployment
        new_offer = float(new_offer)
        if new_offer < 1:
            new_offer = 1

        new_wages = total_wages + lower_capitalists_tax * 100
        new_wages = float(new_wages)
        if new_wages > 250:
            new_wages = 250

        new_demand = demand
        new_demand = float(new_demand)

        new_profit = new_demand - new_offer
        new_profit = float(new_profit)

        new_investment = new_profit - new_cap_taxes
        new_investment = float(new_investment)

        new_growth = new_investment + new_demand

        print("\n \n Here is how the economy is going to react in the short term: ")
        print("new tax on capitalists:", new_cap_taxes * 100, "% \n \n unemployment:", new_unemployment, "\n inflation:", new_inflation, "\n wages:", new_wages, "\n offer:", new_offer, "\n demand:", new_demand, "\n total profit:", new_profit, "\n investment:", new_investment, "\n \n growth:", new_growth)

        #LONG TERM
        new_new_demand = demand - new_inflation * 7
        new_new_demand = float(new_new_demand)

        new_new_profit = new_new_demand - new_offer
        new_new_profit = float(new_profit)

        new_new_investment = new_new_profit - new_cap_taxes
        new_new_investment = float(new_new_investment)

        new_new_unemployment = new_unemployment + (new_new_investment)
        new_new_unemployment = float(new_new_unemployment)
        if new_new_unemployment > 30:
            new_new_unemployment = 30

        new_new_growth = new_new_investment + new_new_demand

        print("\n \n \n Here you have how the economy will react in the long term: \n \n New growth:", new_new_growth, "\n New demand:", new_new_demand, "\n New Unemployment:", new_new_unemployment, "\n New inflation:", new_inflation, "\n \n \n As you can see, your policy was good on the short term but created a recession in the long term, economy doesn't work like that!")

        def menu():
            os.system("cls")
            situation = input("Choose a situation: \n \n enter b to try the boom \n enter r to try the recession \n enter hh to try high unemployment & high inflation \n enter ui to try low unemployment & low inflation n \n \n enter q to quit the program \n \n \n ==> ")

            if situation == "b":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation1_boom()


            elif situation == "r":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation2_recession()

            elif situation == "hh":
                print("HIGH UNEMPLOYMENT AND HIGH INFLATION")
            elif situation == "ui":
                print("LOW UNEMPLOYMENT AND LOW INFLATION")
            elif situation == "q":
                print("\n \n End of the program...")
            else:
                menu()

        menuorquit = input("\n \n \n \n \n Enter m to go back to menu \n Enter any key to quit the program \n \n \n ==> ")
        if menuorquit == "m":
            menu()
        else:
            print("\n \n End of the Program...")

    elif command == "*subventions workers":
        lower_workers_taxes = float(input("Taxes are now at 40%, please type how much you want to lower the taxes on workers (between 5 & 55) >>> "))

        #SHORT TERM
        new_wages = total_wages
        new_wages = float(new_wages)

        new_work_tax = work_taxes - lower_workers_taxes/100
        new_work_tax = float(new_work_tax)

        new_demand = total_wages - new_work_tax * total_wages
        new_demand = float(new_demand)

        new_offer = offer
        new_offer = float(new_offer)

        new_profit = new_demand - offer
        new_profit = float(new_profit)

        new_investment = new_profit - cap_taxes * new_profit
        new_investment = float(new_investment)

        new_growth = new_investment + new_demand
        new_growth = float(new_growth)

        new_unemployment = unemployment + (investment/3 - new_investment/3)
        new_unemployment = float(new_unemployment)
        if new_unemployment < 2.5:
            new_unemployment = 2.5

        new_inflation = 8 - new_unemployment
        new_inflation = float(new_inflation)
        if new_inflation > 8:
            new_inflation = 8

        if new_demand > 49.9:
            new_demand = 49.9

        print("\n \n Here is how the economy is going to react in the short term: ")
        print("new tax on workers:", new_work_tax * 100, "% \n \n unemployment:", new_unemployment, "\n inflation:", new_inflation, "\n wages:", new_wages, "\n offer:", new_offer, "\n demand:", new_demand, "\n total profit:", new_profit, "\n investment:", new_investment, "\n \n growth:", new_growth)

        #LONG TERM
        new_new_demand = new_demand - new_inflation * 13
        new_new_demand = float(new_new_demand)
        if new_new_demand < 1:
            new_new_demand = 1

        new_new_profit = new_new_demand - new_offer
        new_new_profit = float(new_profit)

        new_new_investment = new_new_profit - cap_taxes
        new_new_investment = float(new_new_investment)

        new_new_unemployment = new_unemployment + (new_new_investment)
        new_new_unemployment = float(new_new_unemployment)
        if new_new_unemployment > 30:
            new_new_unemployment = 30

        new_new_growth = new_new_investment + new_new_demand
        if new_new_growth > 89:
            new_new_growth = 80

        print("\n \n \n Here you have how the economy will react in the long term: \n \n New growth:", new_new_growth, "\n New demand:", new_new_demand, "\n New unemployment:", new_new_unemployment, "\n \n \n As you can see, your policy was good on the short term but created a recession in the long term, economy doesn't work like that!")

        def menu():
            os.system("cls")
            situation = input("Choose a situation: \n \n enter b to try the boom \n enter r to try the recession \n enter hh to try high unemployment & high inflation \n enter ui to try low unemployment & low inflation n \n \n enter q to quit the program \n \n \n ==> ")

            if situation == "b":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation1_boom()


            elif situation == "r":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation2_recession()

            elif situation == "hh":
                print("HIGH UNEMPLOYMENT AND HIGH INFLATION")
            elif situation == "ui":
                print("LOW UNEMPLOYMENT AND LOW INFLATION")
            elif situation == "q":
                print("\n \n End of the program...")
            else:
                menu()

        menuorquit = input("\n \n \n \n \n Enter m to go back to menu \n Enter any key to quit the program \n \n \n ==> ")
        if menuorquit == "m":
            menu()
        else:
            print("\n \n End of the Program...")

    elif command == "*subventions everyone":
        print("You're going to lower taxes for capitalists and workers")

        lower_workers_taxes = float(input("Taxes on workers are now at 40%, please type how many you want to reduce them (between 5 & 35) >>> "))

        lower_cap_taxes = (float(input("\n Taxes are now at 50% on capitalists, how much do you want to reduce them (between 5 & 45)? >>> ")))

        new_work_tax = work_taxes - lower_workers_taxes
        new_work_tax = float(new_work_tax)

        new_cap_taxes = cap_taxes - lower_cap_taxes
        new_cap_taxes = float(new_cap_taxes)

        new_demand = total_wages - total_wages * new_work_tax
        new_demand = float(new_demand)

        new_unemployment = unemployment - new_cap_taxes/4
        new_unemployment = float(new_unemployment)
        if new_unemployment > 40:
            new_unemployment = 40

        new_inflation = 8 - new_unemployment
        new_inflation = float(new_inflation)
        if new_inflation < 1:
            new_inflation = 1

        new_offer = new_inflation - new_unemployment
        new_offer = float(new_offer)
        if new_offer < 1:
            new_offer = 1

        new_profit = new_demand - new_offer
        new_profit = float(new_profit)

        new_investment = new_profit - new_cap_taxes
        new_investment = float(new_investment)

        new_growth = new_investment + new_demand
        new_new_unemployment = float(new_new_unemployment)

        print("new tax on capitalists:", new_cap_taxes * 100, "% \n \n unemployment:", new_unemployment, "\n inflation:", new_inflation, "\n wages:", new_wages, "\n offer:", new_offer, "\n demand:", new_demand, "\n total profit:", new_profit, "\n investment:", new_investment, "\n \n growth:", new_growth)
        print("\n \n \n Your economic policy has been desastrous on this situation, growth and buying power went down and unemployment increased. There is a recession because of you.")

        def menu():
            os.system("cls")
            situation = input("Choose a situation: \n \n enter b to try the boom \n enter r to try the recession \n enter hh to try high unemployment & high inflation \n enter ui to try low unemployment & low inflation n \n \n enter q to quit the program \n \n \n ==> ")

            if situation == "b":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation1_boom()


            elif situation == "r":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation2_recession()

            elif situation == "hh":
                print("HIGH UNEMPLOYMENT AND HIGH INFLATION")
            elif situation == "ui":
                print("LOW UNEMPLOYMENT AND LOW INFLATION")
            elif situation == "q":
                print("\n \n End of the program...")
            else:
                menu()

        menuorquit = input("\n \n \n \n \n Enter m to go back to menu \n Enter any key to quit the program \n \n \n ==> ")
        if menuorquit == "m":
            menu()
        else:
            print("\n \n End of the Program...")


    elif command == "*profit-wages":
        print("\n \n \n Okay, you are going to give a part of the profit of the capitalists to increase workers' wages.")
        print("\n \n Capitalists have 50% of their profit that they can have as they want because the other part is taxed by the state. \n How many percents of capitalists' do you want to go to wages ?")

        profit_to_wages = float(input("\n \n ==> "))

        new_demand = demand + profit_to_wages
        new_demand = float(new_demand)

        new_offer = offer
        new_offer = float(new_offer)

        new_total_profit = new_demand - offer
        new_total_profit = float(new_total_profit)

        new_investment = investment
        new_investment = float(new_investment)

        new_unemployment = unemployment
        new_unemployment = float(new_unemployment)

        new_growth = growth

        new_growth = float(new_growth)
        print("unemployment:", new_unemployment, "%", "\n inflation:", inflation, "%", "\n wages:", total_wages, "\n demand:", new_demand, "\n profit:", new_total_profit, "\n investment:", new_investment, "\n growth:", new_growth)
        print("\n \n This policy is useless because it does not really change anything: even if profit are more taxed, they actually increase because by raising wages you made demand higher")

        def menu():
                os.system("cls")
                situation = input("Choose a situation: \n \n enter b to try the boom \n enter r to try the recession \n enter hh to try high unemployment & high inflation \n enter ui to try low unemployment & low inflation n \n \n enter q to quit the program \n \n \n ==> ")

                if situation == "b":
                    app = tkinter.Tk()
                    label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                    label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                    label_welcome.pack()
                    app.mainloop()
                    situation1_boom()


                elif situation == "r":
                    app = tkinter.Tk()
                    label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                    label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                    label_welcome.pack()
                    app.mainloop()
                    situation2_recession()

                elif situation == "hh":
                    print("HIGH UNEMPLOYMENT AND HIGH INFLATION")
                elif situation == "ui":
                    print("LOW UNEMPLOYMENT AND LOW INFLATION")
                elif situation == "q":
                    print("\n \n End of the program...")
                else:
                    menu()

        menuorquit = input("\n \n \n \n \n Enter m to go back to menu \n Enter any key to quit the program \n \n \n ==> ")
        if menuorquit == "m":
            menu()
        else:
            print("\n \n End of the Program...")

    elif command == "*state-workers":
        jobs = input("your population is 50 000 000 people, for now, 1 750 000 people are unemployed (3.5% of the population) \n \n How many jobs do you want to create ? (the state has the capacity to employ 500 000 people) \n \n >>> ")
        jobs = float(jobs)

        if jobs > 500000:
            print("The government can not afford to employ more than 500K, please try again")
            situation1_boom()
        else:
            more_employment = jobs * 100/50000000
            more_employment = float(more_employment)

            new_unemployment = unemployment - more_employment
            new_unemployment = float(new_unemployment)

            employment = 100 - new_unemployment
            employment = float(employment)

            new_wages = 80.4 * employment/96.5
            new_wages = float(new_wages)

            new_offer = offer
            new_offer = float(new_offer)

            new_demand = new_wages - new_wages * work_taxes
            new_demand = float(new_demand)

            new_inflation = 8 - new_unemployment
            new_inflation = float(new_inflation)

            new_total_profit = new_demand - new_offer
            new_total_profit = float(new_total_profit)

            new_investment = new_total_profit - cap_taxes
            new_investment = float(new_investment)

            new_growth = new_investment + new_demand
            new_growth = float(new_growth)

            print("\n demand:", new_demand, "\n offer:", new_offer, "\n profit:", new_total_profit, "\n investment:", new_investment, "\n new_inflation:", new_inflation, "\n unemployment:", new_unemployment, "\n growth", new_growth)
            print("\n \n PLEASE READ THIS: As you can see the results seem pretty good but the problem is that too much government spending could lead to a depression when there will be a recession. During a krach, the state needs to give money to the companies to bring growth back.")

            def menu():
                os.system("cls")
                situation = input("Choose a situation: \n \n enter b to try the boom \n enter r to try the recession \n enter hh to try high unemployment & high inflation \n enter ui to try low unemployment & low inflation n \n \n enter q to quit the program \n \n \n ==> ")

                if situation == "b":
                    app = tkinter.Tk()
                    label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                    label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                    label_welcome.pack()
                    app.mainloop()
                    situation1_boom()


                elif situation == "r":
                    app = tkinter.Tk()
                    label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                    label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                    label_welcome.pack()
                    app.mainloop()
                    situation2_recession()

                elif situation == "hh":
                    print("HIGH UNEMPLOYMENT AND HIGH INFLATION")
                elif situation == "ui":
                    print("LOW UNEMPLOYMENT AND LOW INFLATION")
                elif situation == "q":
                    print("\n \n End of the program...")
                else:
                    menu()

        menuorquit = input("\n \n \n \n \n Enter m to go back to menu \n Enter any key to quit the program \n \n \n ==> ")
        if menuorquit == "m":
            menu()
        else:
            print("\n \n End of the Program...")



        def menu():
            os.system("cls")
            situation = input("Choose a situation: \n \n enter b to try the boom \n enter r to try the recession \n enter hh to try high unemployment & high inflation \n enter ui to try low unemployment & low inflation n \n \n enter q to quit the program \n \n \n ==> ")

            if situation == "b":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation1_boom()


            elif situation == "r":
                app = tkinter.Tk()
                label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                label_welcome.pack()
                app.mainloop()
                situation2_recession()

            elif situation == "hh":
                print("HIGH UNEMPLOYMENT AND HIGH INFLATION")
            elif situation == "ui":
                print("LOW UNEMPLOYMENT AND LOW INFLATION")
            elif situation == "q":
                print("\n \n End of the program...")
            else:
                menu()

            menuorquit = input("\n \n \n \n \n Enter m to go back to menu \n Enter any key to quit the program \n \n \n ==> ")
            if menuorquit == "m":
                menu()
            else:
                print("\n \n End of the Program...")


    elif command == "*commands":
        app = tkinter.Tk()

        label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
        label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")

        label_welcome.pack()
        app.mainloop()

        #os.system("clear")
        os.system("cls")
        situation1_boom()

    elif command == "*quit":
        print("End of the program...")

    else:
        print("No, this command is not right")
        print("\n enter s to go back to the boom simulation")
        print("\n enter q to quit")
        print("\n enter any other key to go back to the menu")

        quitornot = input("\n \n ==> ")
        if quitornot == "s":
            situation1_boom()
        elif quitornot == "q":
            print("End of the program...")
        else:
            menu()

def situation2_recession():
    os.system("cls")
    print("Second Situation: \n ")

    #General
    unemployment = 10
    unemployment = float(unemployment)

    inflation = 2
    inflation = float(inflation)

    total_wages = 80.4
    total_wages = float(total_wages)

    work_taxes = 40/100
    work_taxes = float(work_taxes)

    offer = inflation - unemployment
    offer = float(offer)
    if offer < 1.5:
        offer = 1.5

    demand = total_wages - total_wages * work_taxes
    demand = float(demand)

      #Capitalists
    cap_taxes = 50/100
    cap_taxes = float(cap_taxes)

    total_profit = demand - offer
    total_profit = float(total_profit)

    investment = total_profit - total_profit * cap_taxes
    investment = float(investment)

    growth = demand + investment
    growth = float(growth)

    print("\n unemployment:", unemployment, "%", "\n inflation:", inflation, "%", "\n wages(total):", total_wages, "\n taxes on workers:", work_taxes * 100, "%", "\n offer:", offer, "\n demand:", demand, "\n taxes on capitalists:", cap_taxes * 100, "%", "\n total profit:", total_profit, "\n investment:", investment, "\n growth:", growth, "\n \n \n less than 5% of an unemployment means there isn't a lot while more than 3% of inflation means a lot")

    command = input("\n \n enter '*commands' to access to the list of different commands \n \n How would you react ? we want high growth and a good long term policy type >>> ")

    if command == "*commands":
        app = tkinter.Tk()

        label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
        label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")

        label_welcome.pack()
        app.mainloop()

        #os.system("clear")
        os.system("cls")
        situation2_recession()

    elif command == "*laissez_faire":
        print("The economic situation of the country did not change at all and it is going to be hard to bring growth back in the country. As John Keynes proved during the Great Depression of 1929, a state intervention to stimulate the economy is necessary in a recession.")

        def menu():
                os.system("cls")
                situation = input("Choose a situation: \n \n enter b to try the boom \n enter r to try the recession \n enter hh to try high unemployment & high inflation \n enter ui to try low unemployment & low inflation n \n \n enter q to quit the program \n \n \n ==> ")

                if situation == "b":
                    app = tkinter.Tk()
                    label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                    label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                    label_welcome.pack()
                    app.mainloop()
                    situation1_boom()


                elif situation == "r":
                    app = tkinter.Tk()
                    label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                    label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                    label_welcome.pack()
                    app.mainloop()
                    situation2_recession()

                elif situation == "hh":
                    print("HIGH UNEMPLOYMENT AND HIGH INFLATION")
                elif situation == "ui":
                    print("LOW UNEMPLOYMENT AND LOW INFLATION")
                elif situation == "q":
                    print("\n \n End of the program...")
                else:
                    menu()

        menuorquit = input("\n \n \n \n \n Enter m to go back to menu \n Enter any key to quit the program \n \n \n ==> ")
        if menuorquit == "m":
            menu()
        else:
            print("\n \n End of the Program...")


    elif command == "*tax workers":
            increase_workers_taxes = float(input("Taxes are now at 40%, please type the increase (between 5 & 55) >>> "))

            new_work_tax = work_taxes + increase_workers_taxes/100
            new_work_tax = float(new_work_tax)

            new_demand = total_wages - new_work_tax * total_wages
            new_demand = float(new_demand)

            new_profit = new_demand - offer
            new_profit = float(new_profit)

            new_investment = new_profit - cap_taxes * new_profit
            new_investment = float(new_investment)

            new_growth = new_investment + new_demand
            new_growth = float(new_growth)

            new_unemployment = unemployment + (investment/3 - new_investment/3)
            new_unemployment = float(new_unemployment)
            if new_unemployment > 40:
                new_unemployment = 40

            new_inflation = 12 - new_unemployment
            new_inflation = float(new_inflation)
            if new_inflation < 1:
                new_inflation = 1

                print("\n \n \n Impact of your policy:")
                print("new taxes on workers:", new_work_tax * 100, "%","\n unemployment:", new_unemployment, "\n inflation:", new_inflation, "\n wages(total):", total_wages, "\n offer:", offer, "\n demand:", new_demand, "\n taxes on capitalists:", cap_taxes * 100, "%", "\n total profit:", new_profit, "\n investment:", new_investment, "\n growth:", new_growth)
                print("\n \n Your economic policy has been desastrous on this situation, growth and buying power went down and unemployment increased. There is a recession because of you.")

            def menu():
                os.system("cls")
                situation = input("Choose a situation: \n \n enter b to try the boom \n enter r to try the recession \n enter hh to try high unemployment & high inflation \n enter ui to try low unemployment & low inflation n \n \n enter q to quit the program \n \n \n ==> ")

                if situation == "b":
                    app = tkinter.Tk()
                    label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                    label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                    label_welcome.pack()
                    app.mainloop()
                    situation1_boom()


                elif situation == "r":
                    app = tkinter.Tk()
                    label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
                    label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
                    label_welcome.pack()
                    app.mainloop()
                    situation2_recession()

                elif situation == "hh":
                    print("HIGH UNEMPLOYMENT AND HIGH INFLATION")
                elif situation == "ui":
                    print("LOW UNEMPLOYMENT AND LOW INFLATION")
                elif situation == "q":
                    print("\n \n End of the program...")
                else:
                    menu()

            menuorquit = input("\n \n \n \n \n Enter m to go back to menu \n Enter any key to quit the program \n \n \n ==> ")
            if menuorquit == "m":
                menu()
            else:
                print("\n \n End of the Program...")


from tkinter import*

root = Tk()

label_text = Label(root, text="Bienvenue à tous !", font=(None, 20))
label_text.configure(text="Before you start making choices, don't forget that this curve is usually right about the economy:")
label_text.pack()

photo = PhotoImage(file="curve.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()


def menu():
    os.system("cls")
    situation = input("Choose a situation: \n \n enter b to try the boom \n enter r to try the recession \n enter hh to try high unemployment & high inflation \n enter ui to try low unemployment & low inflation n \n \n enter q to quit the program \n \n \n ==> ")

    if situation == "b":
        app = tkinter.Tk()
        label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
        label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
        label_welcome.pack()
        app.mainloop()
        situation1_boom()


    elif situation == "r":
        app = tkinter.Tk()
        label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
        label_welcome.configure(text="List of the commands of the simulation: \n \n *laissez_faire: 100% classic free economy \n\n\n *tax workers: to tax workers (biggest social class of the society, they don't save money) \n\n\n*tax capitalists: to tax capitalists(richest social classes that usually reinvest their profit) \n\n\n *subventions workers: to reduce workers' tax \n\n\n *subventions capitalists: to reduce capitalists' tax \n\n\n *profit-wages: move money from profit to wages \n\n\n *state-workers: the state employs more people to reduce unemployment \n\n\n *quit: to quit the simulation \n\n\n *commands: to access to the list of different commands")
        label_welcome.pack()
        app.mainloop()
        situation2_recession()

    elif situation == "hh":
        print("HIGH UNEMPLOYMENT AND HIGH INFLATION")
    elif situation == "ui":
        print("LOW UNEMPLOYMENT AND LOW INFLATION")
    elif situation == "q":
        print("\n \n End of the program...")
    else:
        menu()

menu()

"""
List of reactions:
laissez-faire
tax workers
tax capitalists
tax everyone
subventions to capitalists
subventions to workers
subventions everyone
move profit to wages
more state spending to create more employment

List of situations:
- BOOM
- RECESSION
- high inflation and high unemployment
- low inflation and low unemployment
"""
