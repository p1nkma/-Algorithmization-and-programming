#1: Максимальное число непересекающихся отрезков

def max_non_overlapping(segments):
    segments = sorted(segments, key=lambda x: x[1])

    count = 0
    last_end = None

    for left, right in segments:
        if last_end is None or left > last_end:
            count += 1
            last_end = right

    return count

#2: минимальное покрытие интервала [L, R]

def min_cover(segments, L, R):
    segments = sorted(segments, key=lambda x: x[0])

    pos = L
    count = 0
    i = 0

    while pos < R:
        best_right = None

        # Среди всех отрезков с left <= pos ищем максимальный right
        for left, right in segments:
            if best_right is None:
                best_right = right
            else:
                best_right = max(best_right, right)

        if best_right == None:
            return -1

        pos = best_right

    return count

# Задача 3: максимальная прибыль по заказам с дедлайнами

def max_profit(orders, m):
    # Сортируем по убыванию стоимости
    orders = sorted(orders, key=lambda x: -x[0])

    schedule = {}
    total = 0

    for cost, deadline in orders:
        for day in range(min(deadline, m), 0, -1):
            if day not in schedule:
                schedule[day] = cost
                total += cost
                break

    return total, schedule
