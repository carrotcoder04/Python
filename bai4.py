import matplotlib.pyplot as plt # type: ignore
words = input().split()
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
word_freq = dict(sorted(word_freq.items(),key = lambda item: item[1],reverse = True))
labels = list(word_freq.keys())
values = list(word_freq.values())
plt.figure(figsize=(10, 5))
plt.bar(labels,values, color = 'steelblue')
plt.title('110 most frequent tokens in description')
plt.ylabel('Frequency')
plt.yticks(range(0,max(values)+1))
plt.axhline(0, color='black', linewidth = 0.5, ls='--')
plt.show()