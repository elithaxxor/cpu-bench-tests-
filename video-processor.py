import ffmpeg, sys, numpy, traceback, time, os, platform, threading, subprocess
from subprocess import call
#from rich import print
#pip install ffmpeg-python


def OS_info():
    global width; width = os.get_terminal_size().columns
    terminal = os.environ.get('TERM')
    #width_len = len(width)
    cwd = os.getcwd()
    #  IP_INFO = f"\033[1;35;0m {IPx.IP}"
    current_version = platform.release(); system_info = platform.platform(); os_name0 = platform.system(); current_platform = platform.system()
    platform_name = sys.platform; big_names = platform.uname(); processor = platform.processor(); architecture = platform.architecture(); user_id = os.uname() ;login = os.getlogin()
    print()
    print('X' * 50)
    print(f'**[SYSTEM INFO]**'.center(width))
    print()
    print(f'\033[1;35;m [CURRENT_PLATFORM]--[{current_platform}]  ...? '.center(width))
    print(f'\033[1;35;m [PLATFORM_NAME]--[{platform_name}]  ...? '.center(width))
    print(f'\033[1;35;m [CURRENT_VERSION]--[{current_version}]  ...? '.center(width))
    print(f'\033[1;35;m [OS-NAME]--[{os_name0}] + [{terminal}] ...? '.center(width))
    print(f'\033[1;35;m [SYSTEM-INFO]--[{system_info}]  ...? '.center(width))
    print(f'\033[1;35;0m [CURRENT-VERSION]--[{current_version}]  ...? '.center(width))
    print(f'\033[1;35;0m [UUID]--[{big_names}]  ...? '.center(width))
    print(f'\033[1;35;0m [PROCESSOR]--[{processor}]  ...? '.center(width))
    print(f'\033[1;35;0m [ARCHITECTURE]--[{architecture}]  ...? '.center(width))
    print(f'\033[1;35;0m [USER-ID]--[{user_id}]  ...? '.center(width))
    print(f'\033[1;35;0m [LOGIN]--[{login}]  ...? '.center(width))
    print('X' * 50)


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
    pretty = f'{red0}xxx FILE-MOVER xxx{reset0}'.center(width)
    print(f'{pretty : ^70}')
    print(f"{'X' * 125: ^70}")

    one = (
        f'{bblue}[SCRIPT] *** A/V Converter *** {bblue}')
    two = (
        f'[USAGE] - [1] The Program will can: 1.] re-encode AV Conntainers to whatever format needed. IE- .MP4 -> .MOV')
    three = (
        f'[USAGE] - [2] Trim AV, with Min/Max Values && duration ')
    four = (f'[USAGE] - [3] Compresses the AV, by rescaling resolution and resizing file')
    five = (
        f'[USAGE] - [5] Play Videos.{reset}')
    six = (f'{red}[+]-[+] copyright material from Adel Al-Aali [+]-[+] {reset}')
    seven = (f'[+] Future Addtion: Attach to OS.Listwalker and impliment Generator/text feed to auto convert large lists  [+]')

    print(f"{one:^70}")
    print(f"{two:^70}")
    print(f"{three:^70}")
    print(f"{four:^70}")
    print(f"{five:^70}")
    print(f"{six:^70}")
    print(f"{seven:^70}")
    print(f"{x * 20: ^70}")
    print(), print()



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

def period_wait():
    period = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    # multi = [2,2,2,2,2,2,2,2,2,2]
    period_len = len(period)
    with Spinner():
        for z, x in enumerate(period):
            print(x)
            time.sleep(.2)
            if z <= period_len:
                z += 1
                print(f"{yellow}{x * z}{reset}")
                continue
            elif z == period_len:
                break


def clear():
    # check and make call for specific operating system
    os_name = platform.system()
    _ = call('clear' if os_name == 'Linux' or 'Windows' or 'Darwin' else 'cls')



###########
color = Colors()
spinner = Spinner()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset
def splash():
    with Spinner():
        display_header()
        period_wait()
        time.sleep(8)
        clear()

### display headers ##
OS_info()
time.sleep(5)
clear()
splash()

