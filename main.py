

import pickle
import os


def displayMenu():
    print("1-Kayıtları Listele")
    print("2-Kayıt Ara")
    print("3-Kayıt Ekle")
    print("4-Kayıt Sil ")
    print("5-Kayıt Güncelle")
    print("6-Çıkış")


def menuLoop() -> str:
    while True:
        displayMenu()
        option = input("Yapmak istediginiz işlemi seçiniz (1-6): ")
        print("\n")
        if int(option) == 1 or int(option) == 2 or int(option) == 3 or int(option) == 4 or int(option) == 5 or int(option) == 6:
            break
        else:
            print("Lütfen 1 ile 6 arasinda bir sayi girin: ")
    return option


def mainLoop():
    while True:
        option = menuLoop()
        if int(option) == 1:
            listRecord()
        elif int(option) == 2:
            searchRecord()
        elif int(option) == 3:
            addRecord()
        elif int(option) == 4:
            deleteRecord()
        elif int(option) == 5:
            updateRecord()
        elif int(option) == 6:
            break


def listRecord() -> None:
    recordsList = ReadFile()
    print(f"Kayıt Sayısı : {len(recordsList)}\n")
    print(f"{'TC Kimlik No':^11}   {'İsim':^10}   {'Soyisim':^10}   {'Baba Adı':^10}   {'Anne Adı':^10}   {'Doğum Yeri':^10}   {'Medeni Durumu':^10}   {'Kan Grubu':^10}   {'Kütük Şehir':^10}   {'Kütük İlçe':^10}   {'İkametgah Şehir':^10}   {'İkametgah İlçe':^10}   ")
    for record in recordsList:
        print(f"{record.get('id', ' '):11.11}       {record.get('isim', ' '):10.10} {record.get('soyisim', ' '):10.10}   {record.get('babaadi', ' '):10.10}   {record.get('anneadi', ' '):10.10}  {record.get('dogumyeri', ' '):10.10}   {record.get('medenidurum', ' '):10.10}      {record.get('kangrubu', ' '):10.10}   {record.get('kutuksehir', ' '):10.10}    {record.get('kutukilce', ' '):10.10}   {record.get('ikametgahsehir', ' '):10.10}        {record.get('ikametgahilce', ' '):10.10}")
    print()


def searchRecord() -> None:
    print("Kayıt Arama")
    id = input("TC Kimlik NO:")
    recordsList = SearchRecordFromFile(id)
    for record in recordsList:
        print(f"{'İsim':^10}   {'Soyisim':^10}   {'Baba Adı':^10}   {'Anne Adı':^10}   {'Doğum Yeri':^10}   {'Medeni Durumu':^10}   {'Kan Grubu':^10}   {'Kütük Şehir':^10}   {'Kütük İlçe':^10}   {'İkametgah Şehir':^10}   {'İkametgah İlçe':^10}   ")
        print(f"   {record.get('isim', ' '):10.10} {record.get('soyisim', ' '):10.10}   {record.get('babaadi', ' '):10.10}   {record.get('anneadi', ' '):10.10}  {record.get('dogumyeri', ' '):10.10}   {record.get('medenidurum', ' '):10.10}      {record.get('kangrubu', ' '):10.10}   {record.get('kutuksehir', ' '):10.10}    {record.get('kutukilce', ' '):10.10}   {record.get('ikametgahsehir', ' '):10.10}        {record.get('ikametgahilce', ' '):10.10}")
    print("\n")


def addRecord():
    print("Kayıt Ekle: ")
    id = input("TC Kimlik NO: ")
    isim = input("İsim: ")
    soyisim = input("Soyisim: ")
    babaadi = input("Baba Adi: ")
    anneadi = input("Anne Adi: ")
    dogumyeri = input("Doğum Yeri: ")
    medenidurum = input("Medeni Durumu: ")
    kangrubu = input("Kan Grubu: ")
    kutuksehir = input("Kütük Şehir: ")
    kutukilce = input("Kütük İlçe: ")
    ikametgahsehir = input("İkametgah Şehir: ")
    ikametgahilce = input("İkametgah İlçe: ")
    addRecordToFile(id, isim, soyisim, babaadi, anneadi, dogumyeri, medenidurum, kangrubu, kutuksehir, kutukilce, ikametgahsehir, ikametgahilce)
    print("Kayıt Eklendi.\n")


