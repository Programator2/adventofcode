import matplotlib.pyplot as plt


points = [
    [172, 154, 3, -4],
    [145, 157, 5, 2],
    [167, 153, 5, -5],
    [132, 154, 5, 4],
    [124, 148, 5, -1],
    [159, 150, -3, -4],
    [135, 149, 3, -5],
    [137, 157, 1, -4],
    [111, 153, 5, 4],
    [151, 151, -3, 4],
    [143, 157, -2, 2],
    [171, 157, 5, -5],
    [151, 154, 2, -2],
    [124, 157, -1, -5],
    [111, 157, -3, -4],
    [127, 152, 5, -3],
    [115, 152, -4, -5],
    [159, 148, -4, 5],
    [169, 152, 5, -4],
    [111, 154, -3, 3],
    [111, 148, -5, -1],
    [132, 150, -2, -3],
    [119, 156, 4, 1],
    [113, 152, -5, -3],
    [156, 148, 1, 5],
    [151, 150, -1, -3],
    [127, 157, -2, 5],
    [111, 151, 1, 5],
    [119, 154, 2, 1],
    [167, 152, 5, 3],
    [132, 155, -5, 2],
    [119, 148, 5, 2],
    [143, 149, 1, -4],
    [135, 155, -2, 3],
    [168, 157, -3, -4],
    [156, 157, -1, -4],
    [151, 151, -4, -5],
    [114, 148, -4, 5],
    [146, 157, -2, -3],
    [119, 154, 2, 5],
    [169, 157, 2, -3],
    [154, 150, 1, -1],
    [161, 157, -4, 5],
    [114, 148, 3, 5],
    [163, 157, 2, 3],
    [151, 152, 1, -5],
    [120, 152, 4, -5],
    [127, 151, -3, -1],
    [119, 149, 3, 4],
    [119, 152, 5, -3],
    [111, 152, -2, 2],
    [116, 148, 5, -4],
    [121, 151, -3, -1],
    [172, 151, -5, -4],
    [130, 153, -5, 5],
    [172, 155, -4, 5],
    [132, 151, -3, -1],
    [128, 149, -3, 1],
    [119, 155, -1, 2],
    [119, 154, 5, -1],
    [146, 157, 1, 2],
    [130, 153, -5, 4],
    [168, 148, -5, -2],
    [143, 153, 5, 4],
    [151, 156, -4, -5],
    [143, 152, -1, 3],
    [132, 156, 3, 1],
    [146, 157, 2, 2],
    [114, 152, -1, -5],
    [171, 152, -4, 4],
    [112, 157, -1, -5],
    [171, 148, 2, -3],
    [159, 151, -4, 3],
    [122, 150, 1, 3],
    [143, 154, 4, 3],
    [129, 153, -1, -5],
    [143, 154, -5, 1],
    [119, 156, 5, 2],
    [128, 153, 4, 3],
    [159, 155, 3, 5],
    [132, 154, 4, -5],
    [143, 151, -2, 5],
    [151, 148, 1, 1],
    [159, 157, -5, 5],
    [143, 155, -4, -3],
    [120, 152, -4, 1],
    [162, 157, 5, -1],
    [111, 150, -5, 2],
    [162, 157, -3, -2],
    [111, 151, 4, -1],
    [119, 157, -5, -2],
    [144, 157, -4, -5],
    [116, 157, -1, 2],
    [111, 155, 3, -2],
    [155, 149, 4, -5],
    [127, 153, -2, -4],
    [167, 150, 3, 2],
    [111, 154, -5, 3],
    [151, 155, -1, -3],
    [155, 149, -5, -2],
    [112, 157, -5, -5],
    [127, 155, 5, 2],
    [128, 153, 3, -3],
    [122, 155, -5, 3],
    [152, 153, -4, -1],
    [170, 148, 3, -2],
    [140, 157, -1, 5],
    [143, 148, -4, -4],
    [131, 149, 4, -2],
    [172, 153, -3, -1],
    [115, 157, 1, -4],
    [151, 155, 4, -2],
    [168, 152, -5, -2],
    [113, 157, 5, -4],
    [121, 151, 1, -1],
    [116, 148, -4, -3],
    [170, 148, 5, 5],
    [172, 150, -5, 5],
    [135, 149, -5, 3],
    [121, 154, 5, -3],
    [127, 155, -1, 3],
    [122, 150, 4, -4],
    [132, 157, 1, 3],
    [111, 155, 4, 1],
    [167, 152, -2, -2],
    [119, 148, -1, 1],
    [115, 157, -2, 2],
    [147, 157, -5, -4],
    [171, 157, -1, 4],
    [113, 148, -2, 2],
    [172, 149, 2, 2],
    [113, 152, 4, -1],
    [168, 152, -5, -5],
    [120, 153, 1, -4],
    [111, 149, -1, 2],
    [130, 148, -2, -5],
    [148, 157, 2, 2],
    [119, 152, -4, -1],
    [132, 155, -4, 3],
    [119, 153, -5, 2],
    [159, 151, -3, 1],
    [143, 149, -1, -1],
    [136, 157, -3, -5],
    [167, 154, 5, 3],
    [131, 153, -3, 3],
    [124, 157, 3, -2],
    [121, 154, -2, -4],
    [145, 157, 4, 1],
    [170, 152, -3, -4],
    [114, 157, -3, 2],
    [167, 151, -3, -2],
    [151, 149, 4, 1],
    [135, 157, -1, 1],
    [132, 153, 5, 1],
    [127, 156, -2, 2],
    [111, 154, -3, 5],
    [144, 157, 5, 3],
    [135, 154, 2, -4],
    [155, 149, 1, 5],
    [123, 149, -3, -4],
    [151, 151, 2, 5],
    [139, 157, -4, -5],
    [130, 148, -4, 2],
    [170, 157, 2, -4],
    [159, 156, -4, 2],
    [172, 155, 3, -5],
    [170, 152, 5, 5],
    [167, 156, -2, -3],
    [115, 148, -3, 1],
    [136, 157, 5, 4],
    [115, 152, 2, -1],
    [135, 150, -2, 1],
    [154, 155, 4, 3],
    [119, 151, -4, 3],
    [143, 156, -5, 5],
    [169, 148, -5, 3],
    [148, 157, 3, -3],
    [111, 151, -1, -5],
    [161, 157, 4, -5],
    [156, 157, 1, 2],
    [153, 154, -4, 5],
    [170, 148, 3, 5],
    [171, 148, 5, -1],
    [135, 151, 3, -4],
    [113, 157, -5, -4],
    [135, 148, -2, 2],
    [111, 156, -1, -3],
    [111, 155, -1, 4],
    [119, 150, 4, 3],
    [119, 151, 4, 5],
    [159, 153, -5, 3],
    [151, 155, 2, -4],
    [156, 157, 1, -1],
    [152, 152, 3, -3],
    [167, 156, -4, 2],
    [170, 152, -4, 3],
    [127, 150, -5, -3],
    [159, 148, -2, -2],
    [167, 155, 5, -4],
    [169, 152, 3, 4],
    [169, 148, -5, 5],
    [119, 157, -3, 2],
    [143, 151, -1, 2],
    [172, 156, 2, -3],
    [119, 149, 2, 5],
    [171, 157, 5, 3],
    [135, 152, 2, 4],
    [123, 156, -1, -5],
    [111, 156, 5, -4],
    [160, 157, 4, -2],
    [135, 156, 5, -3],
    [130, 153, 1, -3],
    [159, 149, -2, 2],
    [123, 149, -5, -4],
    [151, 153, 4, 5],
    [161, 157, -1, 2],
    [132, 157, 5, 2],
    [159, 154, 1, -4],
    [132, 150, -1, 2],
    [154, 155, 1, -5],
    [159, 150, -3, 2],
    [119, 153, -3, -3],
    [167, 157, -1, -3],
    [114, 148, 4, 2],
    [119, 153, 5, 3],
    [160, 157, 1, -1],
    [159, 156, -4, 1],
    [151, 153, 1, 5],
    [167, 149, 4, -1],
    [112, 152, -5, 2],
    [151, 149, 1, 2],
    [159, 152, 5, 2],
    [128, 149, -4, -3],
    [159, 150, 5, 4],
    [127, 155, 1, 4],
    [151, 153, 3, -5],
    [159, 151, -2, -5],
    [143, 153, 2, -1],
    [116, 148, -2, 4],
    [132, 152, -4, 4],
    [151, 157, 3, -5],
    [159, 154, -2, -1],
    [167, 153, 2, 1],
    [168, 148, -3, 1],
    [119, 148, -4, -4],
    [152, 152, -5, -5],
    [164, 157, 5, 3],
    [132, 155, 4, 5],
    [168, 148, -1, -5],
    [127, 154, -1, 2],
    [151, 149, -1, -2],
    [143, 150, -2, 5],
    [111, 148, 3, 5],
    [155, 156, -2, -2],
    [154, 155, -4, 5],
    [156, 148, -4, 1],
    [111, 148, -3, 3],
    [135, 151, -1, 3],
    [172, 153, 2, -1],
    [172, 149, -3, -4],
    [119, 152, -4, 4],
    [132, 150, 2, -5],
    [123, 149, 3, 3],
    [169, 152, -2, 2],
    [168, 152, -1, -1],
    [160, 157, -5, -4],
    [111, 152, 1, -3],
    [167, 151, 4, -5],
    [135, 153, -1, -1],
    [135, 156, -3, 1],
    [122, 150, -3, -2],
    [153, 151, -3, -2],
    [147, 157, 3, -4],
    [151, 154, 5, -2],
    [159, 154, -5, 5],
    [144, 157, -1, 4],
    [151, 157, -4, 5],
    [111, 149, 4, 1],
    [127, 151, -1, -2],
    [143, 156, 5, 3],
    [127, 152, 3, 5],
    [114, 152, -3, 3],
    [172, 155, 1, 3],
    [143, 149, 5, 4],
    [159, 153, 2, 4],
    [132, 156, 2, 1],
    [152, 153, -4, -5],
    [124, 157, 5, -3],
    [138, 157, -3, 2],
    [132, 156, -1, -3],
    [120, 152, -3, -1],
    [167, 153, -1, 5],
    [135, 151, 3, 2],
    [119, 150, 3, 2],
    [115, 148, 2, -4],
    [171, 152, 5, 2],
    [116, 157, -1, -2],
    [143, 153, -1, 2],
    [111, 152, 2, -2],
    [151, 156, -3, -1],
    [111, 157, -2, -2],
    [116, 157, -3, -3],
    [172, 150, -4, -3],
    [143, 151, -2, 1],
    [140, 157, 5, -4],
    [115, 148, 4, 1],
    [151, 150, -1, 3],
    [167, 148, -3, -1],
    [151, 150, 1, 4],
    [172, 151, 4, 3],
    [132, 153, 4, 2],
    [159, 148, 1, -4],
    [152, 152, 3, -1],
    [111, 150, 3, -1],
    [159, 152, 2, 1],
    [112, 148, -5, 4],
    [135, 153, 4, 4],
    [128, 153, -3, 5],
    [130, 148, 3, -5],
    [111, 149, 1, -1],
    [112, 157, 1, 4],
    [143, 156, 2, 2],
    [129, 148, 1, -1],
    [168, 157, -3, 5],
]

CLOCK = 10238

for p in points:
    # p[0] += CLOCK*p[2]
    # p[1] += CLOCK*p[3]
    plt.scatter(p[0], p[1])

plt.show()
