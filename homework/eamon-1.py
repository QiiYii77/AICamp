import numpy as np
import matplotlib.pyplot as plt


def draw_vectors_add(x, y):
    v1 = np.array(x)
    v2 = np.array(y)
    v3 = v1 + v2

    vector_to_draw = np.array([[0, 0, v1[0], v1[1]],
                               [v1[0], v1[1], v2[0], v2[1]],
                               [0, 0, v3[0], v3[1]]])
    X, Y, U, V = zip(*vector_to_draw)
    plt.figure()
    plt.ylabel('Y-axis')
    plt.xlabel('X-axis')
    ax = plt.gca()
    ax.quiver(X, Y, U, V, angles='xy', scale_units='xy',
              color=['r', 'b', 'g'], scale=1)
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    plt.draw()
    plt.title('Add two vectors', fontsize=10)
    plt.show()


def draw_angle_between_vectors(v1, v2):
    # Draw vectors
    array = np.array([[0, 0, v1[0], v1[1]],
                      [0, 0, v2[0], v2[1]]])
    X, Y, U, V = zip(*array)
    plt.figure()
    plt.ylabel('Y-axis')
    plt.xlabel('X-axis')
    ax = plt.gca()
    ax.quiver(X, Y, U, V, color=['r', 'b'],
              angles='xy', scale_units='xy', scale=1)
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    plt.draw()

    # Caculate angle
    unit_v1 = v1 / np.linalg.norm(v1)
    unit_v2 = v2 / np.linalg.norm(v2)
    dot_product = np.dot(unit_v1, unit_v2)
    angle = np.arccos(dot_product) / np.pi * 180
    plt.title('Angle between vectors is {:n} degrees'.format(
        angle), fontsize=10)

    plt.show()


draw_vectors_add([3, 4], [2, -3])
draw_angle_between_vectors([1, 0], [0, 2])