def deleteRecord():
    print("Kayıt Silme")
    id = input("TC Kimlik NO:")
    recordsList=SearchRecordFromFile(id)
    for record in recordsList:
        print(f"{'İsim':^10}   {'Soyisim':^10}   {'Baba Adı':^10}   {'Anne Adı':^10}   {'Doğum Yeri':^10}   {'Medeni Durumu':^10}   {'Kan Grubu':^10}   {'Kütük Şehir':^10}   {'Kütük İlçe':^10}   {'İkametgah Şehir':^10}   {'İkametgah İlçe':^10}   ")
        print(f"   {record.get('isim', ' '):10.10} {record.get('soyisim', ' '):10.10}   {record.get('babaadi', ' '):10.10}   {record.get('anneadi', ' '):10.10}  {record.get('dogumyeri', ' '):10.10}   {record.get('medenidurum', ' '):10.10}      {record.get('kangrubu', ' '):10.10}   {record.get('kutuksehir', ' '):10.10}    {record.get('kutukilce', ' '):10.10}   {record.get('ikametgahsehir', ' '):10.10}        {record.get('ikametgahilce', ' '):10.10}")
    DeleteRecordsFromFile(recordsList)
    print("\n")
    print("Kayıt silindi.")
    print("\n")


def updateRecord():
    print("Kayıt Güncelleme")
    id = input("TC Kimlik NO:")
    recordsList = ReadFile()
    for record in recordsList:
        if record.get("id") == id:
            print(f"{'İsim':^10}   {'Soyisim':^10}   {'Baba Adı':^10}   {'Anne Adı':^10}   {'Doğum Yeri':^10}   {'Medeni Durumu':^10}   {'Kan Grubu':^10}   {'Kütük Şehir':^10}   {'Kütük İlçe':^10}   {'İkametgah Şehir':^10}   {'İkametgah İlçe':^10}   ")
            print(f"   {record.get('isim', ' '):10.10} {record.get('soyisim', ' '):10.10}   {record.get('babaadi', ' '):10.10}   {record.get('anneadi', ' '):10.10}  {record.get('dogumyeri', ' '):10.10}   {record.get('medenidurum', ' '):10.10}      {record.get('kangrubu', ' '):10.10}   {record.get('kutuksehir', ' '):10.10}    {record.get('kutukilce', ' '):10.10}   {record.get('ikametgahsehir', ' '):10.10}        {record.get('ikametgahilce', ' '):10.10}")
            secim=input("\nGüncellemek istediğiniz değeri yazınız(isim-soyisim-babaadi-anneadi-dogumyeri-medenidurum-kangrubu-kutuksehir-kutukilce-ikametgahsehir-ikametgahilce):")
            yenideger=input("Yeni {} giriniz:".format(secim))
            record[secim] = yenideger
            print("\n")
            print("Kayıt güncellendi.")
            print("\n")
    writeFile(recordsList)


def ReadFile() -> list:
    if os.path.isfile("data.bin"):
        with open("data.bin", "rb") as fileObject:
            recordsList = pickle.load(fileObject)
    else:
        recordsList = list()
    return recordsList


def writeFile(recordsListp: list):
    with open("data.bin", "wb") as fileObject:
        pickle.dump(recordsListp, fileObject)


def SearchRecordFromFile(idp: int) -> list:
    recordsList = ReadFile()
    responseList = list()
    for record in recordsList:
        if record.get("id") == idp:
            responseList.append(record)
    return responseList


def addRecordToFile(idp: int, isimp: str, soyisimp: str, babaadip: str, anneadip: str, dogumyerip: str,
                    medenidurump: str, kangrubup: str, kutuksehirp: str, kutukilcep: str, ikametgahsehirp: str,
                    ikametgahilcep: str):
    recordsList = ReadFile()
    recordDict = dict(id=idp, isim=isimp, soyisim=soyisimp, babaadi=babaadip, anneadi=anneadip, dogumyeri=dogumyerip,
                      medenidurum=medenidurump, kangrubu=kangrubup, kutuksehir=kutuksehirp, kutukilce=kutukilcep,
                      ikametgahsehir=ikametgahsehirp, ikametgahilce=ikametgahilcep)
    recordsList.append(recordDict)
    writeFile(recordsList)


def DeleteRecordsFromFile(recordListp : list) -> None:
    recordList= ReadFile()
    for record in recordList:
        for recordForDelete in recordListp:
            if record.get("id") == recordForDelete.get("id"):
                recordList.remove(recordForDelete)
                continue
    writeFile(recordList)


mainLoop()
