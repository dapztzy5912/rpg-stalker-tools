def start_game():
    print("\n🗡️ Selamat datang di Game RPG Terminal!")
    nama = input("Masukkan nama pahlawanmu: ")
    print(f"🔥 {nama}, petualanganmu dimulai!")

    hp = 100
    musuh_hp = 50
    while hp > 0 and musuh_hp > 0:
        aksi = input("Serang (s) atau Sembuh (h)? ")
        if aksi == "s":
            musuh_hp -= 20
            print(f"⚔️ Kamu menyerang! HP musuh: {musuh_hp}")
        elif aksi == "h":
            hp += 10
            print(f"💖 Kamu sembuh. HP kamu: {hp}")
        else:
            print("❌ Aksi tidak dikenal.")

        if musuh_hp > 0:
            hp -= 15
            print(f"💢 Musuh menyerang! HP kamu: {hp}")

    if hp <= 0:
        print("😵 Kamu kalah...")
    else:
        print("🏆 Kamu menang!")
