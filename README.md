This Was my CS50 Final project. I have not changed names or formatting of the readme. I may do so in the future when I improve on the code.   
   
   # ntfyweather
    #### Description: A weather app that sends push notifications through the NTFY application. It is intended to be run in a cron job.

    First off, I want to give credit to both the makers of the NTFY applicaiton and the makers of the three free to use API's used for this this script: Zippopotamus, the Time API, and the Open Meteo API. Please see their websites below for information on usage.
    https://open-meteo.com/
    https://api.zippopotam.us/
    https://timeapi.io


    This script creates a dictionary with several blank fields, then gives the dictionary to several functions that return the dictionary with information appended. This is not the ultimate design of the application, and further revisions should be coming where dictionary will be removed in favor of a class.

    When running the script, you must supply two command line arguments. The first should be a 5 digit valid zip code. If the supplied argument is not 5 digits, the script will exit with an error. If the zip is 5 digits but it is not a valid zip, it will call the API, and return a non 200 response. If this response if given on any API call, the script will exit with errors. The second command line argument should be the URL or IP of the NTFY server in question. Per the requirement of the NTFY push through python found on their website, the command line input will require the HTTP or HTTPS header and will require a topic after the URL and after a forward slash. This topic is case sensitive. The only error checking on this input is requiring the header and a forward slash on the end, followed by some sort of input. I pursued error checking the server through PyPing or other functions, but nothing seemed to fit well. Instead, if the user does not enter a valid URL and topic that still gets past the requirements, the script will run but the end of the script will mention that if the notification was not received, to check the URL and try again.


