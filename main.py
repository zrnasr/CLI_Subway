from src import *
import time
import logging
from debug import *

class Main:
    @staticmethod
    def run():
        while True:
            clear()
            print('Select one of the below')
            show_menu(Menu.user_options)

            user_input_menu = input('Choose: ')
            # REGISTER
            if user_input_menu == '1':
                clear()
                name = input('Enter username: ')
                password = input('Enter password: ')
                user_obj = User(name, password)
                register_user(user_obj)

                print('You Are Now Part of METRO')
                print(f'Your Metro ID: {user_obj.id}')
                input('Done, Press any key to continue...')
            # LOGIN
            elif user_input_menu == '2':
                clear()
                user_id = input('Enter Unique ID(Forgot password?(y)): ')
                log_in_flag = False
                logged_in_person = None
                if user_id == 'y':
                    clear()
                    get_unique_id_from_username()
                else:
                    try:
                        user_obj = get_unique_id(user_id)
                        logged_in_person = user_obj
                        log_in_flag = True
                    except FileNotFoundError:
                        input("User not found!, Press any key to continue ...")
                while log_in_flag:
                    clear()
                    show_menu(Menu.login_menu)
                    login_user_input = input("What do you want to do next? ")

                    # BANK ACCOUNT MANAGEMENT
                    if login_user_input == '1':
                        clear()
                        show_menu(Menu.bank_acount_menu)
                        user_input = input("Choose: ")

                        # DEPOSIT
                        if user_input == '1':
                            clear()
                            amount = input('How much do you want to deposit? ')
                            print('Sending Data to the Server ...')
                            logged_in_person.make_deposit(float(amount))
                            time.sleep(1)
                            print('Receiving Data from the Server ...')
                            print(f"Operation was successful. Your account balance: {logged_in_person.account.balance}")
                            subway_logger.info(f"Deposit was successful. Your account balance: {logged_in_person.account.balance}")
                            input('Done. Press any key to continue ...')

                        # WITHDRAW
                        elif user_input =='2':
                            clear()
                            try:
                                amount = input('How much do you want to withdraw? ')
                                print('Sending Data to the Server ...')
                                logged_in_person.make_withdraw(float(amount))
                                time.sleep(1)
                                print('Receiving Data from the Server ...')
                                subway_logger.info(f"Withdrawal was successful. Now, your account balance is {logged_in_person.account.balance}.")
                                print(f"Withdrawal was successful. Now, your account balance is {logged_in_person.account.balance}.")                            
                                input('Done. Press any key to continue ...')
                            except AssertionError:
                                subway_logger.error(f"Withdrawal failed. Not enough money available!")
                                input('Not enough money is available! Press any key to continue ...')

                        # SHOW BALANCE
                        elif user_input == '3':
                            clear()
                            try:
                                acc_balance = logged_in_person.show_balance(logged_in_person.username)
                                subway_logger.info(acc_balance)
                                print (acc_balance)
                                
                                input('Done. Press any key to continue ...')
                            except AssertionError as e:
                                subway_logger.error("Operation of taking balance failed")
                                input('Failed. Press any key to continue ...')

                    # BUY TICKET                
                    elif login_user_input == '2':
                        clear()
                        show_menu(Menu.buy_ticket_menu)
                        user_ticket_choice = input('choose: ')

                        if user_ticket_choice == '1':
                            try:
                                logged_in_person.make_withdraw(55)
                                ch_ticket = ChargebleTicket()
                                pickle_tickets(ch_ticket)
                                logged_in_person.buy_ticket(ch_ticket)
                                ticket_logger.info(f"Buying chargeable ticket successfully.{logged_in_person.ticket_list}")
                                print(logged_in_person.ticket_list)
                                input("Done. Press any key to continue ...")
                            except AssertionError:
                                ticket_logger.error("Failure in buying chargeable ticket.")
                                input("Failure in buying chargeable ticket. Please charge your ticket!")
                                
                        elif user_ticket_choice == '3':
                            try:
                                logged_in_person.make_withdraw(55)
                                ex_ticket = ExpirableTicket()
                                pickle_tickets(ex_ticket)
                                logged_in_person.buy_ticket(ex_ticket)
                                # print(logged_in_person.ticket_list)
                                input("C...")
                            except AssertionError as e:
                                print(e)
                                input('C...')
                        elif user_ticket_choice == '4':
                            clear()
                            for i in enumerate(logged_in_person.show_ticket_list(), 1):
                                print(i, '\n') #indent=2)
                            input('C...')

                        elif user_ticket_choice == '5':
                            temp = []
                            for ticket in enumerate(logged_in_person.show_ticket_list(), 1):
                                if isinstance(ticket[1], ChargebleTicket):
                                    print( ticket, indent=1)
                                    temp.append(ticket)
                            charging = int(input('which card would you like to chrage? '))
                            amount = int(input('How much you want to charge your card?\n1.20\n2.30\n3.40\n'))
                            list_of_prices = [20, 30, 40]
                            logged_in_person.make_withdraw(list_of_prices[amount - 1])
                            # logged_in_person.ticket_list[charging - 1].charge_ticket(list_of_prices[amount-1])
                            logged_in_person.charge_chargeble_ticket(charging, list_of_prices[amount - 1])

                            print(logged_in_person.ticket_list)
                            input()


                    elif login_user_input =='3':
                        clear()
                        for i in enumerate(logged_in_person.show_ticket_list(), 1):
                                print(i, '\n') #indent=2)
                        chosen_ticket = input('Which ticket would you like to use for this Trip? ')

                        try:
                            if len(chosen_ticket) == 1 and chosen_ticket.isdigit():
                                logged_in_person.use_ticket_bynumber(int(chosen_ticket))
                            elif len(chosen_ticket) > 1:
                                logged_in_person.use_ticket_byid(chosen_ticket)

                            # logged_in_person.ticket_list[int(chosen_ticket) - 1].use_ticket()
                            print(logged_in_person.ticket_list)
                            input('Ticket has been used successfuly...')
                            input('You can now travel using metro...')
                        except AssertionError as e:
                            print(e)
                            input('C...')

                    elif login_user_input == '4':
                        with open(f'users/{logged_in_person.id}.pickle', 'wb') as user:
                            pickle.dump(logged_in_person, user)
                        break

            elif user_input_menu == '3':
                clear()
                admin_username = input('Enter username: ')
                admin_password = input('Enter password: ')
                admin_objs = []
                for file in glob.glob("admin/*.pickle"):
                    with open(file, 'rb') as admin:
                        while True:
                            try:
                                content = pickle.load(admin)
                                admin_objs.append(content)
                            except EOFError:
                                break

                for admin in admin_objs:
                    if admin.username == admin_username and admin.password == admin_password:
                        show_menu(Menu.admin_menu)
                        admin_input = input('Choose: ')

                        if admin_input == '1':
                            name = input('Enter username: ')
                            password = input('Enter password: ')
                            admin_obj = Admin(name, password)
                            with open(f"admin/{admin_obj.id}.pickle" , 'wb') as admin:
                                pickle.dump(admin_obj, admin)
                            print('You Are Now METRO Admin')
                            print(f'Your Metro ID: {admin_obj.id}')
                            input('C...')

                        elif admin_input == '7':
                            ticket_id = input('Enter ticket ID')
                            os.chdir('tickets')
                            os.system(f'del {ticket_id}.pickle' if os.name =='nt' else f"rm {ticket_id}.pickle")
                            input()
                    else:
                        print("INVALID INPUT")
                        input('C...')

            elif user_input_menu == '4':
                break




if __name__ == '__main__':
    Main.run()