import dnspython as dns
import dns.resolver
import requests
from bs4 import BeautifulSoup

#code flow
#input subdomains list
#send request and pars html 
#match with given error 
#if match thn print
#finish and I love u <3


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
errortext = [
"Do you want to register *.wordpress.com?", #Wordpress
"This UserVoice subdomain is currently available", #UserVoice
"page not found",#Uptimerobot
"Please renew you subscription",#Tilda
"Whatever you were looking for doesn't currently exist at this address",#Tumblr
"project not found",#Surge.sh
"page not found",#Strikingly
"Visiting the subdomain will redirect users to https://www.statuspage.io.",#Statuspage
"Sorry, this shop is currently unavailable.",#Shopify
"404 error unknown site!",#Readme.io
"Unrecognized domain",#Pantheon
"It looks like you may have taken a wrong turn somewhere. Don't worry...it happens to all of us.",#LaunchRock
"No Site For Domain",#Kinsta
"is not a registered InCloud YouTrack",#JetBrains
"Uh oh. That page doesn't exist.",#Intercom
"No settings were found for this company:",#Help Scout
"We could not find what you're looking for.",#Help Juice
"404 Blog is not found",#HatenaBlog
"There isn't a Github Pages site here.",#Github
"The thing you were looking for is no longer here, or never was",#Ghost
"404 Not Found",#Fly.io
"The feed has not been found.",#Feedpress
"Fastly error: unknown domain:",#Fastly
"Domain uses DO name serves with no records in DO.",#Digital Ocean
"404 Not Found",#Cargo Collective
"Trying to access your account?",#Campaign Monitor
"Repository not found",#Bitbucket
"The specified bucket does not exist",#AWS/S3
]
print(errortext[0])
#f = open("sites.txt" , "r")
#for sites in f:
#   r = requests.get("https://"+sites)
#   print(r.status_code)