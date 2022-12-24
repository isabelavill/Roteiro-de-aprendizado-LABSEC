# Single-byte XOR cipher
#using frequency analysis, first we've got to know the frequencies of specifique characters(search online or do it manualy)
#UNFINISHED

frequencies=dict() #unfinished
def score_text(text:bytes) -> float:
    score=0.0
    l=len(text)
    for letter,frequency_expected in frequencies.items():
        frequency_actual = text.count(ord(letter)) / l
        err =  abs(frequency_expected - frequency_actual)
        score += err

    return score

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

    if __name__ == "__main__":
        ciphertext = bytes.fromhex("")
        best_guess=crack_xor_cipher(ciphertext)
        score,key,ciphertext,plaintext=astuple(best_guess)
        print(f"{key=}")
        print(f"{plaintext=}")