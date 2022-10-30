def main():
    username = get_username()
    password = get_password()
    authenticated = athenticate(user=username, password=password)
    if authenticated:
        print_timesheet(username)
        add_hours(username)
if __name__ == "__main__":
    main()