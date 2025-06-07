import os
from game_rpg import rpg
from stalker import instagram, tiktok, steam

def menu():
    while True:
        print("\n=== Terminal Tools Menu ===")
        print("1. Main Game RPG")
        print("2. Stalk Instagram")
        print("3. Stalk TikTok")
        print("4. Stalk Steam")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            rpg.start_game()
        elif pilihan == "2":
            instagram.stalk_instagram()
        elif pilihan == "3":
            tiktok.stalk_tiktok()
        elif pilihan == "4":
            steam.stalk_steam()
        elif pilihan == "0":
            print("👋 Sampai jumpa!")
            break
        else:
            print("❌ Pilihan tidak valid.")

if __name__ == "__main__":
    menu()
