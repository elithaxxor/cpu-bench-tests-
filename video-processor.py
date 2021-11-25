import ffmpeg, sys, numpy, traceback, time, os
#from rich import print
#pip install ffmpeg-python


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



