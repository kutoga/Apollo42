# Apollo42

Apollo42 is a very simple tool to add artist and title ID3 tags to files. Some suggestions are shown and the
user can then choose which one shall be used (or if a custom one shall be given). The tool was mainly developed
to add tags to music files downloaded with youtube-dl.

Usage: `./apollo42.py my_mp3_file1.mp3 my_mp3_file2.mp3`

Example:
```bash
➜  ~/git/source/apollo42 git:(master) ✗ ./apollo42.py Neelix\ -\ Winter\ Sun\ \(Official\ Music\ Video\)\ \[DHADDyC5kC4\].mp3 
File: Neelix - Winter Sun (Official Music Video) [DHADDyC5kC4].mp3
[?] Please select the artist: Neelix
 > Neelix
   Winter Sun
   Neelix - Winter Sun (Official Music Video)
   Neelix - Winter Sun (Official Music Video) [DHADDyC5kC4]
   Neelix - Winter Sun (Official Music Video) [DHADDyC5kC4].mp3
   Winter Sun (Official Music Video)
   CUSTOM

[?] Please select the title: Winter Sun
   Winter Sun (Official Music Video)
 > Winter Sun
   Neelix - Winter Sun (Official Music Video)
   Neelix - Winter Sun (Official Music Video) [DHADDyC5kC4]
   Neelix - Winter Sun (Official Music Video) [DHADDyC5kC4].mp3
   Neelix
   CUSTOM

➜  ~/git/source/apollo42 git:(master) ✗ eyeD3 Neelix\ -\ Winter\ Sun\ \(Official\ Music\ Video\)\ \[DHADDyC5kC4\].mp3 
~/git/source/apollo42/Neelix - Winter Sun (Official Music Video) [DHADDyC5kC4].mp3                                                                                                                                    [ 4.75 MB ]
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Time: 04:29     MPEG1, Layer III        [ ~148 kb/s @ 48000 Hz - Stereo ]
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ID3 v2.3:
title: Winter Sun
artist: Neelix
album: 
track: 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
➜  ~/git/source/apollo42 git:(master) ✗
```
