def random_array(length: int, lower: int, upper: int) -> list[int]:
    array = []
    for i in range(length):
        array.append(random.randint(lower, upper))
    return array
    
def shuffle_cards(length: int) -> list[int]:
    cards = [i for i in range(1, length+1)]

    for i in range(1, length):
        exchange = random.randint(i,length-1)
        temp = cards[i]
        cards[i] = cards[exchange]
        cards[exchange] = temp
        
    return cards
    
def make_array_int(length: int) -> list[int]:
    array = []
    for i in range(length):
        array.append(int(input("Item: ")))
    
    return array
        
def make_array_str(length: int) -> list[str]:
    array = []
    for i in range(length):
        array.append(input("Item: "))
    
    return array
        
      
def loading(num: int, t: float, symbol: str, word: str) -> None:
    print(word, end="")
    for i in range(num):
        print(symbol, end="")
        time.sleep(t)