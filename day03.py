import numpy as np

power = open('files\day03.txt', 'r').read().rstrip().split('\n')
clean_power = []
for p in power:
    clean_power.append(list([int(ch) for ch in p]))

clean_power = np.array(clean_power)

gamma_rate = []
epsilon_rate = []
for i in range(clean_power.shape[1]):
    counts = np.bincount(clean_power[:,i])
    gamma_rate.append(np.argmax(counts))
    epsilon_rate.append(np.argmin(counts))

gamma_rate = [str(int) for int in gamma_rate]
gamma_rate = "".join(gamma_rate)
gamma_rate = int(gamma_rate, 2)

epsilon_rate = [str(int) for int in epsilon_rate]
epsilon_rate = "".join(epsilon_rate)
epsilon_rate = int(epsilon_rate, 2)

print("Part 1: Gamma * Epsilon = {}".format(gamma_rate*epsilon_rate))

oxygen_rating = clean_power.copy()
i = 0
while len(oxygen_rating) != 1:
    counts = np.bincount(oxygen_rating[:,i])
    if counts[0] == counts[1]:
        bit_criteria = 1
    else:
        bit_criteria = np.argmax(counts)
    oxygen_rating = oxygen_rating[oxygen_rating[:,i]==bit_criteria]
    i+=1

co2_rating = clean_power.copy()
i = 0
while len(co2_rating) != 1:
    counts = np.bincount(co2_rating[:,i])
    if counts[0] == counts[1]:
        bit_criteria = 0
    else:
        bit_criteria = np.argmin(counts)
    co2_rating = co2_rating[co2_rating[:,i]==bit_criteria]
    i+=1

oxygen_rating = int("".join([str(int) for int in oxygen_rating[0]]),2)
co2_rating = int("".join([str(int) for int in co2_rating[0]]),2)
print("Part 2: O2 rating * CO2 rating = {}".format(oxygen_rating*co2_rating))
