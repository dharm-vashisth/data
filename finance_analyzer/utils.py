from tabulate import tabulate


def display_df(data_frame, style='psql'):
    print(tabulate(data_frame, headers='keys', tablefmt=style), end='\n\n')


def project_headline():
    print("Data Engineering by \033[1mDharm Vashisth\033[0m :)", end='\n\n')  # \033[1m starting of bold \033[0m is closing.
    print("Welcome to my first project!")


def print_bold_message(msg):
    print(f"\033[1m{msg}\033[0m")
