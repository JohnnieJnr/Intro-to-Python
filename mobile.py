import requests
url="https://maker.ifttt.com/trigger/Global Code/with/key/mLfhMuof3XvnrPAM_qZQcnKGTlJ2IMbRrQ_rJN2F8Le"
r = requests.get(url)
c=r.status_code
print(c)