import traceback, logging, sys, os, asyncio, random
from concurrent import futures
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import math
from datetime import datetime
import platform
import sys
import asyncio
import time
import threading
import traceback
import tqdm
import time
from time import sleep
from tqdm import tqdm
from multiprocessing import Pool
import subprocess

# import keyboard
# import pynput
# from pynput import keyboard

import IPCHECKER as IPx
from IPCHECKER import *
from subprocess import call

import threading
import ctypes
import time

## class thread with exception
class thread_with_exception(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):

        # target function of the thread class
        try:
            while True:
                print('running ' + self.name)
        finally:
            print('ended')

    def get_id(self):

        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')


# t1 = thread_with_exception('Thread 1')
# t1.start()
# time.sleep(2)
# t1.raise_exception()
# t1.join()
#


class Colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"

    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"

    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"

    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"


def display_header2():
    print(
        '\t\t \033 The program calculates prime #s using Threading, Hyperthreading (if available), Multi-Threading & Multi-Processsing.\033 \n'
        '\t\t Too High of a range will result in CPU hangup / over-utilization'
        '\t\t \033[1;34;40m Bright Blu Stay off Drugs Kidz, mmkay? \033[1;34;40m \033[0m 1;34;40m]'
        '\t\t: '), print(), print('\t\t\t', )
    print(f"{'X' * 50}".center(width))
    print('X' * 150)
    print('X' * 150)
    print(f"{'X' * 50}".center(width))
    print(), print()

    print(' :: Testing Order:: '.center(width))
    print(' :: ITERATOR - WITH THREADING - SINGLE CORE:: '.center(width))
    print(' :: ITERATOR - NO THREADING - SINGLE CORE :: '.center(width))
    print(' :: ITERATOR - ASYNCIO (EVENT LOOPING) :: '.center(width))
    print(' :: ITERATOR - MULTI THREADING  :: '.center(width))
    print(' :: ITERATOR - MULTI THREADING w/out Daemon  :: '.center(width))


def display_header3():
    print(
        '\t\t \033 The program calculates prime #s using Threading, Hyperthreading (if available), Multi-Threading & Multi-Processsing.\033 \n'
        '\t\t Too High of a range will result in CPU hangup / over-utilization'
        '\t\t \033[1;34;40m Bright Blu Stay off Drugs Kidz, mmkay? \033[1;34;40m \033[0m 1;34;40m]'
        '\t\t: '), print(), print('\t\t\t', )
    print(f"{'X' * 50}".center(width))
    print('X' * 150)
    print('X' * 150)
    print(f"{'X' * 50}".center(width))
    print(), print()

    print(' :: Testing Order:: '.center(width))
    print(' :: PRIME ITERATOR - WITH THREADING - SINGLE CORE:: '.center(width))
    print(' :: CONCURRENT THREAD POOL EXECUTOR - PRIME TEST  :: '.center(width))
    print(' :: PRIME ITERATOR - ASYNCIO (EVENT LOOPING) :: '.center(width))
    print(' :: PRIME ITERATOR - (Difficult) MULTI THREADING w/out Daemon  :: '.center(width))
    print(' :: PRIME ITERATOR - MULTI Processing w/out Daemon  :: '.center(width))
    print(' :: PRIME ITERATOR - NO THREADING - SINGLE CORE :: '.center(width))
    print('X' * 50)


class LIST_FUNC():
    def __init__(self, delay=None):
        is_prime0 = self.is_prime0

    # CLASS_RANGE = self.CLASS_RANGE

    @staticmethod
    def iter_list(PRIMES_TEST_LIST):
        PRIME_TEST_LEN = len(PRIMES_TEST_LIST)

        for iter00 in tqdm(PRIMES_TEST_LIST):  ######ADD  TQ
            # print( iter00 #, sep = "\t")
            print(iter00, end="")
            if (iter00 + 1) == PRIME_TEST_LEN:
                print('X' * 50)
                end00 = time.time()
                end_time00 = end00 - start00
                print(f'Thread Count: [{yellow}{threading.active_count()}{reset}')
                print(f'End time for Iter List Test , with  [{yellow}{threading.active_count()}{reset}] Active Threads')
                print(end_time00)
                break

    def is_prime0(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        sqrt_n = int(math.floor(math.sqrt(n)))
        for i in tqdm(range(3, sqrt_n + 1, 10000)):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def check_freq(FREQ_ITER):

        def check_sleep(amount):
            with Spinner():
                freq_count = 0
                # print(f'\033[0;35m; [{amount}].. Gettting to Work [{amount}]\033[0;35;m'.center(width))
                start = datetime.now()
                time.sleep(amount)
                end = datetime.now()
                delta = end - start
                return delta.seconds + delta.microseconds / 1000000

        print(f'{bblue}Calculating UNIX-CLOCK and Thread Clock Variance{reset}')
        print(f'{bblue}This is a test will return the the response time from daemon to executed thread{reset}')
        print(
            f'\033[1;34;40m If the program wheel freezes, then youve overloaded your system... \n {yellow} {time.ctime(current_t)} {reset}   \t\t')

        print()
        print('X' * 100)
        print(f'** Sleep Timer.. [{check_sleep}')

        start00 = time.time()
        start_time00 = time.ctime(start00)
        print(f'Calculation Start Time: , {yellow} **[{start_time00}]** {reset} '.center(width))
        error = sum(abs(check_sleep(0.050) - 0.050) for i in tqdm(FREQ_ITER, bar_format="{percentage:3.0f}%"))
        end00 = time.time()

        end_time00 = end00 - start00
        ctyme = round(end_time00, 4)
        cry_time00 = time.ctime(end_time00)
        print(f'\t\t Captured date-time: {cry_time}')
        print('X' * 50)
        print('X' * 50)
        print(
            f'\n{bblue}The Average Clock Variance, from UNIX-CLOCK and CPU threads Thread: (Average is 16ms){reset} \n Average Error is {red} [%{error}] {reset}')
        print(f'The Test Range : {yellow} [{PRIMES_TEST_RANGE}] {reset}')
        print(f'Task  completed in: {yellow} [{ctyme}] Seconds {reset}')
        print(f'Task  completed at: {yellow}[{cry_time00}]{reset}')
        print(f' CPU Latency In MS: (16ms is considered average) \n Average Error is {red} [%{error}] {reset}')


def display_header():
    # print('*' * 75)

    color_red = Colors()
    global red0
    red0 = color_red.fgRed
    global reset0
    reset0 = color_red.reset

    x = 'x'
    print(f"{'X' * 125:^70}")
    print(f"{'X' * 125:^70}")
    pretty = f'{red0}xxx PRIME-NUMBER-SHREDDER xxx{reset0}'
    print(f'{pretty : ^70}')
    print(f"{'X' * 125: ^70}")

    one = (
        f'[USAGE] - [1] This is a python program that takes a list of download links, and saves each file to the programs download directory.')
    two = (
        f'[USAGE] - [2] The program works well with most download repositories, and currently gets around security measure implimented by \n[USAGE] - [2]b 1337x.to, itorrent && archive.org')
    three = (
        f'[USAGE] - [3] Download a LINK GRABBING extension from chrome, to pull the URLs off of the browsers tabs.')
    four = (f'[USAGE] - [4] Save the list into download_list.txt (Found in the Directory as this program')
    five = (
        f'[USAGE] - [5] Wait for downloads. Archive.org may be slow. The program saves both a LIST and DICT for further usage. (see functions)')
    six = (f'[SYSTEM] copyright material from Adel Al-Aali [SYSTEM]')

    print(f"{one:^70}")
    print(f"{two:^70}")
    print(f"{three:^70}")
    print(f"{four:^70}")
    print(f"{five:^70}")
    print(f"{six:^70}")
    print(f"{x * 20: ^70}")
    print(), print()


class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1:
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False


def clear():
    # check and make call for specific operating system
    os_name = platform.system()
    _ = call('clear' if os_name == 'Linux' or 'Windows' or 'Darwin' else 'cls')


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", threading])
    subprocess.check_call([sys.executable, "-m", "pip", "install", tqdm])
    subprocess.check_call([sys.executable, "-m", "pip", "install", datetime])


def hash_pattern():
    print(), print(), print()
    time.sleep(.5)
    print(" ### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
          "#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
          "#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
          "                ##                  ##              ##                  ##                ")
    time.sleep(1)
    print("#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
          "#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### #### ",
          " #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### #### ", print('...?'),
          )
    time.sleep(.5)
    print(" ### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
          "#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
          "#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
          "                ##                  ##              ##                  ##                ")
    time.sleep(1)
    print("#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
          "#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### #### ",
          " #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### #### ", print('...?'),
          )
    time.sleep(.5)
    print(" ### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
          "#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
          " #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
          "                ##                  ##              ##                  ##              ##  ",
          " #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
          "#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### #### ",
          " #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### #### "
          )
    time.sleep(.1)
    print(), print(), print()


#######################################################################################################################DDD
#######################################################################################################################DDD
#######################################################################################################################DDD
#######################################################################################################################DDD


width = os.get_terminal_size().columns  # set the width to center goods
width_len = width
TICKER = 0

try:
    print(IPx.IP)
    # print(f'\033[0;35;47m \t\t[{IPx.get_ip()}]  ...? \033[0m 0;35;47m')
    width = os.get_terminal_size().columns  # set the width to center goods
    terminal = os.environ.get('TERM')
    width_len = width
    cwd = os.getcwd()
    IP = f"\033[1;35;0m {IPx.IP}"
    current_version = platform.release()
    system_info = platform.platform()
    os_name0 = platform.system()
    
    # new adds 
    big_names = platform.uname()
    processor = platform.processor()
    architecture = platform.architecture()
    user_id = os.uname()
    login = os.getlogin()
    os.access(cwd)
    clear()

    display_header()
    print()
    display_header2()
    print()
    print('X' * 150)
    print('X' * 150)
    print()
    print(f'SYSTEM INFO'.center(width))
    print(f'\033[1;35;m [{current_version}]  ...? '.center(width))
    print(f'\033[1;35;m [{os_name0}] + [{terminal}] ...? '.center(width))
    print(f'\033[1;35;m [{system_info}]  ...? '.center(width))
    print(f'\033[1;35;0m [{big_names}]  ...? '.center(width))  ### ADDD YOUR IP
    print(f'\033[1;35;0m [{processor}]  ...? '.center(width))  ### ADDD YOUR IP
    print(f'\033[1;35;0m [{architecture}]  ...? '.center(width))  ### 
    print(f'\033[1;35;0m [{user_id}]  ...? '.center(width))  ### 
    print(f'\033[1;35;0m [{login}]  ...? '.center(width))  ### 
    print(f'\033[1;35;0m [{current_version}]  ...? '.center(width))  ### ADDD YOUR IP


    
    
    
    
    print('X' * 150)
    print('X' * 150)

    print()

    print(f"{'X' * 50}".center(width))
    print(f"{'X' * 50}".center(width))

    time.sleep(7)
except OSError as ose:
    print(str(ose))
except Exception as E:
    traceback.print_exc()
    print(str(E))

clear()

###########
color = Colors()
functions = LIST_FUNC()
spinner = Spinner()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset
############
print(f'{yellow}Enter Prime Test Range: {reset} \n')
PRIMES_TEST_RANGE_INPUT = input()
print('X' * 25)
print(f'{yellow} Enter the amount of iterations to test CPU FREQ (under 200 is suffeciant:{reset}')
FREQ_ITER = input()
PRIMES_TEST_INT = int(float(PRIMES_TEST_RANGE_INPUT))
global PRIMES_TEST_RANGE
PRIMES_TEST_RANGE = range(PRIMES_TEST_INT)
PRIME_TEST_LEN = len(PRIMES_TEST_RANGE)
PRIMES_TEST_LIST = list(PRIMES_TEST_RANGE)

clear()

try:
    with Spinner():
        print(f"{'X' * 100}")
        print()
        current_t = time.time()
        print("\033[0m")
        print(), print()

        print(f"{'X' * 25}".center(width))

        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))

        print('Initiating Boat'.center(width))
        print(f"{'X' * 25}.".center(width))
        print(f'Recursion Length: , [{PRIMES_TEST_RANGE}]'.center(width))
        print(f'Current Iteration Depth: , {PRIME_TEST_LEN}'.center(width))

        time.sleep(1.5)
        start = time.time()
        start00 = time.time()
        cry_time = time.ctime(start)

        with Spinner():
            print(f'\t\t You entered:: {PRIMES_TEST_RANGE}'), print(), print()
            print(f'[{[TICKER]}][## STARTING CPU VARIANCE CALCULATION ##[{[TICKER]}]\t\t'.center(width))
            print("f{'X' * 50}".center(width)), print()
            print(f"{'X' * 20}".center(width))
            functions.check_freq(PRIMES_TEST_RANGE)
            print(f'\033[0m[{[TICKER]}][## ENDING CPU VARIANCE CALCULATION ##[{[TICKER]}]\t\t'.center(width))
            time.sleep(8)
            clear()


