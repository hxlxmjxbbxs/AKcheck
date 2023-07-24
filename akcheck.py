import os
import requests
import argparse
import json
import base64
import ctypes

FOREGROUND_BLUE = 0x0001
FOREGROUND_GREEN = 0x0002
FOREGROUND_RED = 0x0004
FOREGROUND_INTENSITY = 0x0008
FOREGROUND_WHITE = FOREGROUND_BLUE | FOREGROUND_GREEN | FOREGROUND_RED

def set_console_color(color):
    std_handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.SetConsoleTextAttribute(std_handle, color)

try:
    import colorama
    colorama.init()
    from colorama import Fore, Style  # Add this line to import Fore and Style
except ImportError:
    pass

def print_banner():
    banner = r"""
    █████  ██   ██  ██████ ██   ██ ███████  ██████ ██   ██ 
    ██   ██ ██  ██  ██      ██   ██ ██      ██      ██  ██  
    ███████ █████   ██      ███████ █████   ██      █████   
    ██   ██ ██  ██  ██      ██   ██ ██      ██      ██  ██  
    ██   ██ ██   ██  ██████ ██   ██ ███████  ██████ ██   ██ 
                                                            

    Author: hxlxmjxbbxs
    Github: https://github.com/hxlxmjxbbxs
    Released: 2023/07/23
    """
    print(banner)

# Check if the OS is Windows and if colorama is not already initialized
if os.name == "nt" and not os.getenv("ANSICON"):
    os.system("color")

def check_api_key(url, headers=None, params=None):
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False

def check_google_geolocation_api_key(api_key):
    url = "https://www.googleapis.com/geolocation/v1/geolocate"
    params = {
        "key": api_key
    }
    return check_api_key(url)

def check_google_cloud_service_account_credentials(api_key):
    try:
        service_account_info = json.loads(api_key)
        if (
            "client_email" in service_account_info and "private_key" in service_account_info
        ):
            return True
        else:
            return False
    except json.JSONDecodeError:
        return False

def check_buildkite_access_token(api_key):
    url = "https://api.buildkite.com/v2/user"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    return check_api_key(url, headers=headers)

def check_buttercms_api_key(api_key):
    url = f"https://api.buttercms.com/v2/posts/?auth_token={api_key}"
    return check_api_key(url)

def check_asana_access_token(api_key):
    url = "https://app.asana.com/api/1.0/users/me"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    return check_api_key(url, headers=headers)

def check_branch_io_key_and_secret(api_key):
    if ":" in api_key:
        return True
    else:
        return False

def check_bitly_access_token(api_key):
    url = "https://api-ssl.bitly.com/v4/user"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    return check_api_key(url, headers=headers)

def check_mailchimp_api_key(api_key):
    if "-" not in api_key:
        return False

    datacenter = api_key.split("-")[1]

    url = f"https://{datacenter}.api.mailchimp.com/3.0/"
    headers = {
        "Authorization": f"OAuth {api_key}"
    }

    return check_api_key(url, headers=headers)


def check_wpengine_api_key(api_key):
    url = "https://api.wpengineapi.com/v1/installs"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    return check_api_key(url, headers=headers)

def check_datadog_api_key(api_key):
    url = "https://api.datadoghq.com/api/v1/validate"
    headers = {
        "DD-API-KEY": api_key
    }
    return check_api_key(url, headers=headers)

def check_delighted_api_key(api_key):
    url = "https://api.delighted.com/v1/people.json"
    headers = {
        "Authorization": f"Basic {api_key}"
    }
    return check_api_key(url, headers=headers)

def check_travis_ci_api_token(api_key):
    url = "https://api.travis-ci.org/user"
    headers = {
        "Authorization": f"token {api_key}"
    }
    return check_api_key(url, headers=headers)

def check_wakatime_api_key(api_key):
    url = "https://wakatime.com/api/v1/users/current"
    headers = {
        "Authorization": f"Basic {api_key}"
    }
    return check_api_key(url, headers=headers)

def check_sonarcloud_token(api_key):
    url = "https://sonarcloud.io/api/user_tokens/search"
    headers = {
        "Authorization": f"Basic {api_key}"
    }
    return check_api_key(url, headers=headers)

def check_spotify_access_token(api_key):
    url = "https://api.spotify.com/v1/me"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    return check_api_key(url, headers=headers)

def check_instagram_access_token(api_key):
    url = f"https://graph.instagram.com/me?fields=id,username&access_token={api_key}"
    return check_api_key(url)

def check_instagram_graph_api_access_token(api_key):
    url = f"https://graph.instagram.com/me?fields=id,username&access_token={api_key}"
    return check_api_key(url)

def check_paypal_client_id_and_secret_key(api_key):
    if ":" in api_key:
        return True
    else:
        return False

