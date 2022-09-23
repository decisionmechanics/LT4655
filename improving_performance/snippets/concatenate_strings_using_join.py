import time

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

start_time = time.perf_counter()

sentence = ""

for word in words:
    if sentence:
        sentence += " "

    sentence += word

print(f"Took {time.perf_counter() - start_time:.8f} seconds")

print(sentence)

# Better to...

start_time = time.perf_counter()

sentence = " ".join(words)

print(f"Took {time.perf_counter() - start_time:.8f} seconds")

print(sentence)
