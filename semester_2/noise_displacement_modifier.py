import random

def get_noise(x, y):

    noise_points = []

    xy = [-0, 0]

    for holdx in range(0, x):

        xy[1] = 0
        xy[0] += 1

        for holdy in range(0, y):

            xfinal = (xy[0]) + (random.randrange(-5, 5) / 10)
            yfinal = (xy[1]) + (random.randrange(-5, 5) / 10)

            noise_points.append(f"({xfinal}, {yfinal})")

    return_points = ','.join(noise_points)
    return return_points