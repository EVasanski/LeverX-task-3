from concurrent.futures import ThreadPoolExecutor
from threading import Lock

a = 0
lock = Lock()


def function(arg):
    global a
    for _ in range(arg):
        with lock:
            a += 1


def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(5):
            executor.submit(function, 1000000)

    # threads = []
    # for i in range(5):
    #     thread = Thread(target=function, args=(1000000,))
    #     thread.start()
    #     threads.append(thread)
    #
    # [t.join() for t in threads]
    print("----------------------", a)  # ???


main()
