# Solution generated by ChatGPT
# https://chat.openai.com/chat

# Read the sequences from the file
with open('seq.dat', 'r') as f:
    sequences = f.readlines()

# Loop over the sequences
for i, seq in enumerate(sequences):
    # Split the sequence into a list of integers
    seq = [int(x) for x in seq.split()]

    # Check if the sequence is a Munodi sequence
    is_munodi = True
    length = 0
    for n in seq:
        length += 1
        if n == 1:
            # If the number is 1, the sequence terminates, so we can stop here
            break
        elif n % 2 == 0:
            # If the number is even, the next number should be n/2
            if seq[length] != n / 2:
                is_munodi = False
                break
        else:
            # If the number is odd, the next number should be 3*n+1
            if seq[length] != 3 * n + 1:
                is_munodi = False
                break

    # Print the result
    if is_munodi:
        print('Sequence {} is a Munodi sequence (length {})'.format(i + 1, length))
    else:
        print('Sequence {} is NOT a Munodi sequence'.format(i + 1))