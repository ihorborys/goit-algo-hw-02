from queue import Queue
import random
import time


q = Queue()

def generate_request():
    request = random.randint(1, 10) # Cтворюємо випадкову нову заявку
    q.put(request)
    print(f"Нову заявку за послугою №{request} згенеровано: ")

def process_request():
    if len(q.queue) > 0:
        done_request = q.get(q.queue)
        print(f"Заявку № {done_request} оброблено: ")
    else:
        print("Черга заявок порожня")

try:
    while True:
        time.sleep(random.uniform(0.5, 1.5))
        if random.choice([False, True]):
            generate_request() # Викликаємо функцію для створення нових заявок
        time.sleep(random.uniform(0.5, 2.5))
        if random.choice([False, True]):
            process_request()# Викликаємо функцію для обробки заявок
except KeyboardInterrupt:
    print("Процес генерації/оброблення заявок перервано")