except Exception as e:
    print(str(e))


def _foo(my_number):
    square = my_number * my_number
    time.sleep(1)
    return square


period_list = ['..........']
period_list *= 100
len_period_list = len(period_list)
for x, y in enumerate(period_list):
    print(f'{x}')
print(), print()
print(len_period_list)
print(period_list)

# x = lambda clear: call('clear' if os_name == 'Linux' or 'Windows' or 'Darwin' else 'cls')
# threading_prime = functions.is_prime0(PRIMES_TEST_LIST)

hash_pattern()
clear()
display_header()
display_header2()

try:
    with Spinner():

        print(), print()
        print('X' * 50)

        start04 = time.time()
        start05 = time.ctime(start04)

        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        print(f' :: Starting Test on {bblue} Single -NON-THREADED- ITERATION Range Iterator{reset} :: '.center(width))
        print(f'starting: {yellow}[{start05}]{reset}'.center(width))
        print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        time.sleep(12), print(), print()

        functions.iter_list(PRIMES_TEST_LIST)
        if functions.iter_list:

            end_sec = time.time()
            end_t = time.ctime(end_sec)
            end_d = end_sec - start04

            print(), print()
            print('X' * 50)
            print(f'The Test Range : {bblue}[{PRIMES_TEST_RANGE}{bblue}]')
            print(f'Task  completed in: {yellow}[{end_d}{reset}]')
            print(f'Task  completed at: {yellow}[{end_t}{reset}]')
            print(f'Time To Complete Task {red}[{end_d}] Seconds {reset}')
            print('X' * 50)
            print('X' * 50), print(), print()
            TICKER += 1
            time.sleep(7)
        #  sys.exit()
        else:
            print('Moving on to Next Iteration')
            time.sleep(1)
            pass

        print(f' :: Starting Test on {bblue} Range Iterator {reset} :: '.center(width))
        print(
            f'{cyan}[{TICKER}]{reset} :: Single Threaded Processing with daemon on :: {cyan}[{TICKER}] {reset} '.center(
                width))
        print(f'{bblue}This is Single-Processing, and effeciant will depend on the Test Algo.{reset}'.center(width))
        print(f"{'X' * 50}".center(width))

        current_tim = time.time()
        current_time00 = time.ctime(current_tim)
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        print(f'Single Threaded ITERATION starting:'.center(width))
        print(f'{yellow}[{current_time00}]{reset}'.center(width))
        print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
        time.sleep(5)
        clear()

        START = time.time()
        t = threading.Thread(name='first_thread', target=functions.iter_list, args=(PRIMES_TEST_RANGE,))
        current_time = time.ctime(START)
        print(f'Current_Time: {yellow} {current_time} {reset}')
        t.start()
        if t:
            print(f"{'X' * 50}".center(width))
            print(f"{'X' * 50}".center(width))

            print('f :: Check to see if thread is alive:: ')
            print(f"d.isAlive(), {t.is_alive()}")
            end91 = time.time()
            current_time91 = time.ctime(end91)
            end_time91 = end91 - START

            print(f'{bblue}SINGLE THREADED Iteration Test Results: {bblue}'.center(width))
            print(f'Thread Count: [{red}{threading.active_count()}{reset}]')
            print(f'The Test Range : {bblue}[{PRIMES_TEST_RANGE}{bblue}]')
            print(f'Task  completed in: {yellow}[{end_time91} Seconds{reset}]')
            print(f'Task  completed at: {yellow}[{current_time91}{reset}]')
            print(f'Time To Complete Task {red}[{end_time91}]{reset}')
            print('X' * 50)
            print('X' * 50), print(), print()
            print()
            print(f'Checking For Alive Threads'.center(width))
            t.terminate()
            #   executor.shutdown()
            print(f"d.isAlive(),{red} {t.is_alive()}{reset}")
            print('Moving on to iteration test, with single thread')
            TICKER += 1
            time.sleep(7)
            clear()
            print(), print()
        else:
            pass

except Exception as f:
    traceback.print_exc()
    print(str(f))

    ############################ ########## ########## #### ############################ ########## ########## ####
# ############################ ########## ########## ####  ############################ ########## ########## ####
############################ ########## ########## #### ############################ ########## ########## ####
# ############################ ########## ########## ####  ############################ ########## ########## ####
############################ ########## ########## #### ############################ ########## ########## ####
# ############################ ########## ########## ####  ############################ ########## ########## ####
############################ ########## ########## #### ############################ ########## ########## ####
# ############################ ########## ########## ####  ############################ ########## ########## ####


