from itertools import permutations

# Define the given parameters
A = ['a', 'b', 'c']
P = [0.05, 0.25, 0.7]
y = 'bbbccab'

# Define a function to compute the probability of a given key
def key_probability(key):
    probability = 1.0
    for i in range(len(A)):
        probability *= P[i] ** key.count(A[i])
    return probability

# Generate all possible keys
keys = list(permutations(A))

# Compute the probability of each key
key_probabilities = {}
for key in keys:
    key_probabilities[key] = key_probability(key)

# Find the most probable key
most_probable_key = max(key_probabilities, key=key_probabilities.get)

# Decrypt the message using the most probable key
decrypted_message = ''
for i in range(len(y)):
    index = A.index(y[i])
    decrypted_message += most_probable_key[index]

# Print the results
print("The most probable key is:", most_probable_key)
print("The decrypted message is:", decrypted_message)
print("The y message is        :", y)