class VideoEditor():
    def __init__(self):
        print(f'[+] Enter **[Desired]** File Name ex:: [sample.mp4], \n\t[+] Press Enter for default file_name [new_vid]\n')
        self.file00 = input('')
        if self.file00 == '':
            self.file00 = 'new_vid.mp4'
        self.cwd = os.getcwd()
        print(f" \n {'x'*50} \n [++] CWD :: \n \t [{self.cwd}][++]\n")
        self.vid_loc = input('[+] Enter Video Location')
        self.streamVideo = ffmpeg.input(self.vid_loc)


    def __repr__(self):
        return "<Test a:%s >" % (self)
    def __str__(self):
        return "From str method of Test: %s" % (self)

    def trimVideo(self):
        try:
            print('\n','X'*50)
            trim_start = time.time(); CTtime = time.ctime(trim_start)
            start = f'[+] -- [INIIATING TRIM SEQUENCE] [+] \n{CTtime}'
            print(f'[+] Enter the The Desired Start and Duration [+] \n[+]** [START] ')
            tstart = input('')

            print(f'[+]** [DURATION] ')
            tdur = input('')
            print()
            print(f'{start}')
            streamVideo = self.streamVideo.trim(start=tstart, duration=tdur)
            streamVideo = ffmpeg.output(streamVideo, self.file00)
            ffmpeg.run(streamVideo)
            trim_end = time.time(); ct_end = trim_start-trim_end
            end = f'[+]  \n\t Completion Seconds [{round(trim_end, 3)}] \n {ct_end}'
            print(f'{end}')
            encoding_text = 'ff_manip.txt'
            with open(encoding_text, 'a') as f:
                f.write(str('meta\n' + str(self.streamVideo))+'\n'+'\n')
                f.write(str('trim data' + str(start) +'\n'+'\n'))
                f.write(str('trim_start'+ str(end)+ '\n'+'\n'))
                f.write(str('trim_end' + str(end)+ '\n'+'\n'))
                f.write(str(streamVideo))
            print(f'[+] Trim Data Saved to \n{encoding_text}')
            return f'[+] Succesfully trimmed data \n \t\t[START] [{tstart}] :: [DUR] [{tdur}]'

        except Exception as e:
            traceback.print_exc()
            return f'[-] Error in Trim Parse \n \n [{e}]\n\t\t :: [FILE_NAME]--[[{self.file00}]] ::   \t\t[START] [{tstart}] :: [DUR] [{tdur}] \n{traceback.print_exc()}'

    def encoder(self):
        try:
            print('\n', 'X'*50)
            print('[+] Enter The Desired Filename / Encoding [ex: output.mp4]')
            encode_out = input('')
            encode_start = time.time(); ECTtime = time.ctime(encode_start)
            start = f'[+] -- [INIIATING TRIM SEQUENCE] [+] \n{ECTtime}'
            print(f'{start}')
            streamVideo = ffmpeg.output(self.streamVideo, encode_out)
            ffmpeg.run(streamVideo)
            encode_end = time.time(); ect_end= encode_start - encode_end
            end = f'[+]  \n\t Completion Seconds [{round(encode_end, 3)}] \n {ect_end}'
            print(f'{end}')
            encoding_text = 'ff_manip.txt'
            with open(encoding_text, 'a') as f:
                f.write(str('meta\n' + str(self.streamVideo))+'\n'+'\n')
                f.write(str('encoding start' + str(start))+'\n'+'\n')
                f.write(str('encoding end' + str(end))+'\n'+'\n')
                f.write(str('encoding data ' + str(streamVideo)+'\n')+'\n')

            print(f'[+] Trim Data Saved to \n{encoding_text}')
            return f'[+] [Successfully Formatted Data] \n \t\t[FILE_NAME] [{encode_out}] :: '
        except Exception as e:
            traceback.print_exc()
            return f'[-] Error in Trim Parse \n \n [{e}] \t\t:: [FILE_NAME]--[[{self.file00}]] ::   \n{ traceback.print_exc()}'

    def changeFPS(self):
        try:
            print('\n','X'*50)
            print('[+] Enter The Desired fps [must be INT]\n **')
            fps = input('')
            fps = int(fps)
            fps_start = time.time()
            fpsctime = time.ctime(fps_start)
            start = f'[+] -- [INIIATING TRIM SEQUENCE] [+] \n{fpsctime}\t\t [FPS] --[{fps}]'
            print(f'{start}')
            streamVideo = self.streamVideo.filter('fps', fps=fps, round='up')
            streamVideo = ffmpeg.output(self.streamVideo, self.file00)
            ffmpeg.run(streamVideo)
            encoding_text = 'ff_manip.txt'

            print(f'[+] [CHANGE FPS -- SUCCESS] \n{streamVideo}')
            fps_end = time.time(); fect_end=fps_start-fps_end
            end = f'[+]  \n\t Completion Seconds [{round(fps_end, 3)}] \n {fps_end}'
            print(f'{end}')
            with open(encoding_text, 'a') as f:
                f.write(str('meta' + str(self.streamVideo))+'\n')
                f.write(str('encoding start' + str(start))+'\n')
                f.write(str('encoding end' + str(fps_end))+'\n')
                f.write(str('encoding meta' + str(streamVideo))+'\n')
            return f'[+] [Successfully CHANGED DATA FPS ] \n \t\t:: [FILE_NAME]--[[{self.file00}]] ::   '


        except Exception as e:
            traceback.print_exc()
            return f'[-] Error in Trim Parse \n \n [{e}] \t\t :: [FILE_NAME]--[[{self.file00}]] ::  \n{traceback.print_exc()}'

    def scaleVideo(self):
        try:
            print('\n', 'X' * 50)
            scalestart = time.time()
            cscalestart = time.ctime(scalestart)
            start = f'[+] -- [INIIATING VIDEO-SCALER] -- [+] \n{cscalestart}'
            print(f'[+] Enter the The Desired Scale Resolution *[MUST BE INT]* [+] \n\t\t [+]**[HORZONTAL]')
            horz = input('')
            print('\n\t\t[+]**[VERTICAL]')
            vert = input('')
            scale = f'{horz}x{vert}'
            print(f'[+] Entered :: [{str(scale)}]')
            print(f'{start}')
            streamVideo = self.streamVideo.filter('scale', w=horz, h=vert)

            streamVideo = ffmpeg.output(self.streamVideo, str(self.file00))

            ffmpeg.run(streamVideo)
            print(f'[+] [CHANGE FPS -- SUCCESS] \n{streamVideo}')
            scale_end = time.time();
            scalEnd = scalestart - scale_end
            scaleEndC= time.ctime(scalEnd)
            end = f'[+]  \n\t Completion Seconds [{round(scalEnd, 3)}] \n {scaleEndC}'
            print(f'{end}')
            encoding_text = 'ff_manip.txt'
            with open(encoding_text, 'a') as f:
                f.write(str('meta' + str(self.streamVideo)))
                f.write(str('Scale Start' + start))
                f.write(str('Resolution' + scale))
                f.write(str('Scale End' + str(scalEnd)))
                f.write(str('Scale meta' + str(streamVideo)))

            return f'[+] [Successfully Scaled Video ] \n \t\t:: [FILE_NAME]--[[{self.file00}]] :: \n\t\t [{scale}] '


        except Exception as e:
            traceback.print_exc()
            return f'[-] Error in [SCALING VIDEO]\n \n [{e}] \t\t:: [FILE_NAME]--[[{self.file00}]] ::   \n{traceback.print_exc()}'


