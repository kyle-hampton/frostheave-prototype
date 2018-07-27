from django import forms
from django.conf import settings
import requests

class PlayerForm(forms.Form):
    players = forms.CharField(max_length=100)

    def search(self):
        result = {}
        players = self.cleaned_data['players']
        endpoint = 'https://www.haloapi.com/stats/h5/servicerecords/arena?players={players}[&seasonId]'
        url = endpoint.format(source_lang='en', word_id=word)
        headers = {'app_id': settings.Subscription_name, 'app_key': settings.key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:
                result['message'] = 'No entry found for "%s"' % players
            else:
                result['message'] = 'Gamer not available, try again later'
        return result
