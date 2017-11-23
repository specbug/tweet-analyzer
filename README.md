# tweetAnalyzer
Android based app to search for live tweets using specific input handle and save the data in a text file.


##Overview

This is the code based on challenge for 'Learn Python for Data Science #2' by [llSourcell](https://github.com/llSourcell) on YouTube.
The code uses the tweepy library to access the Twitter API and the TextBlob library to perform Sentiment Analysis on each Tweet. We'll 
be able to see how positive or negative each tweet is about whatever topic we choose. The app is implemented on Kivy platform as it's 
written in Python.



##Dependencies

* tweepy (http://www.tweepy.org/)
* textblob (https://textblob.readthedocs.io/en/dev/)
* Kivy (https://kivy.org/docs/installation/installation-windows.html#kivy-dependencies)



##Libraries

* Kivy
  ~~~
  python -m pip install kivy
  ~~~
  
* buildozer
  ~~~
  pip install buildozer
  ~~~
  
* buildozer.spec file
  ~~~
  buildozer init
  # edit the buildozer.spec, then
  buildozer android debug deploy run (to deploy the apk on your device (Supports Linux, OS X))
  ~~~
  


##Further references

* kivy (https://kivy.org/docs/installation/installation-windows.html)

* buildozer (https://github.com/kivy/buildozer)


##Usage

After you're done with all above steps and the code, make sure you've the buildozer.spe and the tweepy.txt file in same location and 	
execute the following:

  ~~~
  python Main.py
  ~~~
  
  
##License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/specbug/tweetAnalyzer/blob/master/LICENSE) file 
for details


##Credits

The code is referenced from [llSourcell](https://github.com/llSourcell)
