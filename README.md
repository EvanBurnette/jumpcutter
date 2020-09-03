## Purpose

Jumpcutter speeds up or cuts out silent time from your videos.
See carykh's original readme below for more details. Video explanation here: https://www.youtube.com/watch?v=DQ8orIurGxw

## Installation

1. Installing python and ffmpeg:

    Download python: https://www.python.org/downloads/
    Download FFmpeg: https://ffmpeg.org/download.html

    Python and FFmpeg must be accessible via command line therefore both programs must be added to the path.

    On Windows, check the box to add python to environment variables.
    FFmpeg comes in a folder which you can add to program files. 
    On windows FFmpeg must be added manually to the path.

    On mac follow this guide for ffmpeg: https://www.youtube.com/watch?time_continue=277&v=8nbuqYw2OCw&feature=emb_logo

    On mac follow this guide for python: https://www.youtube.com/watch?v=TgA4ObrowRg

    Test that each is installed by typing calling them from the command line. (quit() to exit python)

2. Install package dependencies:

    Open a terminal and navigate to the jumpcutter folder and run this command: "pip install -r requirements.txt"

3. Run the program:
    
    Double click the jumpcutterGUI.py file and navigate to the file you want to process. The output file will appear in the same folder as the original file.

(Note: If the TEMP folder is not deleted, the script will crash. The script should automatically delete the folder usually. The TEMP folder is in the same folder as the script.)

Happy Cutting!

Carykh's original readme:
----------------------------------------------------------------------------------
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
