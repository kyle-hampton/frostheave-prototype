from django import forms
from django.conf import settings
import requests

class PlayerForm(forms.Form):
    player = forms.CharField(max_length=100)

    def search(self):
        result = {}
        form = self.cleaned_data['form']
        endpoint = 'https://www.haloapi.com/stats/h5/servicerecords/arena?players={players}[&seasonId]'
        url = endpoint.format(source_lang='en', form_id=form)
        headers = {'Ocp-Apim-Subscription-Key': '92a2365131bb451e9cf5fc960ba1df22'}
        response = requests.get(url, headers)
        if response.status_code == 200:
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:
                result['message'] = 'No entry found for "%s"' % form
            else:
                result['message'] = 'Gamer not available, try again later'
        return result
