import numpy as np
import utils

if __name__ == '__main__':
    print("Підзавдання 1. Перетворити повороти у кватерніони qz, qy, qx:")
    qx = utils.quat_from_axis_angle([1, 0, 0], 20)
    qy = utils.quat_from_axis_angle([0, 1, 0], 90)
    qz = utils.quat_from_axis_angle([0, 0, 1], 50)
    print("qz:", qz)
    print("qy:", qy)
    print("qx:", qx)

    print("\nПідзавдання 2. Обчислити фінальний кватерніон q = qz * qy * qx:")
    q_total = utils.quat_multiply(utils.quat_multiply(qz, qy), qx)
    print(q_total)

    print("\nПідзавдання 3. Довести, що немає Gimbal Lock:")
    print("Матричне обертання при beta = 90 втрачає ступінь вільності (осі X та Z співпадають).")
    print("Однак, отриманий вище кватерніон зберігає унікальну 4-вимірну репрезентацію.")
    print("Ми можемо декомпозувати його назад у єдиний кут і вісь, доводячи відсутність 'замка':")
    axis, angle = utils.quat_to_axis_angle(q_total)
    print("Вісь:", axis)
    print("Кут:", angle)
