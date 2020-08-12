jumpcutter speeds up or cuts out silent time from your videos

Evan's readme for busy people:

I've added a very simple gui system to navigate to the video you want to jumpcut and a single prompt that asks you for the silent speed multiplier. There are several additional default parameters in the jumpcutter.py script which you might need to edit to match your video format. In my case I have the --frame_rate set to 30fps and the audio --sample_rate set to 48000khz.

The hardest part of running this program is installing ffmpeg and Python, plus all the packages that carykh used in jumpcutter. Python and ffmpeg must be accessible via command line because the jumpcutter script sends commands to the system via command line. On windows, python and ffmpeg must be added to the "PATH" in the Environment Variables.

On mac this video might help: https://www.youtube.com/watch?time_continue=277&v=8nbuqYw2OCw&feature=emb_logo

Now that python and ffmpeg are installed, run the script (by double clicking or from command line) and when it fails just install the missing package like this: "pip install <packagename>" "pip install pyautogui" for example. (I hope to find a better method of dependency management in the future.)

To run the GUI double click the jumpcutterGUI.py file and navigate to the file you want to remove or reduce silence from and then enter the silence speed multiplier. The output file will appear in the folder with the same name as the original plus the speed.

Happy Cutting!

----------------------------------------------------------------------------------
Carykh's original readme:
# jumpcutter
Automatically edits videos. Explanation here: https://www.youtube.com/watch?v=DQ8orIurGxw

## Some heads-up:

It uses Python 3.

It works on Ubuntu 16.04 and Windows 10. (It might work on other OSs too, we just haven't tested it yet.)

This program relies heavily on ffmpeg. It will start subprocesses that call ffmpeg, so be aware of that!

As the program runs, it saves every frame of the video as an image file in a
temporary folder. If your video is long, this could take a LOT of space.
I have processed 17-minute videos completely fine, but be wary if you're gonna go longer.

I want to use pyinstaller to turn this into an executable, so non-techy people
can use it EVEN IF they don't have Python and all those libraries. Jabrils 
recommended this to me. However, my pyinstaller build did not work. :( HELP

## Building with nix
`nix-build` to get a script with all the libraries and ffmpeg, `nix-build -A bundle` to get a single binary.
