import math

def distance_form(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def checkio(data):

    count = 1

    while count > 0:

        if len(data) == 1:
            return data

        count = 0

        # Sort black holes by merger priority
        sorted_list = []

        if len(data) > 1:
            for i in range(len(data)- 1):
                for j in range(i+1, len(data)):

                    distance_ij = distance_form(data[i][0], data[i][1], data[j][0], data[j][1])

                    if len(sorted_list) == 0:
                        sorted_list.insert(0, [i, j])
                        continue

                    for k in range(len(sorted_list)):

                        distance_k = distance_form(data[sorted_list[k][0]][0], data[sorted_list[k][0]][1],
                            data[sorted_list[k][1]][0], data[sorted_list[k][1]][1])

                        if distance_ij < distance_k:
                            sorted_list.insert(k, [i, j])
                            break
                        elif distance_ij == distance_k:
                            if min(i, j) < min(sorted_list[k][0], sorted_list[k][1]):
                                sorted_list.insert(k, [i, j])
                                break
                            elif min(i, j) > min(sorted_list[k][0], sorted_list[k][1]):
                                sorted_list.insert(k + 1, [i, j])
                                break
                            else:
                                if max(i, j) < max(sorted_list[k][0], sorted_list[k][1]):
                                    sorted_list.insert(k, [i, j])
                                    break
                                else:
                                    sorted_list.insert(k + 1, [i, j])
                                    break
                        elif (k+1) == len(sorted_list):
                            sorted_list.insert(k+1, [i, j])

        # Iterate through sorted_list, checking to see if merger criteria are met
        for i in range(len(sorted_list)):
            first_check = True
            second_check = True

            # Criteria 1: Check if intersection area >= 55% of the smallest holes area
            distance_i = distance_form(data[sorted_list[i][0]][0], data[sorted_list[i][0]][1],
                            data[sorted_list[i][1]][0], data[sorted_list[i][1]][1])

            if distance_i >= data[sorted_list[i][0]][2] + data[sorted_list[i][1]][2]:
                first_check = False
            elif distance_i == 0:
                first_check = True
            elif distance_i + min(data[sorted_list[i][0]][2], data[sorted_list[i][1]][2]) <= max(
                    data[sorted_list[i][0]][2], data[sorted_list[i][1]][2]):
                first_check = True
            else:
                # Intersection area from Eq (14) from http://mathworld.wolfram.com/Circle-CircleIntersection.html
                area1 = (data[sorted_list[i][0]][2] ** 2) * math.acos((distance_i ** 2 + data[sorted_list[i][0]][2] ** 2
                        - data[sorted_list[i][1]][2] ** 2) / (2 * distance_i * data[sorted_list[i][0]][2]))
                area2 = (data[sorted_list[i][1]][2] ** 2) * math.acos((distance_i ** 2 + data[sorted_list[i][1]][2] ** 2
                        - data[sorted_list[i][0]][2] ** 2) / (2 * distance_i * data[sorted_list[i][1]][2]))
                area3 = (1 / 2.0) * math.sqrt((-1 * distance_i + data[sorted_list[i][0]][2] + data[sorted_list[i][1]][2]) *
                        (distance_i + data[sorted_list[i][0]][2] - data[sorted_list[i][1]][2]) *
                        (distance_i - data[sorted_list[i][0]][2] + data[sorted_list[i][1]][2]) *
                        (distance_i + data[sorted_list[i][0]][2] + data[sorted_list[i][1]][2]))
                intersection_area = area1 + area2 - area3

                if intersection_area >= 0.55 * (math.pi * min(data[sorted_list[i][0]][2], data[sorted_list[i][1]][2]) ** 2):
                    first_check = True
                else: first_check = False

            # Criteria 2: Check if the area of one black hole is >= 20% more than the area of the other
            if (math.pi * max(data[sorted_list[i][0]][2], data[sorted_list[i][1]][2]) ** 2) >= 1.2 * (math.pi *
                min(data[sorted_list[i][0]][2], data[sorted_list[i][1]][2]) ** 2):
                second_check = True
            else: second_check = False

            # If both conditions are met, then begin merge process
            if first_check and second_check:
                if data[sorted_list[i][1]][2] > data[sorted_list[i][0]][2]:
                    new_radius = round(math.sqrt((math.pi * data[sorted_list[i][0]][2] ** 2) + (math.pi *
                                    data[sorted_list[i][1]][2] ** 2)) / math.sqrt(math.pi), 2)
                    # Increase larger black holes radius
                    data[sorted_list[i][1]] = (data[sorted_list[i][1]][0], data[sorted_list[i][1]][1], new_radius)
                    # Delete the black hole that was merged into the larger one
                    del data[sorted_list[i][0]]
                    count = count + 1
                    break

                elif data[sorted_list[i][1]][2] < data[sorted_list[i][0]][2]:
                    new_radius = round(math.sqrt((math.pi * data[sorted_list[i][0]][2] ** 2) + (math.pi *
                                    data[sorted_list[i][1]][2] ** 2)) / math.sqrt(math.pi), 2)
                    # Increase larger black holes radius
                    data[sorted_list[i][0]] = (data[sorted_list[i][0]][0], data[sorted_list[i][0]][1], new_radius)
                    # Delete the black hole that was merged into the larger one
                    del data[sorted_list[i][1]]
                    count = count + 1
                    break

    return data