print(
    r"################# START OF MULTI THREAD #################   ################# START OF MULTI THREAD #################",
    r"################# START OF MULTI THREAD #################   ################# START OF MULTI THREAD #################",
    r"################# START OF MULTI THREAD #################   ################# START OF MULTI THREAD #################",
    r"################# START OF MULTI THREAD #################   ################# START OF MULTI THREAD #################",
    r"################# START OF MULTI THREAD #################   ################# START OF MULTI THREAD #################",
    r"################# START OF MULTI THREAD #################   ################# START OF MULTI THREAD #################",
    r"################# START OF MULTI THREAD #################   ################# START OF MULTI THREAD #################",
    r"################# START OF MULTI THREAD #################   ################# START OF MULTI THREAD #################",
    r"################# START OF MULTI THREAD #################   ################# START OF MULTI THREAD #################",
    r"################# START OF MULTI THREAD #################   ################# START OF MULTI THREAD #################",
    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
    print(f"".center(width))
)
print(
    f'{blue}This is Multi-Threading,{red}Asyncio{reset} and effeciant will depend on the Test Algo.{reset}'.center(
        width))

display_header()
display_header3()
print(f' :: Starting Test on {bblue}ASYNC ITERATION Range Iterator{reset} :: '.center(width))
time.sleep(8)
clear()

try:
    with Spinner():  ## start sequence ##
        current_time01 = time.time()
        current_time02 = time.ctime(current_time01)
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        print(f' :: Starting Test on {bblue}ASYNC ITERATION Range Iterator{reset} :: '.center(width))
        print(
            f'{blue}This is Multi-Threading,{red}Asyncio{reset} and effeciant will depend on the Test Algo.{reset}'.center(
                width))
        print(f'starting: {yellow}[{current_time01}]{reset}'.center(width))
        print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        time.sleep(5), print(), print()

        start01 = time.time()
        for list00 in tqdm(PRIMES_TEST_RANGE):
            async def fetch_data02(PRIMES_TEST_RANGE):
                task = asyncio.create_task(read_data(PRIMES_TEST_RANGE))
                await task
                await asyncio.sleep(.00000001)


            async def read_data(PRIMES_TEST_RANGE):
                print(PRIMES_TEST_RANGE)
                await asyncio.sleep(.00000001)


            print(list00)

        print(), print()
        print('X' * 50)
        print('X' * 50)
        print()

        ############ End Sequence ##
        end33 = time.time()
        cry_time33 = time.ctime(end33)
        end_time33 = end33 - start01
        print(f'{bblue}Async Iteration Test Results: {bblue}'.center(width))

        print(f'The Test Range : {bblue}[{PRIMES_TEST_RANGE}{bblue}]')
        print(f'Task  completed in: {yellow}[{end_time33}{reset}]')
        print(f'Task  completed at: {yellow}[{cry_time33}{reset}]')
        print(f'Time To Complete {yellow} Asyncio Task {yellow} {red}[{end_time33}]{reset}')
        print('X' * 50)
        print('X' * 50)
        print()

        TICKER += 1
        time.sleep(7)
except Exception as f:
    traceback.print_exc()
    print(str(f))

############## ################ ############## ############################## ################
############## ################ ############## ############################## ################
############## ################ ############## ############################## ################
############## ################ ############## ############################## ################
############## ################ ############## ############################## ################

###### TESTING VARIOUS WAYS TO IMPLIMENT THREADPOOL EXECUTOR ###
###### TESTING VARIOUS WAYS TO IMPLIMENT THREADPOOL EXECUTOR ###
###### TESTING VARIOUS WAYS TO IMPLIMENT THREADPOOL EXECUTOR ###
###### TESTING VARIOUS WAYS TO IMPLIMENT THREADPOOL EXECUTOR ###
###### TESTING VARIOUS WAYS TO IMPLIMENT THREADPOOL EXECUTOR ###


display_header()
display_header2()
print(f' :: Starting Test on {bblue}Multi-Threaded ITERATION Range Iterator{reset} :: '.center(width))
time.sleep(7)
clear()

try:
    current_time77 = time.time()
    current_time78 = time.ctime(current_time77)

    print(f"{'X' * 50}".center(width))
    print(f"{'X' * 50}".center(width))
    print(f' :: Starting Test on {bblue}Multi-Threaded ITERATION Range Iterator{reset} :: '.center(width))
    print(
        f' Multi-Threading,{red}NOT USING ThreadPoolExecutor to handle time-slicing. {reset} \n  {bblue}Effeciancy will depend on the Test Algo.{reset}'.center(
            width))
    print(f'starting: {yellow}[{current_time77}]{reset}'.center(width))
    print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
    print(f"{'X' * 50}".center(width))
    print(f"{'X' * 50}".center(width))
    time.sleep(5), print(), print()

    ############# Multi Threading
    # format = "%(asctime)s: %(message)s"
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                        )


    def read_data():
        time.sleep(1)
        for i in PRIMES_TEST_RANGE:
            logging.debug('Starting')
            print(f'Process Reviewing {i}')
            time.sleep(.000000001)
            logging.debug('Exiting')


    def action():
        for i in PRIMES_TEST_RANGE:
            logging.debug('Starting')
            print(f'Reading Data {i}')
            time.sleep(.000000001)
            logging.debug('Exiting')


    # if __name__ == '__main__':
    t = threading.Thread(name='Thread_2', target=read_data)
    w = threading.Thread(name='Thread_3', target=action)
    w2 = threading.Thread(target=read_data)

    t.start()
    w.start()
    w2.start()

    t.join()
    print(f"d.isAlive(), {t.is_alive()}")
    w.join()
    print(f"w.isAlive(), {w.is_alive()}")
    w2.join()

    ## End Sequence ##
    ###########################################
    print(), print()
    print('X' * 50)
    print('X' * 50)
    print()
    end77 = time.time()
    cry_time01 = time.ctime(end77)
    end_time00 = end77 - current_time77
    print(f'{bblue}Multi-Threaded Iteration Test Results: {bblue}'.center(width))
    print(f'The Test Range : {yellow}[{PRIMES_TEST_RANGE}{reset}]')
    print(f'Thread Count: [{yellow}{threading.active_count()}{reset}')
    print(f'Task  completed in: {yellow}[{end_time00}{reset}]')
    print(f'Task  completed at: {yellow}[{cry_time01}{reset}]')
    print(f'Thread Count: [{red}{threading.active_count()}{reset}]')
    print(f'Time To Complete Task {red}[{end_time00}]{reset}')
    print('X' * 50)
    print('X' * 50)
    print(' :: Killing Threads:: ')
    print(f'Checking For Alive Threads'.center(width))
    # executor.shutdown()
    t.terminate()
    w.terminate()
    w2.terminate()
    print(f"d.isAlive(), {t.is_alive()}")
    print(f"d.isAlive(), {w.is_alive()}")
    print(f"d.isAlive(), {w2.is_alive()}")
    print('X' * 50)
    print('X' * 50)

    TICKER += 1
    time.sleep(7)
    clear()

except Exception as f:
    traceback.print_exc()
    print(str(f))

# except Exception as f:
#     traceback.print_exc()
#     print(str(f))

#############################################################################################################################################
##################################  ##################################  ##################################  ##################################
#############################################################################################################################################

#############################################################################################################################################
##################################  ##################################  ##################################  ##################################
#############################################################################################################################################

## Threading w/ daemon on


display_header()
display_header2()
print(f'{cyan} Starting Sequence on Multi Threaded Proceeses to Test Iterations.. {reset}'.center(width))
print(f'{cyan} -- DAEMON ON -- {reset}'.center(width))
time.sleep(5)
clear()
try:
    ## start sequence
    current_time44 = time.time()
    current_time45 = time.ctime(current_time44)
    print(f"{'X' * 50}".center(width))
    print(f"{'X' * 50}".center(width))
    print(
        f' :: Starting Test on {bblue}Multi-Threaded ITERATION Range Iterator{reset} {red} DAEMON ON {reset}:: '.center(
            width))
    print(
        f' Multi-Threading,{red}NOT USING ThreadPoolExecutor to handle time-slicing. {reset} \n  {bblue}Effeciancy will depend on the Test Algo.{reset}'.center(
            width))
    print(f'starting: {yellow}[{current_time45}]{reset}'.center(width))
    print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
    print(f"{'X' * 50}".center(width))
    print(f"{'X' * 50}".center(width))
    time.sleep(5), print(), print()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")


    def daemon():
        for i2 in PRIMES_TEST_RANGE:
            logging.info("Thread %s: starting")
            time.sleep(.00001)
            logging.info("Thread %s: finishing")


    def non_daemon():
        for i2 in PRIMES_TEST_RANGE:
            logging.info("Thread %s: starting")
            logging.info("Thread %s: finishing")


    d0 = threading.Thread(name='daemon00', target=daemon)
    d0.daemon = True
    t0 = threading.Thread(name='non-daemon00', target=non_daemon)
    d0.start()
    t0.start()
    d0.join()
    print(f"d0.isAlive(), {d0.is_alive()}")
    t0.join()
    print(f"t0.isAlive(), {t0.is_alive()}")

    print(), print()
    print('X' * 50)
    print('X' * 50)
    print()
    end44 = time.time()
    cry_time44 = time.ctime(end44)
    end_time44 = end44 - current_time44

    ### end sequence ###
    print(), print()
    print('X' * 50)
    print('X' * 50)
    print()
    end44 = time.time()
    cry_time44 = time.ctime(end44)
    end_time44 = end44 - current_time44
    print(f'{bblue}Multi-Threaded Iteration Test Results: {bblue}'.center(width))
    print(f'The Test Range : {yellow}[{PRIMES_TEST_RANGE}{reset}]')
    print(f'Thread Count: [{yellow}{threading.active_count()}{reset}')
    print(f'Task  completed in: {yellow}[{end_time44}{reset}]')
    print(f'Task  completed at: {yellow}[{cry_time44}{reset}]')
    print(f'Thread Count: [{red}{threading.active_count()}{reset}]')
    print(f'Time To Complete Task {red}[{end_time44}]{reset} Seconds')
    print('X' * 50)
    print('X' * 50)
    print()
    print(' :: Killing Threads:: ')
    print(f'Checking For Alive Threads'.center(width))
   # executor.shutdown()
    print(f"d.isAlive(), {d0.is_alive()}")
    print(f"d.isAlive(), {t0.is_alive()}")
    print('X' * 50)
    print('X' * 50)
    print(f'{bblue} Moving on to next iteration {reset}'.center(width))

    time.sleep(7)
    clear()

