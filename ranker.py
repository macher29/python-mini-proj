def Ranker(List):
    for item in List:
        while True:
            try:
                response = input(f"{item}, good 'g' or bad 'b': ")

                if response == "g":
                    with open("good.txt", "a") as f:
                        f.write(f"{item}, ")
                    break
                
                elif response == "b":
                    with open("bad.txt", "a") as f:
                        f.write(f"{item}, ")
                    break

                else:
                    print("Type 'g' for good or 'b' for bad")

            except Exception as e:
                print(e)

List = list(input("Enter List: ").split(", "))
Ranker(List)