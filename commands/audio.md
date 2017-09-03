## Audios: 

* To create a large audio file - with loops of small files: 
~~~
ffmpeg -f concat -i audioLoops.txt -c copy largeTrack_A.mp3
~~~

* Contents of audioLoops.txt
~~~
file 'Track_A.mp3'
file 'Track_A.mp3'
file 'Track_A.mp3'
file 'Track_A.mp3'
file 'Track_A.mp3'
file 'Track_A.mp3'

~~~
