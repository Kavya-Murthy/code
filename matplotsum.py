plt.figure()
plt.axis([0, 25, 25, 0])
curr = plt.gca()
for i in range(0, 5):
    for j in range(0, 5):
        if (i + j) % 2 == 0:
            curr.add_patch(plt.Rectangle((i * 5, j * 5), 5, 5, color="white"))
        else:
            curr.add_patch(plt.Rectangle((i * 5, j * 5), 5, 5, color="black"))
plt.show()