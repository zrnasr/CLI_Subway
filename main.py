from src import *
import time
from debug import *

class Main:
    @staticmethod
    def run():
        while True:
            clear()
            print('Select one of the below')
            show_menu(Menu.main_menu)

            user_input_menu = input('Choose: ')
            # REGISTER
            if user_input_menu == '1':
                clear()
                name = input('Enter username: ')
                password = input('Enter password: ')
                user_obj = User(name, password)
                save_user(user_obj)

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
                        usr = user_obj.find_user(f'{user_id}.pickle', 'user/')
                        
                        if usr.banned_user:
                            user_logger.error("User is in black list!")
                            input("User is in black list! Press any key to continue ...")
                        else:
                            logged_in_person = user_obj
                            log_in_flag = True
                            user_logger.info("User logged in successfully!")
                            input("User logged in successfully. Press any key to continue ...")
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
                            bank_logger.info(f"Deposit was successful. Your account balance: {logged_in_person.account.balance}")
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
                                bank_logger.info(f"Withdrawal was successful. Now, your account balance is {logged_in_person.account.balance}.")
                                print(f"Withdrawal was successful. Now, your account balance is {logged_in_person.account.balance}.")                            
                                input('Done. Press any key to continue ...')
                            except AssertionError:
                                bank_logger.error(f"Withdrawal failed. Not enough money available!")
                                input('Not enough money is available! Press any key to continue ...')

                        # SHOW BALANCE
                        elif user_input == '3':
                            clear()
                            try:
                                acc_balance = logged_in_person.show_balance(logged_in_person.username)
                                bank_logger.info(acc_balance)
                                print (acc_balance)
                                
                                input('Done. Press any key to continue ...')
                            except AssertionError as e:
                                bank_logger.error("Operation of taking balance failed")
                                input('Failed. Press any key to continue ...')

                    elif login_user_input == '2':
                        clear()
                        show_menu(Menu.buy_ticket_menu)

                        user_ticket_choice = input('choose: ')
                        #BUY CHARGEBLE TICKET
                        tl = ["ChargebleTicket", "DisposableTicket", "ExpirableTicket" ]
                        c_flag = True
                        if user_ticket_choice == '1':
                            command = tl[0] + "()"
                        elif user_ticket_choice == '2':
                            command = tl[1] + "()"
                        elif user_ticket_choice == '3':
                            command = tl[2] + "()"
                        elif user_ticket_choice == '4':
                            clear()
                            for i in enumerate(logged_in_person.show_ticket_list(), 1):
                                print(i, '\n')
                            c_flag = False
                            input('Done, Press any key to continue ...')

                        # CHARGE TICKET
                        elif user_ticket_choice == '5':
                            temp = []
                            for ticket in enumerate(logged_in_person.show_ticket_list(), 1):
                                if isinstance(ticket[1], ChargebleTicket):
                                    print(ticket)
                                    temp.append(ticket)
                            
                            if temp == []:
                                c_flag = False
                                input("There is no Chargeable ticket to be charged. Press any key to continue ...")
                            else:
                                c_flag = False
                                try:
                                    charging = int(input('which card would you like to chrage? '))
                                    amount = int(input('How much you want to charge your card?\n1.20\n2.30\n3.40\n'))
                                    list_of_prices = [20, 30, 40]
                                    logged_in_person.make_withdraw(list_of_prices[amount - 1])
                                    logged_in_person.charge_chargeble_ticket(charging, list_of_prices[amount - 1])
                                    ticket_logger.info("%s successfully charged", type(ticket_obj).__name__)
                                    input("Chargeable ticket successfully charged")
                                except AssertionError :
                                    ticket_logger.error("Failure in charging ticket.")
                                    input("Failure in charging ticket.")
                                print(logged_in_person.ticket_list)
                                
                        else:
                            input('Invalid Input...')

                        if c_flag:
                            try:
                                logged_in_person.make_withdraw(55)
                                ticket_obj = eval(command)
                                logged_in_person.buy_ticket(ticket_obj)
                                print(logged_in_person.ticket_list[-1])
                                ticket_logger.info("%s successfully is bought", type(ticket_obj).__name__)
                                input("Buying ticket successfully")

                            except AssertionError:
                                    ticket_logger.error("Failure in buying ticket.")
                                    input("Failure in buying ticket. Please charge your wallet!")

                    elif login_user_input == '3':
                        save_user(logged_in_person)
                        break

            #admin
            elif user_input_menu == '3':
                clear()
                print('Select one of the below')
                show_menu(Menu.superuser_menu)
                admin_input = input('Choose: ')
                log_in_flag = False
                logged_in_admin = None

                # REGISTER
                if admin_input == '1':
                    clear()
                    name = input('Enter username: ')
                    password = input('Enter password: ')
                    admin_obj = SuperUser(name, password)
                    save_user(admin_obj)
                    user_logger.info(f'Super user Registered. Metro ID: {admin_obj.id}')
                    print(f'Super user Registered. Your Metro ID: {admin_obj.id}')
                    input('Done, Press any key to continue...')

                # LOGIN
                elif admin_input == '2':
                    clear()
                    admin_id = input('Enter Unique ID(Forgot password?(y)): ')
                    log_in_flag = False
                    logged_in_admin = None
                    if admin_id == 'y':
                        clear()
                        get_unique_id_from_username()
                    else:
                        try:
                            admin_obj = get_unique_id(admin_id)
                            logged_in_admin = admin_obj
                            log_in_flag = True
                            user_logger.info("super user logged in successfully!")
                            input("super user logged in successfully. Press any key to continue ...")
                        except FileNotFoundError:
                            user_logger.error("admin not found!")
                            input("User not found!, Press any key to continue ...")
                    
                    if log_in_flag:
                        try:
                            id = input("Whom do you want to put in blacklist? Enter the ID: ")
                            user_object = logged_in_admin.find_user(f'{id}.pickle', 'user/')

                            logged_in_admin.set_blacklist(user_object)
                            save_user(user_object)
                            user_logger.info("user was set in black list by admin")
                            input("user was set in black list by admin. Press any key to Logout ...")
                        except:
                            user_logger.error("Failure in adding user to blacklist")
                            input("Failure in adding user to blacklist. Press any key to Logout ...")

                        save_user(logged_in_admin)

            elif user_input_menu == '4':
                break


if __name__ == '__main__':
    Main.run()