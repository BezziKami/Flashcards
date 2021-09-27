import json
import os


class Flashcards_deck:
    items = []

    def __init__(self, name):

        self.name = name

    def addFlashcard(self):

        front = input("text on front: ")
        back = input("text on back: ")
        self.items.append(Flashcard(front, back))
        self.dumpToFile()

    def handleOptions(self):

        working = 0
        choice = 0
        while not working:
            print(
                "1:add\n2:remove(todo)\n3:show all\n4:start learning\n5:exit\n6:dumptofile\n7:loadfromfile\n8:")
            choice = int(input())
            if choice == 1:
                self.addFlashcard()
            elif choice == 3:
                self.showAll()
            elif choice == 4:
                self.startLearning()
            elif choice == 5:
                working = 1
            elif choice == 6:
                self.dumpToFile()
            elif choice == 7:
                self.loadFromFile()

    def showAll(self):
        for x in self.items:
            print("FRONT: ", x.string_front, "BACK: ", x.string_back)

    def startLearning(self):
        for x in self.items:
            front = x.string_front
            back = x.string_back
            print(front)
            input()
            print(back)
            print("==================")

    def dumpToFile(self):
        tempDict = dict()
        for x in self.items:
            tmp = {x.string_front: x.string_back}
            tempDict.update(tmp)
        with open(os.path.join("E:", "Coding", "CodingProjects", "Flashcards", "Decks", "test.json"), 'w') as file:
            json.dump(tempDict, file)
            file.close()

    def loadFromFile(self):
        with open(r"E:\Coding\CodingProjects\Flashcards\Decks\test.json") as json_file:
            data = json.load(json_file)
        print(data)
        for key, value in data.items():
            self.items.append(Flashcard(key, value))


class Flashcard:

    def __init__(self, front, back):
        self.string_front = front
        self.string_back = back


def main():
    decks_of_flashcards = []
    deck_index_in_use = 0
    while 1:
        if len(decks_of_flashcards) != 0:
            print("deck currently in use: " +
                  decks_of_flashcards[deck_index_in_use - 1].name)
            decks_of_flashcards[deck_index_in_use - 1].handleOptions()
        print("what do you want to do?: ")
        option = int(input())

        if option == 1:  # adding new decks
            decks_of_flashcards.append(
                Flashcards_deck(input("what name of deck?:")))

        elif option == 2:  # printing all decks
            for x in decks_of_flashcards:
                print(x.name)

        elif option == 3:  # switching decks
            print("which deck should i switch to?: ")
            pointer = 1
            for x in decks_of_flashcards:
                print(str(pointer) + ": " + x.name)
                pointer += 1
            deck_index_in_use = int(input("Choice: "))


if __name__ == "__main__":

    main()