# print(f"d.isAlive() {w2.is_alive()}")
except Exception as fx:
    traceback.print_exc()
    print(str(fx))

display_header()
display_header2()
print(), print()

current_time98 = time.time()
current_time99 = time.ctime(current_time98)
print(f"{'X' * 50}".center(width))
print(f"{'X' * 50}".center(width))

print(f' :: Starting Test on {bblue}THREAD-POOL multi-threaded ITERATION Range Iterator{reset} :: '.center(width))
print(
    f'{blue}This is Multi-Threading,{red}Multi-Threaded, with ThreadPoolExecutor{reset} and effeciant will depend on the Test Algo.{reset}'.center(
        width))
print(f'starting: {yellow}[{current_time98}]{reset}'.center(width))
print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
print(f"{'X' * 50}".center(width))
print(f"{'X' * 50}".center(width))
time.sleep(5), print(), print()

try:
    ## start of sequence
    threads = list()

    current_time65 = time.time()
    current_time66 = time.ctime(current_time65)
    print(f"{'X' * 50}".center(width))
    print(f"{'X' * 50}".center(width))
    print(
        f' :: Starting Test on {bblue}Multi-Threaded ITERATION Range Iterator{reset} {red} DAEMON ON {reset}:: '.center(
            width))
    print(
        f' Multi-Threading,{red}NOT USING ThreadPoolExecutor to handle time-slicing. {reset} \n  {bblue}Effeciancy will depend on the Test Algo.{reset}'.center(
            width))
    print(f'starting: {yellow}[{current_time65}]{reset}'.center(width))
    print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
    print(f"{'X' * 50}".center(width))
    print(f"{'X' * 50}".center(width))
    time.sleep(5), print(), print()


    def worker():
        for index in PRIMES_TEST_RANGE:
            logging.info("Main    : create and start thread %d.", index)
            x = threading.Thread(target=slave, args=(index,))
            threads.append(x)
            x.start()


    def slave():
        for index, thread in enumerate(threads):
            logging.info("Main    : before joining thread %d.", index)
            thread.join()
            logging.info("Main    : thread %d done", index)


    if __name__ == '__main__':
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            executor.map(worker, PRIMES_TEST_RANGE)

        print('X' * 50)
        print('X' * 50)

        ### end sequence ###

        print(), print()
        print('X' * 50)
        print('X' * 50)
        print()
        end65 = time.time()
        cry_time65 = time.ctime(end65)
        end_time65 = end65 - current_time65
        print(f'{bblue}Multi-Threaded Iteration With Thread Pool Results: {bblue}'.center(width))
        print(f'The Test Range : {yellow}[{PRIMES_TEST_RANGE}{reset}]')
        print(f'Thread Count: [{yellow}{threading.active_count()}{reset}')
        print(f'Task  completed in: {yellow}[{end_time65}{reset}]')
        print(f'Task  completed at: {yellow}[{cry_time65}{reset}]')
        print(f'Thread Count: [{red}{threading.active_count()}{reset}]')
        print(f'Time To Complete Task {red}[{end_time65}]{reset} Seconds')
        print('X' * 50)
        print('X' * 50)
        print()
        print(' :: Killing Threads:: ')
        print(f'Checking For Alive Threads'.center(width))
        print(f"x.isAlive(), {x.is_alive()}")
       # print(f"d.isAlive(), {t0.is_alive()}")
        print('X' * 50)
        print('X' * 50)
        print(f'{bblue} Moving on to next iteration {reset}'.center(width))

        time.sleep(7)
        clear()

except Exception as f:
    traceback.print_exc()
    print(str(f))

    ##################### START OF GITHUB CHANGES ################################
    ##############################################################################

display_header()
display_header2()
print(), print()

current_time98 = time.time()
current_time99 = time.ctime(current_time98)
print(f"{'X' * 50}".center(width))
print(f"{'X' * 50}".center(width))

print(f' :: Starting Test on {bblue}THREAD-POOL multi-threaded ITERATION Range Iterator{reset} :: '.center(width))
print(
    f'{blue}This is Multi-Threading,{red}Multi-Threaded, with ThreadPoolExecutor{reset} and effeciant will depend on the Test Algo.{reset}'.center(
        width))
print(f'starting: {yellow}[{current_time98}]{reset}'.center(width))
print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
print(f"{'X' * 50}".center(width))
print(f"{'X' * 50}".center(width))
time.sleep(5), print(), print()


#### Another way to do thread pooling #####

## start of sequence

def randomNum_gen():
    start = .1  # inclusive
    end = .8  # exclusive
    n = 8  # size -- coorleate to 8 max cores, could double tthe time if 4 cores.
    # rand_int = random.uniform(range(start, end), k=n)
    rand_int = random.random()
    rand_float = rand_int / 10
    print(rand_float)

    return rand_float


def threading_function():
    print(f'Sleeping for {rand_float} Seconds.')
    time.sleep(rand_float)
    return f'Done Sleeping {rand_float}'


try:
    with Spinner():
        threads = list()
        current_time44 = time.time()
        current_time65 = time.ctime(current_time44)
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        print(
            f' :: Starting Test on {bblue}Multi-Threaded ITERATION Range Iterator{reset} {red} DAEMON ON {reset}:: '.center(
                width))
        print(
            f' Multi-Threading,{red}NOT USING ThreadPoolExecutor to handle time-slicing. {reset} \n  {bblue}Effeciancy will depend on the Test Algo.{reset}'.center(
                width))
        print(f'starting: {yellow}[{current_time44}]{reset}'.center(width))
        print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        time.sleep(5)
        # print()

        ##Body #####
        # random - create random foat gen for

        ## Tread pool with executor.submit
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            rand_sec = randomNum_gen()
            # results = [executor.submit(threading_function, rand_sec) for x in PRIMES_TEST_RANGE]
            # for f in concurrent.futures.as_completed(results):
            #     print(f"xxx{x} ## xxxx {f.results()}".center(width))

            for x in PRIMES_TEST_RANGE:
                rand_sec = randomNum_gen()
                results = [executor.submit(threading_function, rand_sec)]

                for future in futures.as_completed(results):
                    print(future)

            ## thread pool with executor.map (mapping the thread to function)
            ## map returns the order in which thread was run
            # with concurrent.futures.ThreadPoolExecutor() as executor:
            #     rand_sec = randomNum_gen()
            #     results = executor.map(threading_function, rand_sec)
            #     for result in results:
            #         print(result)
            #

            #  Manual Threading / Reading theads
            #  f1 = executor.submit(threading_function, rand_sec) ## -< future object (to receive single thread. delete later.)
            #    print(f1.results())
            #    print(f2.resutls())
            #  f2 = executor.submit(threading_function, rand_sec) #
            #  print (f1.result())
            #  print (f2.result())

            ## end of sequence
            #########

            print(), print()
            print('X' * 50)
            print('X' * 50)
            print()
            end45 = time.time()
            cry_time45 = time.ctime(end45)
            end_time45 = end45 - current_time44
            print(f'{bblue}Multi-Threaded Iteration With Thread Pool Results: {bblue}'.center(width))
            print(f'The Test Range : {yellow}[{PRIMES_TEST_RANGE}{reset}]')
            print(f'Thread Count: [{yellow}{threading.active_count()}{reset}')
            print(f'Task  completed in: {yellow}[{end_time45}{reset}]')
            print(f'Task  completed at: {yellow}[{cry_time45}{reset}]')
            print(f'Thread Count: [{red}{threading.active_count()}{reset}]')
            print(f'Time To Complete Task {red}[{end_time45}]{reset} Seconds')
            print('X' * 50)
            print('X' * 50)
            print()
            print(' :: Killing Threads:: ')
            print(f'Checking For Alive Threads'.center(width))
            executor.shutdown()
            print(f"d.isAlive(), {d0.is_alive()}")
            print(f"d.isAlive(), {t0.is_alive()}")
            print('X' * 50)
            print('X' * 50)
            print(f'{bblue} Moving on to next iteration {reset}'.center(width))

            time.sleep(7)
            clear()


