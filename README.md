# cut_random_videos_in_folder
cut random videos in folder for tiktoker

Instructions:

Input Paths:

You will be prompted to enter the paths to the input and output directories after running the code.
Folder Creation:

The code will create an "error" folder inside the input directory, if it doesn't already exist.
Video Processing:

The code will loop through all the files in the input folder.
If a file ends with ".mp4", it will be processed.
Random Segment Extraction:

A random segment (3-5 seconds) will be extracted from each video.
Output Files:

Processed videos will be saved in the output folder with the prefix "output_".
Error Handling:

If an error occurs during processing, it will be printed, and the original video will be moved to the "error" folder.
Perform Video Processing:

The process_videos function is called to start the video processing.
Remember to replace input_folder and output_folder with your actual file paths when prompted.
