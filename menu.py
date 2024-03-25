import subprocess


def execute_script(script_name):
    try:
        subprocess.run(f'bash {script_name}', shell=True, check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors if the script fails
        print(f'Error executing {script_name}: {e}')
        return


def logo():
    print("\033c")
    print("\033[1;35m")
    print("**********************************")
    print("*                ___  __   _   _ *")
    print("*               |    |  \ | \ / |*")
    print("*|\ /| o |\ | o |    |_ / |  V  |*")
    print("*|   | | | \| | |___ |    |     |*")
    print("*                                *")
    print("**********************************")
    print("\033[1;32m")
    print('Select Option')
    print("\n")


def menu():
    top_scripts = [
        ['start_minicom.sh', 'CP/M'],
        ['start_dosbox.sh', 'MS DOS'],
        ['start_apple.sh', 'Apple ProDOS'],
        ['start_linux', 'Debian Linux'],
        ['start_halt.sh', 'Quit']
    ]

    linux_scripts = [
        ['start_browser.sh', 'Web Browser (w3m)'],
        ['start_mail.sh', 'Email (mutt)'],
        ['start_rss.sh', 'News Reader (newsboat)'],
        ['start_weather.sh', 'Weather (wttr.in)'],
        ['start_addressbook.sh', 'Address Book (abook)'],
        ['start_emacs.sh', 'Editor (emacs)'],
        ['start_mc.sh', 'File Browser (mc)'],
        ['start_htop.sh', 'System Monitor (htop)'],
        ['start_ebooks', 'EBooks (epy)'],
        ['start_games', 'Games'],
        ['start_asciiquarium.sh', 'Aquarium (asciiquarium)'],
        ['start_shell.sh', 'Exit to shell']
    ]

    book_scripts = [
        ['read_beowolf.sh', 'Beowolf'],
        ['read_grimm.sh', 'Grimms Fairy Tales'],
        ['read_debianguide.sh', 'Debian Linux: Installation and Usage'],
        ['start_shell.sh', 'Exit to shell']
    ]

    game_scripts = [
        ['start_nethack.sh', 'Nethack'],
        ['start_nethack_online.sh', 'Nethack Online'],
        ['start_angband.sh', 'Angband'],
        ['start_adom.sh', 'Ancient Domains Of Mystery'],
        ['start_bastet.sh', 'Tetris'],
        ['start_ninvaders.sh', 'Space Invaders'],
        ['start_buggy.sh', 'Moon Buggy'],
        ['start_anchorhead.sh', 'Anchorhead'],
        ['start_mud.sh', 'MUDs'],
        ['start_shell.sh', 'Exit to shell']
    ]

    while True:
        logo()
        for i, script in enumerate(top_scripts):
            print(f'{i + 1}. {script[1]}')
        print("\n")
        choice = input('Enter number: ')

        top_script_index = int(choice) - 1
        if 0 <= top_script_index < len(top_scripts):
            script_name = top_scripts[top_script_index][0]

            if script_name == 'start_linux':
                logo()
                for i, script in enumerate(linux_scripts):
                    print(f'{i + 1}. {script[1]}')
                print("\n")
                choice = input('Enter number: ')

                linux_script_index = int(choice) - 1
                if 0 <= linux_script_index < len(linux_scripts):
                    script_name = linux_scripts[linux_script_index][0]

                    if script_name == 'start_ebooks' or script_name == 'start_games':
                        logo()
                        if script_name == 'start_ebooks':
                            for i, script in enumerate(book_scripts):
                                print(f'{i + 1}. {script[1]}')
                            print("\n")
                            choice = input('Enter number: ')

                            book_script_index = int(choice) - 1
                            if 0 <= book_script_index < len(book_scripts):
                                script_name = book_scripts[book_script_index][0]
                        if script_name == 'start_games':
                            for i, script in enumerate(game_scripts):
                                print(f'{i + 1}. {script[1]}')
                            print("\n")
                            choice = input('Enter number: ')

                            game_script_index = int(choice) - 1
                            if 0 <= game_script_index < len(game_scripts):
                                script_name = game_scripts[game_script_index][0]

        execute_script('./menu_scripts/' + script_name)
        if script_name == 'start_shell.sh':
            break


# Run the menu
menu()