except Exception as f:
    traceback.print_exc()
    print(str(f))


def randomNum_genIII():
    start = 1  # inclusive
    end = 8  # exclusive
    n = 8  # size -- coorleate to 8 max cores, could double tthe time if 4 cores.
    rand_int = random.random()
    rand_float = rand_int / 10  # see line 1072
    print(rand_float)

    return rand_float


def threading_functionIII(rand_float):
    print(f'Sleeping for {rand_float} Seconds.')
    time.sleep(seconds)
    return f'Done Sleeping {rand_float}'


try:
    with Spinner():
        current_time20 = time.time()
        current_time21 = time.ctime(current_time20)
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        print(
            f' :: Starting Test on {bblue}Multi-Threaded ITERATION Range Iterator{reset} {red} DAEMON ON {reset}:: '.center(
                width))
        print(
            f' Multi-Threading,{red}NOT USING ThreadPoolExecutor to handle time-slicing. {reset} \n  {bblue}Effeciancy will depend on the Test Algo.{reset}'.center(
                width))
        print(f'starting: {yellow}[{current_time21}]{reset}'.center(width))
        print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        time.sleep(5)
        # print()

        print(f' :: Starting Multi-Processing Module :: '.center(width))
        print('####################### start of multi pool processing ################')
        with concurrent.futures.ProcessPoolExecutor() as executor:
            ## the submit submits the execute function. it is best used for submitting just one thread
            for x in PRIMES_TEST_RANGE:
                rand_floatIII = randomNum_genIII()
                f1 = executor.submit(threading_functionIII, rand_floatIII)
                print(f1.result)

            # for y in concurrent.futures.as_completed(f1):
            #     print(y.result())

            # print(f1.results)

            ## end of sequence
            #########

            print(), print()
            print('X' * 50)
            print('X' * 50)
            print()
            end20 = time.time()
            cry_time20 = time.ctime(end20)
            end_time21 = end20 - current_time20
            print(f'{bblue}Multi-Threaded Iteration With Thread Pool Results: {bblue}'.center(width))
            print(f'The Test Range : {yellow}[{PRIMES_TEST_RANGE}{reset}]')
            print(f'Thread Count: [{yellow}{threading.active_count()}{reset}')
            print(f'Task  completed in: {yellow}[{end_time21}{reset}]')
            print(f'Task  completed at: {yellow}[{cry_time20}{reset}]')
            print(f'Thread Count: [{red}{threading.active_count()}{reset}]')
            print(f'Time To Complete Task {red}[{end_time21}]{reset} Seconds')
            print('X' * 50)
            print('X' * 50)
            print()
            print(' :: Killing Threads:: ')
            print(f'Checking For Alive Threads'.center(width))
            executor.shutdown()
            print(f"d.isAlive(), {d0.is_alive()}")
            print(f"d.isAlive(), {t0.is_alive()}")
            print('X' * 50)
            print('X' * 50)
            print(f'{bblue} Moving on to next iteration {reset}'.center(width))

            time.sleep(7)
            clear()
except Exception as f:
    traceback.print_exc()
    print(str(f))

#
#
# try:
#     with futures.Process.Pools.Executor() as executor:
#
# except exception as E:


#
# with ThreadPoolExecutor(max_workers=1) as executor:
#     future = executor.submit(pow, 323, 1235)
#     print(future.result())
#
#


#    with Pool(2) as p:
#       r = list(tqdm.tqdm(p.imap(functions.iter_list, PRIMES_TEST_RANGE), total=PRIME_TEST_LEN))
# for i in tqdm(range(PRIMES_TEST_RANGE)):
#     sleep(3), print(i)
#     print(r)
#


##########################################
##########################################
##########################################
hash_pattern()
display_header()
display_header2()
print(), print()
time.sleep(3)
try:
    with Spinner():
        print(f'[{[TICKER]}][## STARTING CPU VARIANCE CALCULATION ##[{[TICKER]}]\t\t'.center(width))
        print("f{'X' * 50}".center(width))

        print('Calculating UNIX-CLOCK and Thread Clock Variance')
        print('This is a test will return the the response time from daemon to executed thread')
        print(f'Gettting to Work'.center(width))
        time.sleep(.1)
        print(f'\t\t You entered:: {PRIMES_TEST_RANGE}')
        print(f"{'X' * 20}".center(width))
        time.sleep(.5)

        start00 = time.time()
        start_time00 = time.ctime(start00)
        print('Calculation Start Time: ', start_time00)

        error = sum(abs(check_sleep(0.050) - 0.050) for i in tqdm(PRIMES_TEST_RANGE))
        end00 = time.time()
        end_time00 = end00 - start00
        cry_time00 = time.ctime(end_time00)
        print(f'[{[TICKER]}][## ENDING CPU VARIANCE CALCULATION ##[{[TICKER]}]\t\t'.center(width))
        print(f'\t\t Captured date-time: {cry_time}')

        print('X' * 50)
        print('X' * 50)

        print(
            f'\nThe Average Clock Variance, from UNIX-CLOCK and CPU threads Thread: (Average is 16ms) \n Average Error is [%{error}]')
        print(f'The Test Range : [{PRIMES_TEST_RANGE}]')
        print(f'Task  completed in: [{end_time00}]')
        print(f'Task  completed at: [{cry_time00}]')
        print('X' * 50)
        print('X' * 50)

        TICKER += 1
        time.sleep(4)

except Exception as f:
    traceback.print_exc()
    print(str(f))

try:
    with Spinner():

        print(f"{bblue}Prime_# Test will return the prime #'s specified from user's input{reset}".center(width))
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        print(
            f' :: Starting Test on {bblue} :: (aSyncIO) Synchronous threading, maxing out a single clock :: {reset} :: '.center(
                width))
        print(
            f'{blue}This is Multi-Threading,{red}Asyncio{reset} and effeciancy will depend on the Test Algo.{reset}'.center(
                width))
        print(f' :: Starting: {yellow}[{current_time01}]{reset}'.center(width))
        print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        print('X' * 50)
        time.sleep(5)
        print(), print()

        time.sleep(1)
        start02 = time.time()


        async def fetch_data():
            print('start fetching ')
            task00 = asyncio.create_task(another_thread())
            value00 = await task00
            #  print(value00)
            await asyncio.sleep(.000000000000000001)
            print('done fetching')

            return {'Data ': 1}


        async def another_thread():
            print('antoher fucking thread')
            print('X' * 50)
            await asyncio.sleep(.00000000000000000001)


        async def print_numbers():
            for i in tqdm(PRIMES_TEST_RANGE):
                print(i)
                await asyncio.sleep(0.00000000000000000001)


        async def main00():  ## creating tasks // futures -- a place holder for a value that will exist in the future.
            print('EVENT LOOP SEQUENCE (ASYNCIO)  ')

            task01 = asyncio.create_task(fetch_data())
            task02 = asyncio.create_task(print_numbers())
            value01 = await task01
            print(value01)

            await task02


        asyncio.run(main00())
        end02 = time.time()
        end_time02 = end02 - start02
        print('thread inside of a thread:: (SHOULD BE THE SLOWEST) ')
        print(end_time02)
        time.sleep(3)
        print(), print(), print()

        print('startin sequence 3: ')
        start03 = time.time()


        async def main01():
            print('adel')
            # await foo('text') ## makes async func wait for foo func to execute.
            task = asyncio.create_task(foo('text'))
            await task
            await asyncio.sleep(
                .000001)  ## we are pausing the execution to function, and then run the asncio task above
            print('finished')


        async def foo(text):
            for fast in tqdm(PRIMES_TEST_RANGE):
                print(fast)
            await asyncio.sleep(.000001)


        asyncio.run(main01())

        print('Just as single thread, no hyperthreading! ')
        end03 = time.time()
        end_time03 = end03 - start03
        print(end_time03)
        time.sleep(3)
        print(), print(), print()

        print(), print(), print()


        def print_to_stderr(*a):
            print(*a, file=sys.stderr)
            print_to_stderr("Hello World")


        def print_to_stdout(*a):
            print(*a, file=sys.stdout)


        print_to_stdout("Hello World")

        ##
        totaltotal = time.time()
        total_end = start - totaltotal
        print(f'{red}END OF SEQUENCE{reset}'.center(width))
        print(total_end)


except Exception as f:
    traceback.print_exc()
    print(str(f))

hash_pattern()

