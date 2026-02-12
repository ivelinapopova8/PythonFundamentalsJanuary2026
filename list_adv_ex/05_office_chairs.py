room_counter = 1
rooms = int(input())
all_chairs = 0
all_visitors = 0
not_enough_chairs = False

for room in range(1, rooms + 1):
    chairs, visitor = input().split()
    visitors = int(visitor)
    all_chairs += len(chairs)
    all_visitors += visitors

    if visitors > len(chairs):
        not_enough_chairs = True
        print(f"{visitors - len(chairs)} more chairs needed in room {room}")

if not not_enough_chairs:
    print(f"Game On, {all_chairs-all_visitors} free chairs left")