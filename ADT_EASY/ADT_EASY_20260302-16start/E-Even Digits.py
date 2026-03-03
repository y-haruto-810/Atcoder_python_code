n = int(input())
n_iti = (n-1) % 5 
n_ni = ((n-1) // 5) % 5
n_san = ((n-1) // 25) % 5
n_yon = ((n-1) // 125) % 5
n_go = ((n-1) // 625) % 5
n_roku = ((n-1) // 3125) % 5
n_nana = ((n-1) // (3125*5)) % 5
n_hati = ((n-1) // (3125*25)) % 5
n_kyuu = ((n-1) // (3125*125)) % 5
n_juu = ((n-1) // (3125*625)) % 5
n_juuiti = ((n-1) // (3125*3125)) % 5
n_juuni = ((n-1) // (3125*3125*5)) % 5
n_juusan = ((n-1) // (3125*3125*25)) % 5
n_juuyon = ((n-1) // (3125*3125*125)) % 5
n_juugo = ((n-1) // (3125*3125*625)) % 5
n_juuroku = (n-1) // (3125**3) % 5
n_juunana = (n-1) // ((3125**3)*5) % 5
n_juuhati = (n-1) // ((3125**3)*25) % 5

num = str(n_juuhati * 2) + str(n_juunana * 2) + str(n_juuroku * 2) + str(n_juugo * 2) + str(n_juuyon * 2) + str(n_juusan * 2) + \
    str(n_juuni * 2) + str(n_juuiti * 2) + str(n_juu * 2) + str(n_kyuu * 2) + str(n_hati * 2) + str(n_nana * 2) + \
    str(n_roku * 2) + str(n_go * 2) + str(n_yon * 2) + str(n_san * 2) + str(n_ni * 2) + str(n_iti * 2)

print(int(num))
