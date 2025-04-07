from itertools import permutations
from time import sleep
import pwn


def main():
    r = pwn.remote("krzeworzech.tasks.2025.ctf.cs.msu.ru", 25069)
    for i in range(100):
        print(f"$ Итерация: {i}")
        sleep(0.1)
        print(r.recvline().decode().strip())
        print(r.recvline().decode().strip())
        symbols = dict()
        digits = 0
        for i in range(0, 10):
            r.sendline((str(i) * 4).encode())
            line = r.recvline().decode().strip()
            matched_digits = int(line.split()[3])
            if matched_digits:
                symbols.update({f"{i}": matched_digits})
                digits += matched_digits
            if digits == 4:
                break

        all_possible = [
            "".join(p)
            for p in permutations("".join([i[0] * i[1] for i in symbols.items()]))
        ]
        possible = all_possible.copy()
        for _ in range(1, 8):
            guess = possible[0]
            r.sendline(guess.encode())
            line = r.recvline().decode().strip()
            if "right" in line:
                print(line)
                print(guess)
                break
            matched_digits = int(line.split()[3])
            possible = [
                p
                for p in possible
                if sum(g == c for g, c in zip(guess, p)) == matched_digits
            ]
        if i == 99:
            print(r.recvline().decode().strip())
            print(r.recvline().decode().strip())
    print(r.recvall().decode().strip())

if __name__ == "__main__":
    main()