print(
    r"################# START OF PRIME_# TEST  #################   ################# START OF PRIME # TEST #################",
    r"################# START OF PRIME_# TEST  #################   ################# START OF PRIME # TEST #################",
    r"################# START OF PRIME_# TEST  #################   ################# START OF PRIME # TEST #################",
    r"################# START OF PRIME_# TEST  #################   ################# START OF PRIME # TEST #################",
    r"################# START OF PRIME_# TEST  #################   ################# START OF PRIME # TEST #################",
    r"################# START OF PRIME_# TEST  #################   ################# START OF PRIME # TEST #################",
    r"################# START OF PRIME_# TEST  #################   ################# START OF PRIME # TEST #################",
    r"################# START OF PRIME_# TEST  #################   ################# START OF PRIME # TEST #################",
    r"################# START OF PRIME_# TEST  #################   ################# START OF PRIME # TEST #################",
    r"################# START OF PRIME_# TEST  #################   ################# START OF PRIME # TEST #################",
    r"################# START OF PRIME_# TEST  #################   ################# START OF PRIME # TEST #################",
    r"################# START OF PRIME_# TEST  #################   ################# START OF PRIME # TEST #################",
    r"################# START OF PRIME_# TEST  #################   ################# START OF PRIME # TEST #################",
    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
    print(f"".center(width))
)
# display_header()
display_header2()
print(f'{bblue} This is the start of the prime # test {reset}'.center(width))
time.sleep(5)


#
#
# #### PRIME #S START

def is_primeIII(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, PRIMES_TEST_INT):
        if n % i == 0:
            return False
    return True


def check_sleep(amount):
    with Spinner():
        freq_count = 0
        # print(f'\033[0;35m; [{amount}].. Gettting to Work [{amount}]\033[0;35;m'.center(width))
        start = datetime.now()
        time.sleep(amount)
        end = datetime.now()
        delta = end - start
        return delta.seconds + delta.microseconds / 1000000


PRIMES = PRIMES_TEST_RANGE
try:
    with Spinner():
        print(
            f'[{[TICKER]}][## STARTING \033 ANOTHER \033 CPU VARIANCE CALCULATION ##[{[TICKER]}]\t\t'.center(width))
        print("f{'X' * 50}".center(width))

        print(), print()

        print(f"{'X' * 50}".center(width))
        print('Calculating UNIX-CLOCK and Thread Clock Variance')
        print('This is a test will return the the response time from daemon to executed thread')
        print(f'Gettting to Work'.center(width))
        time.sleep(.1)
        print(f'\t\t You entered:: {PRIMES_TEST_RANGE}')
        print(f"{'X' * 20}".center(width))
        time.sleep(.5)

        start00 = time.time()
        start_time00 = time.ctime(start00)
        print('Calculation Start Time: ', start_time00)
        error = sum(abs(check_sleep(0.050) - 0.050) for i in PRIMES_TEST_RANGE)
        end00 = time.time()
        end_time00 = end00 - start00
        cry_time00 = time.ctime(end_time00)
        print(f'[{[TICKER]}][## ENDING CPU VARIANCE CALCULATION ##[{[TICKER]}]\t\t'.center(width))
        print(f'\t\t Captured date-time: {cry_time}')

        print('X' * 50)
        print('X' * 50)

        print(
            f'\nThe Average Clock Variance, from UNIX-CLOCK and CPU threads Thread: (Average is 16ms) \n Average Error is [%{error}]')
        print(f'The Test Range : [{PRIMES_TEST_RANGE}]')
        print(f'Task  completed in: [{end_time00}]')
        print(f'Task  completed at: [{cry_time00}]')
        print('X' * 50)
        print('X' * 50)

        TICKER += 1
        time.sleep(4)

except Exception as f:
    traceback.print_exc()
    print(str(f))

    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####


def randomNum_genIIII():
    pass


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in tqdm(zip(PRIMES_TEST_LIST, executor.map(is_primeIII,
                                                                     PRIMES_TEST_LIST))):  # zip the list into a tuple, and map to function
            print('%d is prime: %s' % (number, prime))

    # if __name__ == '__main__':
    #      main()


# main()

def prime_threading():
    print(f'Sleeping for {rand_float} Seconds.')
    time.sleep(seconds)
    return f'Done Sleeping {rand_float}'


try:  ## CONCURRENT THREAD POOL EXECUTOR - PRIME TEST  ##
    with Spinner():
        start000 = time.time()
        threads = list()

        current_time000 = time.ctime(start000)
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        print(
            f' :: Starting Test on {bblue}## CONCURRENT THREAD POOL EXECUTOR - PRIME TEST  ## r{reset} {red} DAEMON ON {reset}:: '.center(
                width))
        print(
            f' Multi-Threading,{red}NOT USING ThreadPoolExecutor to handle time-slicing. {reset} \n  {bblue}Effeciancy will depend on the Test Algo.{reset}'.center(
                width))
        print(f'starting: {yellow}[{current_time000}]{reset}'.center(width))
        print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        time.sleep(5)
        # print()

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            rand_secIIII = randomNum_gen()
            for i, d in zip(PRIMES_TEST_RANGE, map(is_primeIII, PRIMES_TEST_RANGE)):
                results = executor.submit(prime_threading, rand_secIIII)
                print('%d is prime: %s' % (i, d))  ## may have to chagne %d and %s

        print('X' * 50)
        print(type(t))
        print(f'Thread Count: {threading.active_count()} ')

        print(), print()
        end00 = time.time()
        end_time00 = end00 - start00
        print(f'End time for multi/single threaded process, with [{threading.active_count()}] Active Threads')
        print(end_time000)
        TICKER += 1
        time.sleep(3)
        id00 = threading.get_ident()
        print('[TRHEAD ID]** ', id00)

        # id00 = threading.get_ident()
        # print('[TRHEAD ID]** ', id00)

        print(), print()
        print('X' * 50)
        print('X' * 50)
        print()
        end000 = time.time()
        cry_time001 = time.ctime(end000)
        end_time21 = end000 - start000
        print(f'{bblue}Multi-Threaded Iteration With Thread Pool Results: {bblue}'.center(width))
        print(f'The Test Range : {yellow}[{PRIMES_TEST_RANGE}{reset}]')
        print(f'Thread Count: [{yellow}{threading.active_count()}{reset}')
        print(f'Task  completed in: {yellow}[{end_time21}{reset}]')
        print(f'Task  completed at: {yellow}[{cry_time20}{reset}]')
        print(f'Thread Count: [{red}{threading.active_count()}{reset}]')
        print(f'Time To Complete Task {red}[{end_time21}]{reset} Seconds')
        print('X' * 50)
        print('X' * 50)
        print()
        print(' :: Killing Threads:: ')
        print(f'Checking For Alive Threads'.center(width))
        executor.shutdown()
        print(f"d.isAlive(), {results.is_alive()}")
        #  print(f"d.isAlive(), {t0.is_alive()}")
        print('X' * 50)
        print('X' * 50)
        print(f'{bblue} Moving on to next iteration {reset}'.center(width))

except Exception as f:
    traceback.print_exc()
    print(str(f))

    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####

try:
    with Spinner():
        start05 = time.time()
        for i, d in zip(PRIMES, map(is_primeIII, PRIMES)):
            async def fetch_data02(PRIMES):
                task = asyncio.create_task(read_data(PRIMES))
                await task
                await asyncio.sleep(.00000000000001)


            async def read_data(PRIMES):
                print(PRIMES)
                await asyncio.sleep(.00000000000001)


            print(i, d)

        end05 = time.time()
        end_time00 = end05 - start05
        print(
            'iteration for multi-threaded process (should be slower, or slightly optimized, depending on variable / function)')

        print(end_time00)
        TICKER += 1
        time.sleep(3)

except Exception as f:
    traceback.print_exc()
    print(str(f))

# ##### ###### ###### ##### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ######
# ##### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ######
# ##### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ######
#

#
display_header()
display_header2()

time.sleep(5)


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(.000000000001)
    id00 = threading.get_ident()
    print(id00)
    logging.info("Thread %s: finishing", name)


#### SIMPLE THREAD ### PRIME ##
try:
    with Spinner():
        ## start sequence ##
        current_time001 = time.time()
        current_time002 = time.ctime(current_time001)
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        print(f' :: Starting Test on {bblue} SIMPLE THREAD / PRIME # ITERATOR {reset} :: '.center(width))
        print(
            f'{blue}This is Multi-Threading,{red}Asyncio{reset} and effeciant will depend on the Test Algo.{reset}'.center(
                width))
        print(f'starting: {yellow}[{current_time01}]{reset}'.center(width))
        print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        time.sleep(5), print(), print()

        for i in PRIMES_TEST_RANGE:
            t5 = threading.Thread(target=is_primeIII, args=(i,))
            t5.start()

        print('main thread end!')
        # if action(is_prime):
        #     print('sucesses')

        print(), print()
        print('X' * 50)
        print('X' * 50)
        print()
        end001 = time.time()
        cry_time002 = time.ctime(end001)
        end_time002 = end001 - current_time001
        print(f'{bblue}Multi-Threaded Iteration With Thread Pool Results: {bblue}'.center(width))
        print(f'The Test Range : {yellow}[{PRIMES_TEST_RANGE}{reset}]')
        print(f'Thread Count: [{yellow}{threading.active_count()}{reset}')
        print(f'Task  completed in: {yellow}[{end_time21}{reset}]')
        print(f'Task  completed at: {yellow}[{cry_time20}{reset}]')
        print(f'Thread Count: [{red}{threading.active_count()}{reset}]')
        print(f'Time To Complete Task {red}[{end_time21}]{reset} Seconds')
        print('X' * 50)
        print('X' * 50)
        print()
        print(' :: Killing Threads:: ')
        print(f'Checking For Alive Threads'.center(width))
        # executor.shutdown()
        print(f"d.isAlive(), {t5.is_alive()}")
        # print(f"d.isAlive(), {t0.is_alive()}")
        print('X' * 50)
        print('X' * 50)
        print(f'{bblue} Moving on to next iteration {reset}'.center(width))

        time.sleep(7)
        clear()