def check_stripe_live_token(api_key):
    url = "https://api.stripe.com/v1/charges"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    return check_api_key(url, headers=headers)

def check_razorpay_key_and_secret(api_key):
    if ":" in api_key:
        return True
    else:
        return False

def check_circleci_access_token(api_key):
    url = "https://circleci.com/api/v1.1/me"
    headers = {
        "Circle-Token": api_key
    }
    return check_api_key(url, headers=headers)

def check_npm_token(api_key):
    url = "https://registry.npmjs.org/-/npm/v1/user"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    return check_api_key(url, headers=headers)

def check_opsgenie_api_key(api_key):
    url = "https://api.opsgenie.com/v2/users/me"
    headers = {
        "Authorization": f"GenieKey {api_key}"
    }
    return check_api_key(url, headers=headers)

def check_keen_io_api_key(api_key):
    url = "https://api.keen.io/3.0/projects"
    headers = {
        "Authorization": api_key
    }
    return check_api_key(url, headers=headers)

def check_calendly_api_key(api_key):
    url = "https://api.calendly.com/v1/users/me"
    headers = {
        "Authorization": f"Token {api_key}"
    }
    return check_api_key(url, headers=headers)

def check_azure_app_id_and_api_key(api_key):
    if ":" in api_key:
        return True
    else:
        return False

def check_youtube_api_key(api_key):
    url = "https://www.googleapis.com/youtube/v3/channels"
    params = {
        "part": "snippet",
        "mine": "true",
        "key": api_key
    }
    return check_api_key(url)

def check_iterable_api_key(api_key):
    url = "https://api.iterable.com/api/users/getFields"
    headers = {
        "Api-Key": api_key
    }
    return check_api_key(url, headers=headers)

def check_visual_studio_app_center_api_token(api_key):
    url = "https://api.appcenter.ms/v0.1/user"
    headers = {
        "X-API-Token": api_key
    }
    return check_api_key(url, headers=headers)

def check_weglot_api_key(api_key):
    url = "https://api.weglot.com/v3/status"
    headers = {
        "api_key": api_key
    }
    return check_api_key(url, headers=headers)

def check_pivotaltracker_api_token(api_key):
    url = "https://www.pivotaltracker.com/services/v5/me"
    headers = {
        "X-TrackerToken": api_key
    }
    return check_api_key(url, headers=headers)

def check_linkedin_oauth(api_key):
    url = "https://api.linkedin.com/v2/me"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    return check_api_key(url, headers=headers)

def check_help_scout_oauth(api_key):
    url = "https://api.helpscout.net/v2/users/me"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    return check_api_key(url, headers=headers)

def check_shodan_api_key(api_key):
    url = f"https://api.shodan.io/api-info?key={api_key}"
    return check_api_key(url)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = "Check if an API key is valid.")
parser.add_argument("--key", type = str, required = True, help = "The API key to check.")

args = parser.parse_args()
api_key = args.key

print_banner()

if check_google_geolocation_api_key(api_key):
	print(Fore.GREEN + "The Google Geolocation API key is valid." + Style.RESET_ALL)
else :
	print("The Google Geolocation API key is not valid.")

if check_google_cloud_service_account_credentials(api_key):
	print(Fore.GREEN + "The Google Cloud Service Account credentials are valid." + Style.RESET_ALL)
else :
	print("The Google Cloud Service Account credentials are not valid.")

if check_buildkite_access_token(api_key):
	print(Fore.GREEN + "The Buildkite access token is valid." + Style.RESET_ALL)
else :
	print("The Buildkite access token is not valid.")

if check_buttercms_api_key(api_key):
	print(Fore.GREEN + "The ButterCMS API key is valid." + Style.RESET_ALL)
else :
	print("The ButterCMS API key is not valid.")

if check_asana_access_token(api_key):
	print(Fore.GREEN + "The Asana access token is valid." + Style.RESET_ALL)
else :
	print("The Asana access token is not valid.")

if check_branch_io_key_and_secret(api_key):
	print(Fore.GREEN + "The Branch.IO key and secret are valid." + Style.RESET_ALL)
else :
	print("The Branch.IO key and secret are not valid.")

if check_bitly_access_token(api_key):
	print(Fore.GREEN + "The Bit.ly access token is valid." + Style.RESET_ALL)
else :
	print("The Bit.ly access token is not valid.")
    
if check_mailchimp_api_key(api_key):
	print(Fore.GREEN + "The MailChimp API key is valid." + Style.RESET_ALL)
else :
	print("The MailChimp API key is not valid.")

if check_wpengine_api_key(api_key):
	print(Fore.GREEN + "The WPEngine API key is valid." + Style.RESET_ALL)
else :
	print("The WPEngine API key is not valid.")

if check_datadog_api_key(api_key):
	print(Fore.GREEN + "The DataDog API key is valid." + Style.RESET_ALL)
