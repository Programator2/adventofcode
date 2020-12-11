with open('2.txt') as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.rstrip(), lines))
    for i, x in enumerate(lines):
        for k in range(i+1, len(lines)):
            n_diff = 0
            diff_loc = 0
            # k is index for second word
            for j in range(len(x)):
                # j j is index for a character
                if x[j] != lines[k][j]:
                    n_diff += 1
                    diff_loc = j
                    if n_diff > 1:
                        break
            if n_diff <= 1:
                print(x[:diff_loc] + x[diff_loc+1:])
                print(x)
                print(lines[k])
                print(f'different character at index {diff_loc}')
                break
