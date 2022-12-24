# Detect single-character XOR
#import from challenge 3 def crack_xor_cipher and ScoredGuess
#UNFINISHED

def crack_xor_cipher(ct: bytes) -> ScoredGuess: #from 3.py
    best_guess=ScoredGuess()
    ct_len=len(ct)
    ct_freqs = {b: ct.count(b) / ct_len for b in range(256)}

    for candidate_key in range(256):
        score:0
        for letter,frequency_expected in frequencies.items():
            score+=abs(frequency_expected - ct_freqs[ord(letter)^candidate_key])
        guess=ScoredGuess(socre,candidate_key)
        best_guess=min(best_guess,guess)
    
    if best_guess.key is None:
        exit("no key found")
        best_guess.ciphertext = ct
        best_guess.plaintext = bytes_xor(ct,bytes([best_guess.key]) * len(ct))
    
    return best_guess

if __name__=="__main__":
    with open("data/4.txt") as f:
        lines = [bytes.fromhex(line.strip()) for line in f]
    
    overall_best=ScoredGuess()
    for line in lines:
        print(end=".", flush=True)
        candidate = crack_xor_cipher(line)
        overall_best = min(overall_best, candidate)

    if overall_best.ciphertext is None:
          exit("no ciphertext found")
    
    print()
    print(f"{lines.index(overall_best.ciphertext)=}")
    print(f"{overall_best.key=}")
    print(f"{overall_best.plaintext=}")