else :
	print("The DataDog API key is not valid.")

if check_delighted_api_key(api_key):
	print(Fore.GREEN + "The Delighted API key is valid." + Style.RESET_ALL)
else :
	print("The Delighted API key is not valid.")

if check_travis_ci_api_token(api_key):
	print(Fore.GREEN + "The Travis CI API token is valid." + Style.RESET_ALL)
else :
	print("The Travis CI API token is not valid.")

if check_wakatime_api_key(api_key):
	print(Fore.GREEN + "The WakaTime API key is valid." + Style.RESET_ALL)
else :
	print("The WakaTime API key is not valid.")

if check_sonarcloud_token(api_key):
	print(Fore.GREEN + "The Sonarcloud Token is valid." + Style.RESET_ALL)
else :
	print("The Sonarcloud Token is not valid.")

if check_spotify_access_token(api_key):
	print(Fore.GREEN + "The Spotify Access Token is valid." + Style.RESET_ALL)
else :
	print("The Spotify Access Token is not valid.")

if check_instagram_access_token(api_key):
	print(Fore.GREEN + "The Instagram Basic Display API Access Token is valid." + Style.RESET_ALL)
else :
	print("The Instagram Basic Display API Access Token is not valid.")

if check_instagram_graph_api_access_token(api_key):
	print(Fore.GREEN + "The Instagram Graph API Access Token is valid." + Style.RESET_ALL)
else :
	print("The Instagram Graph API Access Token is not valid.")

if check_paypal_client_id_and_secret_key(api_key):
	print(Fore.GREEN + "The Paypal client id and secret key are valid." + Style.RESET_ALL)
else :
	print("The Paypal client id and secret key are not valid.")

if check_stripe_live_token(api_key):
	print(Fore.GREEN + "The Stripe Live Token is valid." + Style.RESET_ALL)
else :
	print("The Stripe Live Token is not valid.")

if check_razorpay_key_and_secret(api_key):
	print(Fore.GREEN + "The Razorpay API key and secret are valid." + Style.RESET_ALL)
else :
	print("The Razorpay API key and secret are not valid.")

if check_circleci_access_token(api_key):
	print(Fore.GREEN + "The CircleCI access token is valid." + Style.RESET_ALL)
else :
	print("The CircleCI access token is not valid.")

if check_npm_token(api_key):
	print(Fore.GREEN + "The NPM token is valid." + Style.RESET_ALL)
else :
	print("The NPM token is not valid.")

if check_opsgenie_api_key(api_key):
	print(Fore.GREEN + "The OpsGenie API key is valid." + Style.RESET_ALL)
else :
	print("The OpsGenie API key is not valid.")

if check_keen_io_api_key(api_key):
	print(Fore.GREEN + "The Keen.io API key is valid." + Style.RESET_ALL)
else :
	print("The Keen.io API key is not valid.")

if check_calendly_api_key(api_key):
	print(Fore.GREEN + "The Calendly API key is valid." + Style.RESET_ALL)
else :
	print("The Calendly API key is not valid.")

if check_azure_app_id_and_api_key(api_key):
	print(Fore.GREEN + "The Azure Application Insights APP ID and API key are valid." + Style.RESET_ALL)
else :
	print("The Azure Application Insights APP ID and API key are not valid.")

if check_youtube_api_key(api_key):
	print(Fore.GREEN + "The YouTube API key is valid." + Style.RESET_ALL)
else :
	print("The YouTube API key is not valid.")

if check_iterable_api_key(api_key):
	print(Fore.GREEN + "The Iterable API key is valid." + Style.RESET_ALL)
else :
	print("The Iterable API key is not valid.")

if check_visual_studio_app_center_api_token(api_key):
	print(Fore.GREEN + "The Visual Studio App Center API token is valid." + Style.RESET_ALL)
else :
	print("The Visual Studio App Center API token is not valid.")

if check_weglot_api_key(api_key):
	print(Fore.GREEN + "The WeGlot API key is valid." + Style.RESET_ALL)
else :
	print("The WeGlot API key is not valid.")

if check_pivotaltracker_api_token(api_key):
	print(Fore.GREEN + "The PivotalTracker API token is valid." + Style.RESET_ALL)
else :
	print("The PivotalTracker API token is not valid.")

if check_linkedin_oauth(api_key):
	print(Fore.GREEN + "The LinkedIn OAUTH is valid." + Style.RESET_ALL)
else :
	print("The LinkedIn OAUTH is not valid.")

if check_help_scout_oauth(api_key):
	print(Fore.GREEN + "The Help Scout OAUTH is valid." + Style.RESET_ALL)
else :
	print("The Help Scout OAUTH is not valid.")

if check_shodan_api_key(api_key):
	print(Fore.GREEN + "The Shodan API key is valid." + Style.RESET_ALL)
else :
	print("The Shodan API key is not valid.")
