Extractor
===========

This is a Python script that fixes two minor annoyances I have with extracting archives:

1. You usually don't know how many files are inside it - sometimes the archive contains 100+ files that will overwhelm your current directory when you extract them. Sure, you could play safe and extract them to a new directory, but this is a little tedious if the archive actually contains only a couple of files.

2. After extracting the archive needs to be deleted, which is an action that should be automatically executed.


These are petty issues, but over the course of a computer user's lifetime a lot of extraction takes place. This script helps a little.

Extractor fixes this problem by checking how many files will be extracted, and deciding if they should go in a new directory or the current one.


Usage
------
Before using the script you need to edit it to set your 7-Zip's (or other extracting software's) exe path.

You can also specify the number of files in an archive that will trigger the creation of a new directory.

To run the script call it with the archive's path as the argument. Because this isn't very user-friendly, you should set this script to be the default program for .zips, .rars, etc. You can download registry entries that accomplish that here: [download registry entries](https://github.com/Winterstark/Extractor/tree/master/file%20association%20registry%20entries)

To use the registry entries first run "reg_app_extractor.reg" to create a class for the Extractor filetype, and then run any or all of the other entries - each associates the Extractor class with a filetype (7z/rar/zip). These entries are very simple and can easily be edited to associate any other filetype you may need.




Notes
------
* After extracting the archives aren't permanently deleted: they're just sent to the Recycle Bin.
* Tested on Windows 7 only.
* Running Extractor on files on the Desktop sometimes confuses Windows so it doesn't display the extracted files. Just press F5 to refresh and the files will appear.