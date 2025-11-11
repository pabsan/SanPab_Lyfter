import csv

def game_feed():
    try:
        my_list = []
        num_games = int(input("Please enter the number of games: "))
        i = 1
        while (i <= num_games):
            #cosmetic menu
            print(f"============={i} of {num_games}==============")
            #User type the info
            name = input("Type the game name: ")
            gender = input("Type the game gender: ")
            developer = input("Type developer name: ")
            clasification = input("Type clasification ESRB: ")
            
            #save to the list
            my_list.append({"name":name, "gender":gender,"developer":developer,"clasification_esrb":clasification})
            i += 1
            #cosmetic menu
        print(f"========================================")
        return my_list
    except ValueError as e:
        print(f"Error on input data {e}")



def write_csv(path, data, headers):
    try:
        with open(path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file,headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"File has been saved in {[path]}")
    except FileNotFoundError as e:
        print(f"Error on finding the file {e}")

try:
    game_list = game_feed()
    write_csv('video_games.csv',game_list, game_list[0].keys())
except Exception as e:
    print(f"Error unexpected. {e}")