except IOError as f:
    print(str(f))

try:  ## MULTI PROCESSING ##
    with Spinner():
        ## start sequence ##
        current_time011 = time.time()
        current_time012 = time.ctime(current_time011)
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        print(f' :: Starting Test on {bblue}MULTI PROCESSING ITERATION Range Iterator{reset} :: '.center(width))
        print(
            f'{blue}This is Multi-Threading,{red}Asyncio{reset} and effeciant will depend on the Test Algo.{reset}'.center(
                width))
        print(f'starting: {yellow}[{current_time012}]{reset}'.center(width))
        print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        time.sleep(5), print(), print()

        start01 = time.time()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for number, prime in tqdm(zip(PRIMES_TEST_LIST, executor.map(is_primeIII,
                                                                         PRIMES_TEST_LIST))):  # zip the list into a tuple, and map to function
                print('%d is prime: %s' % (number, prime))

            ## end sequence

            print(), print()
            print('X' * 50)
            print('X' * 50)
            print()
            end012 = time.time()
            cry_time012 = time.ctime(end012)
            end_time012 = end012 - current_time011
            print(f'{bblue}Multi-Threaded Iteration With Thread Pool Results: {bblue}'.center(width))
            print(f'The Test Range : {yellow}[{PRIMES_TEST_RANGE}{reset}]')
            print(f'Thread Count: [{yellow}{threading.active_count()}{reset}')
            print(f'Task  completed in: {yellow}[{end_time012}{reset}]')
            print(f'Task  completed at: {yellow}[{cry_time012}"{reset}]')
            print(f'Thread Count: [{red}{threading.active_count()}{reset}]')
            print(f'Time To Complete Task {red}[{end_time012}]{reset} Seconds')
            print('X' * 50)
            print('X' * 50)
            print()
            print(' :: Killing Threads:: ')
            print(f'Checking For Alive Threads'.center(width))
            executor.shutdown()
            print(f"d.isAlive(), {d0.is_alive()}")
            # print(f"d.isAlive(), {t0.is_alive()}")
            print('X' * 50)
            print('X' * 50)
            print(f'{bblue} Moving on to next iteration {reset}'.center(width))

            time.sleep(7)
            clear()



except Exception as f:
    traceback.print_exc()
    print(str(f))

display_header3()
print(f'{blue} MULTI PROCESSING (ld way) using logging Range Iterator {reset}'.center(width))

try:  ### old way of setting up multi thread
    current_time013 = time.time()
    current_time014 = time.ctime(current_time013)
    print(f"{'X' * 50}".center(width))
    print(f"{'X' * 50}".center(width))
    print(
        f' :: Starting Test on {bblue}MULTI PROCESSING (ld way) using logging Range Iterator{reset} :: '.center(width))
    print(
        f'{blue}This is Multi-Threading,{red}Asyncio{reset} and effeciant will depend on the Test Algo.{reset}'.center(
            width))
    print(f'starting: {yellow}[{current_time014}]{reset}'.center(width))
    print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
    print(f"{'X' * 50}".center(width))
    print(f"{'X' * 50}".center(width))
    time.sleep(5), print(), print()

    # if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    start = time.time()
    logging.info("Main    : before creating thread")

    X = threading.Thread(name='thread04', target=is_primeIII, args=(PRIMES_TEST_RANGE,))

    for number, prime in zip(PRIMES, executor.map(is_primeIII, PRIMES)):
        print('%d is prime: %s' % (number, prime))
        logging.info("Main    : before running thread")
        X.start()
        print('%d is prime: %s' % (i, d))
        logging.info("Main    : wait for the thread to finish")
        X.join()
        logging.info("Main    : all done")

    end014 = time.time()
    end_time014 = end014 - start014
    cry_end014 = time.ctime(end014)
    print(f'End Time: [{cry_end014}]')
    print(f'Time to complete:  [{end_time014}]')
    TICKER += 1

    ## END SEQUENCE ##

    ## end sequence

    print(), print()
    print('X' * 50)
    print('X' * 50)
    print()
    end012 = time.time()
    cry_time012 = time.ctime(end012)
    end_time012 = end012 - current_time011
    print(f'{bblue}Multi-Threaded Iteration With Thread Pool Results: {bblue}'.center(width))
    print(f'The Test Range : {yellow}[{PRIMES_TEST_RANGE}{reset}]')
    print(f'Thread Count: [{yellow}{threading.active_count()}{reset}')
    print(f'Task  completed in: {yellow}[{end_time012}{reset}]')
    print(f'Task  completed at: {yellow}[{cry_time012}"{reset}]')
    print(f'Thread Count: [{red}{threading.active_count()}{reset}]')
    print(f'Time To Complete Task {red}[{end_time012}]{reset} Seconds')
    print('X' * 50)
    print('X' * 50)
    print()
    print(' :: Killing Threads:: ')
    print(f'Checking For Alive Threads'.center(width))
   #fexecutor.shutdown()
   # print(f"d.isAlive(), {d0.is_alive()}")
    # print(f"d.isAlive(), {t0.is_alive()}")
    print('X' * 50)
    print('X' * 50)
    print(f'{bblue} Moving on to next iteration {reset}'.center(width))

except Exception as f:
    traceback.print_exc()
    print(str(f))

display_header3()
print(f'{blue} Complex Multi-Threaded PRIME iterator  {reset}'.center(width))
try:  ## complex way of starting thread
    ## start of sequence
    threads = list()

    current_time065 = time.time()
    current_time066 = time.ctime(current_time065)
    print(f"{'X' * 50}".center(width))
    print(f"{'X' * 50}".center(width))
    print(
        f' :: Starting Test on {bblue} Complex Multi-Threaded PRIME iterator {reset} {red} DAEMON ON {reset}:: '.center(
            width))

    print(f'starting: {yellow}[{current_time065}]{reset}'.center(width))
    print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
    print(f"{'X' * 50}".center(width))
    print(f"{'X' * 50}".center(width))
    time.sleep(5), print(), print()


    def worker():
        for index in PRIMES_TEST_RANGE:
            logging.info("Main    : create and start thread %d.", index)
            x = threading.Thread(target=slave, args=(index,))
            threads.append(x)
            x.start()


    def slave():
        for index, thread in enumerate(threads):
            logging.info("Main    : before joining thread %d.", index)
            thread.join()
            logging.info("Main    : thread %d done", index)


    if __name__ == '__main__':
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            executor.map(worker, PRIMES_TEST_RANGE)

        print('X' * 50)
        print('X' * 50)

        ### end sequence ###

        print(), print()
        print('X' * 50)
        print('X' * 50)
        print()
        end065 = time.time()
        cry_time065 = time.ctime(end065)
        end_time065 = end065 - current_time065

        print(f'{bblue} Complex Multi-Threaded PRIME iterator {bblue}'.center(width))
        print(f'The Test Range : {yellow}[{PRIMES_TEST_RANGE}{reset}]')
        print(f'Thread Count: [{yellow}{threading.active_count()}{reset}')
        print(f'Task  completed in: {yellow}[{end_time065}{reset}]')
        print(f'Task  completed at: {yellow}[{cry_time065}{reset}]')
        print(f'Thread Count: [{red}{threading.active_count()}{reset}]')
        print(f'Time To Complete Task {red}[{end_time065}]{reset} Seconds')
        print('X' * 50)
        print('X' * 50)
        print()
        print(' :: Killing Threads:: ')
        print(f'Checking For Alive Threads'.center(width))
        print(f"d.isAlive(), {d0.is_alive()}")
        print(f"d.isAlive(), {t0.is_alive()}")
        print('X' * 50)
        print('X' * 50)
        print(f'{bblue} Moving on to next iteration {reset}'.center(width))

        time.sleep(7)
        clear()

except Exception as f:
    traceback.print_exc()
    print(str(f))

############################# START OF MULTI PROCESSING

display_header3()
print(f'[{TICKER}] ::{blue} Starting multi-processing with daemon on {reset} :: [{TICKER}] '.center(width))
print(f'[{TICKER}] ::{blue} Starting multi-processing with daemon on {reset} :: [{TICKER}]  '.center(width))


