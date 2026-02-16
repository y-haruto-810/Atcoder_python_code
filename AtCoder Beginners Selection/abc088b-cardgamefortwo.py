n = int(input())
a_list = list(map(int, input().split()))
people = "alice"
alice_score = 0
bob_score = 0

while a_list != [] :
    if people == "alice" :
        max_num = max(a_list)
        alice_score += max(a_list)
        a_list.remove(max_num)
        if a_list == [] :
            print(alice_score - bob_score)
        people = "bob"
    elif people == "bob" :
        max_num = max(a_list)
        bob_score += max(a_list)
        a_list.remove(max_num)
        if a_list == [] :
            print(alice_score - bob_score)
        people = "alice"
