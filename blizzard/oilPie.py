from fractions import Fraction
​
def divide_pie(groups):
    drones = list(groups)
    total_drones = sum([abs(x) for x in drones])
    pie_size = Fraction(total_drones, total_drones)
    for group in drones:
        if group > 0:
            pie_size = Fraction(pie_size.numerator*total_drones - group*pie_size.denominator, pie_size.denominator*total_drones)
        else:
            pie_size = Fraction(pie_size.numerator*total_drones - pie_size.numerator*abs(group), pie_size.denominator*total_drones)
    return [pie_size.numerator, pie_size.denominator]
