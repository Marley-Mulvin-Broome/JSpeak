# JSpeak
<!-- TOC -->
* [JSpeak](#jspeak)
  * [Installation](#installation)
    * [AnkiWeb](#ankiweb)
    * [Manual](#manual)
  * [Usage](#usage)
    * [Editor](#editor)
    * [Browser](#browser)
    * [Preferences](#preferences)
      * [TTS Engine](#tts-engine)
      * [TTS Language](#tts-language)
        * [Google](#google)
<!-- TOC -->


JSpeak is a TTS (Text To Speech) generator for Anki.

## Installation

### AnkiWeb

This addon is **NOT YET** available on anki web. Please install it [manually](#manual).

### Manual

1. Download the latest release from the [releases page]() and extract it to your Anki addons folder.
2. Extract the zip file to your Anki addons folder. You can find this folder by going to Anki's preferences, then in the window that pops up, click the "Open Addons Folder" button.
3. Restart Anki.
4. **Done!**

## Usage

### Editor

1. Open a card in the editor.
2. Select the field, or highlight the text you want to generate audio of.
3. Click the Apple icon in the editor toolbar.
4. There will now be audio added to either one of the target fields from your preferences, or appended to the end of the selected field.

### Browser

**Not yet implemented**

### Preferences

JSpeak has a list of preferences you can edit in Anki. To access them in Anki, navigate to `Tools > Addons > JSpeak > Config.`

#### TTS Engine

This is the TTS engine that will be used to generate the audio. Currently, the only supported engine is `Google`.
Example: `"TTS Engine": "Google"`

#### TTS Language

This determines the language to be used when generating the audio.
To update the language, you must enter the corresponding language code or key, depending on the engine.
Example: `"TTS Language": "jp"`

##### Google

| **Code** | **Language**              |
|----------|---------------------------|
| af       | Afrikaans                 |
| ar       | Arabic                    |
| bg       | Bulgarian                 |
| bs       | Bosnian                   |
| ca       | Catalan                   |
| cs       | Czech                     |
| da       | Danish                    |
| de       | German                    |
| el       | Greek                     |
| en       | English                   |
| es       | Spanish                   |
| et       | Estonian                  |
| fi       | Finnish                   |
| fr       | French                    |
| hi       | Hindi                     |
| hr       | Croatian                  |
| hu       | Hungarian                 |
| id       | Indonesian                |
| is       | Icelandic                 |
| it       | Italian                   |
| iw       | Hebrew                    |
| ja       | Japanese                  |
| jw       | Javanese                  |
| km       | Khmer                     |
| ko       | Korean                    |
| la       | Latin                     |
| lv       | Latvian                   |
| ml       | Malayalam                 |
| mr       | Marathi                   |
| ms       | Malay                     |
| my       | Myanmar (Burmese)         |
| ne       | Nepali                    |
| nl       | Dutch                     |
| no       | Norwegian                 |
| pl       | Polish                    |
| pt       | Portuguese                |
| ro       | Romanian                  |
| ru       | Russian                   |
| si       | Sinhalese                 |
| sk       | Slovak                    |
| sq       | Albanian                  |
| sr       | Serbian                   |
| su       | Sundanese                 |
| sv       | Swedish                   |
| sw       | Swahili                   |
| ta       | Tamil                     |
| te       | Telugu                    |
| th       | Thai                      |
| tl       | Filipino                  |
| tr       | Turkish                   |
| uk       | Ukrainian                 |
| ur       | Urdu                      |
| vi       | Vietnamese                |
| zh       | Chinese (Mandarin)        |
| zh-CN    | Chinese (Simplified)      |
| zh-TW    | Chinese (Mandarin/Taiwan) |

**Note:** this may be incomplete, or be missing accents. If you find any errors, please submit a pull request or open an issue.