def randomNum_genIII():
    start = 1  # inclusive
    end = 8  # exclusive
    n = 8  # size -- coorleate to 8 max cores, could double tthe time if 4 cores.
    rand_int = random.random()
    rand_float = rand_int / 10  # see line 1072
    print(rand_float)

    return rand_float


def threading_functionIIII(rand_float):
    print(f'Sleeping for {rand_float} Seconds.')
    time.sleep(seconds)
    return f'Done Sleeping {rand_float}'


try:
    current_time201 = time.time()
    current_time202 = time.ctime(current_time201)
    with Spinner():
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))

        print(f'starting: {yellow}[{current_time202}]{reset}'.center(width))
        print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
        print(f"{'X' * 50}".center(width))
        print(f"{'X' * 50}".center(width))
        time.sleep(5), print(), print()

        print(f'[{TICKER}] ::{blue} Starting multi-processing with daemon on {reset} :: [{TICKER}]  '.center(width))
        for i, d in zip(PRIMES, map(is_primeIII, PRIMES)):
            rand_floatIII = randomNum_genIIII()
            f1 = executor.submit(threading_functionIIII, rand_floatIIII)
            print(f1.result)

        # for y in concurrent.futures.as_completed(f1):
        #     print(y.result())

        # print(f1.results)

        ## end of sequence
        #########

        print(), print()
        print('X' * 50)
        print('X' * 50)
        print()
        end201 = time.time()
        cry_time201 = time.ctime(end201)
        end_time201 = end201 - current_time201
        print(f'{bblue}Multi-Threaded Iteration With Thread Pool Results: {bblue}'.center(width))
        print(f'The Test Range : {yellow}[{PRIMES_TEST_RANGE}{reset}]')
        print(f'Thread Count: [{yellow}{threading.active_count()}{reset}')
        print(f'Task  completed in: {yellow}[{end_time201}{reset}]')
        print(f'Task  completed at: {yellow}[{cry_time201}{reset}]')
        print(f'Thread Count: [{red}{threading.active_count()}{reset}]')
        print(f'Time To Complete Task {red}[{end_time201}]{reset} Seconds')
        print('X' * 50)
        print('X' * 50)
        print()
        print(' :: Killing Threads:: ')
        print(f'Checking For Alive Threads'.center(width))
       # executor.shutdown()
        print(f"d.isAlive(), {d0.is_alive()}")
        print(f"d.isAlive(), {t0.is_alive()}")
        print('X' * 50)
        print('X' * 50)
        print(f'{bblue} Moving on to next iteration {reset}'.center(width))

        time.sleep(7)
        clear()


except Exception as ef:
    traceback.print_exc()
    print(str(ef))


print(f'{red} -- END OF SEQUENCE -- {reset} ')
sys.exit(1)

# def wait_on_future():
#     f = executor.submit(pow, 5, 2)
#     # This will never complete because there is only one worker thread and
#     # it is executing this function.
#     print(f.result())
#
# executor = ThreadPoolExecutor(max_workers=1)
# executor.submit(wait_on_future)
#
#
# # establish paralell task
# def task_iseven(num00):
#     for num00 in var_list:
#         return num00

#
# ##### ###### ###### ##### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ######
#
#
# print(f'[{TICKER}] :: Starting multi-processing with daemon on :: [{TICKER}]  '.center())
# print(f'This is Multi-Processing, this may be more effeciant than the former, depending on the Test Algo.')
# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(.000000000001)
#     logging.info("Thread %s: finishing", name)
#
#
# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#
#     start = time.time()
#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,), daemon=True)
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     x.join
#     logging.info("Main    : all done")
#
#     end = time.time()
#     end_time = end - start
#     cry_end = time.ctime(end)
#     print(f'End Time: [{cry_end}]')
#     print(f'Time to complete:  [{end_time}]')
#     TICKER += 1
#
#
# ######################
# #################
#
# x = threading.Thread(name = 'thread01', target=lambda a: sys.stdout.write("\n".join(a) + "\n"))

#
# x.start()
#
# print('System End... Lets go to the sky.. ')
# timer.sleep(1)
# webbrowser.open("https://xkcd.com/2258")
# timer.sleep(2)
# sys.exit()
#
#
#
#
#
# def prime():
#     time.sleep(.1)
#     print(b.result())  # b will never complete because it is waiting on a.
#     return .1
#
# def not_prime():
#     time.sleep(.01)
#     print(a.result())  # a will never complete because it is waiting on b.
#     return .01
#
#
#
# executor = ThreadPoolExecutor(max_workers=2)
# a = executor.submit(even)
# b = executor.submit(odd)
#
# if True:
#     sys.exit()
# else:
#     sys.exit()
#
#
#
#
#


#
# ## for loop i lambda
# filter(lambda n: n%y != 0 for y in range(2,n), range(2,n+1))
#
# x = threading.Thread(name='thread01', target=lambda x=var_range: list(map(print, x)))
#
# print(threading.currentThread().getName())  ## to get thread name ##
#
# if True:
#     print('goodbye.. ?')
#     time.sleep(1.5)
#     import antigravity
#     sys.exit()
#


#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####

#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
##              ##                 ##                 ##                ###               ###
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####

#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####


#
#
# sys.exit()
#

# ## define multi-threading function
# def countHighFrequencyItem(var_list):
#     if len(var_list) == 0:
#         return 0


# all_tasks = []
#
# with ThreadPoolExecutor(max_workers=4) as executor:
#     for index in range(len(var_list)):
#         all_tasks.append(
#             executor.submit(
#                 task,
#                 var_list[index],
#                 index))
#         temp_res = list(range(len(var_list)))
#
#     # parse the completed tasks
#     for future_var in as_completed(all_tasks):
#         tooFrequent, index00 = future_var.result()
#         temp_res[index00] = tooFrequent
#
#     count = 0
#     for is_frequent in temp_res:
#         if is_frequent:
#             print(temp_res)
#             count += 1
#            # return count
#


# x = lambda x=var_list: sys.stdout.write("\n".join(var_list) + "\n")
# print(x)
# x()


###


# x()


#
# # for loop in threading lambda
# t= threading.Thread(name='func'+str(i), target=lambda i=i: func())
#
# ## my version
#
#
# #
# #
# #
# #
# # if xy:
# #     print('v working')
# # else:
# #     print('v not working')
# #
# # if t:
# #     print('t working')
# # else:
# #     print('t not working')
# #
# # if x:
# #     print('x working')
# #     sys.exit
# #
# # else:
# #     print('v not working')
# #     sys.exit()
#
#
#
#
#
# # if x:
# #     print('working')
# #     sys.exit(1)
# # else:
# #     print('not working')
# #     sys.exit(0)
# #
#
#
#
#
#
#
#
#
#
# #- Method 1: pass the method to be executed as a parameter to the Thread The construction method of the model
# ## SPAWN A THREAD AND PASS IT ARGUMENTS, TO TELL WORK WHAT TO DO
#
# def action(arg):
#     time.sleep(1)
#     print('the arg is:% ', arg)
#
# for i in range(4):
#     t =threading.Thread(target=action,args=(i,))
#     t.start()
#
# print('main thread end!')
#
# if action(arg):
#     sys.exit(1)
#
# #### METHOD 2 ### A LITTLE BIT MORE COMPLEX THREAD, WHERE EACH THREAD IS NAMED
#
# def worker():
#     print(threading.currentThread().getName(), 'Starting')
#     time.sleep(2)
#     print(threading.currentThread().getName(), 'Exiting')
#
# def my_service():
#     print(threading.currentThread().getName(), 'Starting')
#     time.sleep(3)
#     print(threading.currentThread().getName(), 'Exiting')
#
# t = threading.Thread(name='my_service', target=my_service)
# w = threading.Thread(name='worker', target=worker)
# w2 = threading.Thread(target=worker) # use default name
#
# w.start()
# w2.start()
# t.start()
#
#
# #- Method 2: from Thread Inherit and rewrite run()
# class MyThread(threading.Thread):
#     def __init__(self,arg):
#         super(MyThread, self).__init__()#Note: be sure to explicitly call the initialization function of the parent class.
#         self.arg=arg
#     def run(self):#Define the function to run for each thread
#         time.sleep(1)
#         print('the arg is:%s\r' % self.arg)
#
# for i in range(4):
#     t =MyThread(i)
#     t.start()
#
# print('main thread end!')
#
#
#
#
# ### Method 3 ## Creating thread using threading Module
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       print_time(self.name, 5, self.counter)
#       print ("Exiting " + self.name)
#
# def print_time(threadName, counter, delay):
#    while counter:
#       if exitFlag:
#          threadName.exit()
#       time.sleep(delay)
#       print ("%s: %s" % (threadName, time.ctime(time.time())))
#       counter -= 1
#
# # Create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # Start new Threads
# thread1.start()
# thread2.start()
#
# print("Exiting Main Thread")
#
#
#
#
