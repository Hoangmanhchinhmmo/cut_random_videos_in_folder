# cut_random_videos_in_folder
cut random videos in folder for tiktoker

Instructions:

<b>#Input Paths:</b>

You will be prompted to enter the paths to the input and output directories after running the code.
Folder Creation:

The code will create an "error" folder inside the input directory, if it doesn't already exist.

<b>#Video Processing:</b>

The code will loop through all the files in the input folder.
If a file ends with ".mp4", it will be processed.

<b>#Random Segment Extraction:</b>

A random segment (3-5 seconds) will be extracted from each video.

<b>#Output Files:</b>

Processed videos will be saved in the output folder with the prefix "output_".

<b>#Error Handling:</b>

If an error occurs during processing, it will be printed, and the original video will be moved to the "error" folder.

<b>Perform Video Processing:</b>

The process_videos function is called to start the video processing.
Remember to replace input_folder and output_folder with your actual file paths when prompted.