v_Editor = VideoEditor()
affirmative = ["Yes","yes","YES","y","Y","ye","YE",""]
negative = ["No","no","NO","n","N","neg"]
print('[+] A/V Converter.')

try:
    print(f"\n {'X'*50}") ## ENCODER
    print('[+] Change Encoding?')
    encodeA = input('')
    if encodeA in affirmative:
        flag01 = v_Editor.encoder()
        print(f'[++] -- {flag01} -- [++]')
    elif encodeA in negative:
        print('[-] Passing -- [ENCODE VIDEO]')
        pass

    print(f"\n {'X'*50}") ## TRIMMER
    print('[+] Trim Video?.')
    trimA = input('')
    if trimA in affirmative:
        print('[+] Starting -- [TRIM VIDEO] -- [+]')
        flag = v_Editor.trimVideo()
        print(f'[++] -- {flag} -- [++]')
        print(f"{'X' * 50}\n")

    elif trimA in negative:
        print('[-] Passing -- [TRIM VIDEO]')
        pass

    print('[+] Change FPS?') ## FPS
    fpsA = input('')
    if fpsA in affirmative:
        print('[+] Starting --[CHANGE FPS] -- [+].')
        flag = v_Editor.changeFPS()
        print(f'--[{flag}]--')

    elif fpsA in negative:
        print('[-] Passing -- [CHANGE FPS]')
        pass

## VIDEO SCALER
    print(f"\n {'X' * 50}")  ## TRIMMER
    print('[+] Scale Video?.')
    scaleA = input('')

    if scaleA in affirmative:
        print('[+] Starting -- [SCALE-VIDEO] -- [+]')
        flag = v_Editor.scaleVideo()
        print(f'[++] -- {flag} -- [++]')
        print(f"{'X' * 50}\n")
    elif trimA in negative:
        print('[-] Passing -- [VIDEO-SCALER]')
        splash()
        pass
except Exception as e:
    print(f'[-] Error in Trim Parse \n \n [{e}] \t\t \n{traceback.print_exc()}')


# ## reduce video fps
# streamVideo = streamVideo.filter('fps', fps=10, round='up')
# ## change video scaling
# streamVideo = streamVideo.filter('scale', w=128, h=128)
# ## output
# streamVideo = ffmpeg.output(streamVideo, 'output.mov')
# ffmpeg.run(streamVideo)



