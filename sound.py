import winsound
print('这个窗口是用来播放声音的，如果你关掉它你将听不到声音')
filename = 'BadApple.wav'
winsound.PlaySound(filename, winsound.SND_FILENAME)
