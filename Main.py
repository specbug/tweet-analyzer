from kivy.app import App
import tweepy
from textblob import TextBlob
import csv
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class TweetPy(App):
	def build(self):
		layout = BoxLayout(padding = 10, orientation = 'vertical')
		self.txt = TextInput(text = '', multiline=False, size = layout.size)
		layout.add_widget(self.txt)
		btn = Button(text = 'Search')
		btn.bind(on_press=self.buttonClicked)
		layout.add_widget(btn)
		self.lbl = Label(text = '',size = layout.size)
		layout.add_widget(self.lbl)
		return layout

	def buttonClicked(self,btn):
		consumer_key = 'QHpJ8pdlo2qOnYQrbgXaPANbK'
		consumer_secret = 'mdyQSdwziyWv7GkQfR87IToV3SGq7dIa49KR02KOQ0mfjcqZ5Z'
		access_token = '2449128006-MPuyn5dOyyO3W44IfZ9QsFLng9fklxNluwxGJJL'
		access_token_secret = 'sT6F4CnIJOfoSXhlEzHLQDbFZrzv6AHvDw1ZmlHHQG49s'

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

		api = tweepy.API(auth)
		str = self.txt.text

		public_tweets = api.search(str)

		for tweet in public_tweets:
			analysis = TextBlob(tweet.text)
			with open("tweepy.txt", "a", newline='', encoding='utf-8') as tweetScore:
				tweetWrite = csv.writer(tweetScore)
				tweetWrite.writerow([tweet.text, analysis.sentiment.polarity, analysis.sentiment.subjectivity])
				self.lbl.text = tweet.text
		tweetScore.close()
		

if __name__ == "__main__":
	TweetPy().run()