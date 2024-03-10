# Sigma_conversion_to_all

This project helps you visualize the power of Sigma Rules empowered by SigmAIQ to convert them to the supported SIEM language of your choice. This project also aims to standardize Detection-as-Code (DAC) practices.

## Description

Sigma Rules are becoming increasingly popular due to their simple design. The wrapper class, SigmAIQ, helps simplify the usage of PySigma to translate any Sigma rule to the designated SIEM language.

## Syntax
* SigmaHQ
    * A popular open-source project aimed at simplifying detection analytics by using YARA-like text (Sigma rules) to convert to any SIEM Language.
* Backend
    * Backends are SIEM engines supported by Sigma rules.
* Pipeline
    * Pipelines are formats supported by Backends. They help format the query language; sysmon, windows, etc.
* PySigma
    * Module to convert YARA rules.
* SigmAIQ
    * A wrapper class that helps you utilize PySigma to program detection analytics via Detection-as-Code practices.

## Prerequisite
Download the latest sigma repository from [SigmaHQ](https://github.com/SigmaHQ/sigma).

## Sigma Conversion To All
This script searches for a key string in the Sigma rules repository and copies them to a destination folder to translate the Sigma YARA rule into all available backends and pipelines. The intention is to understand the power of Sigma rules' conversion to most supported SIEM query languages.

## Sample Output
```shell
hyunwookim@Hyuns-MBP-2 Sigma_conversion_to_all % python3 ./sigma_conversion_all.py 
Enter the directory where you wish to copy contents from: /Users/hyunwookim/Desktop/sigma/sigma/rules/windows/process_creation
Whats the key string you are looking for?: base64
Enter the new directory you wish to copy to: /Users/hyunwookim/Desktop/Your_Folder_Here                          
File 'proc_creation_win_powershell_base64_wmi_classes.yml' is copied to '/Users/hyunwookim/Desktop/Your_Folder_Here'
File 'proc_creation_win_powershell_base64_frombase64string.yml' is copied to '/Users/hyunwookim/Desktop/Your_Folder_Here'
File 'proc_creation_win_susp_inline_base64_mz_header.yml' is copied to '/Users/hyunwookim/Desktop/Your_Folder_Here'
File 'proc_creation_win_powershell_base64_reflection_assembly_load.yml' is copied to '/Users/hyunwookim/Desktop/Your_Folder_Here'
File 'proc_creation_win_powershell_base64_hidden_flag.yml' is copied to '/Users/hyunwookim/Desktop/Your_Folder_Here'
File 'proc_creation_win_powershell_base64_encoded_cmd.yml' is copied to '/Users/hyunwookim/Desktop/Your_Folder_Here'
File 'proc_creation_win_powershell_frombase64string.yml' is copied to '/Users/hyunwookim/Desktop/Your_Folder_Here'
File 'proc_creation_win_powershell_base64_invoke.yml' is copied to '/Users/hyunwookim/Desktop/Your_Folder_Here'
File 'proc_creation_win_powershell_base64_encoded_cmd_patterns.yml' is copied to '/Users/hyunwookim/Desktop/Your_Folder_Here'
File 'proc_creation_win_powershell_base64_encoded_obfusc.yml' is copied to '/Users/hyunwookim/Desktop/Your_Folder_Here'
File 'proc_creation_win_powershell_base64_iex.yml' is copied to '/Users/hyunwookim/Desktop/Your_Folder_Here'
File 'proc_creation_win_powershell_frombase64string_archive.yml' is copied to '/Users/hyunwookim/Desktop/Your_Folder_Here'
File 'proc_creation_win_powershell_base64_mppreference.yml' is copied to '/Users/hyunwookim/Desktop/Your_Folder_Here'
File 'proc_creation_win_powershell_base64_reflection_assembly_load_obfusc.yml' is copied to '/Users/hyunwookim/Desktop/Your_Folder_Here'
Translated rule saved to /Users/hyunwookim/Desktop/Your_Folder_Here/translated_proc_creation_win_powershell_base64_wmi_classes.yml
Translated rule saved to /Users/hyunwookim/Desktop/Your_Folder_Here/translated_proc_creation_win_powershell_base64_frombase64string.yml
Translated rule saved to /Users/hyunwookim/Desktop/Your_Folder_Here/translated_proc_creation_win_susp_inline_base64_mz_header.yml
Translated rule saved to /Users/hyunwookim/Desktop/Your_Folder_Here/translated_proc_creation_win_powershell_base64_reflection_assembly_load.yml
Translated rule saved to /Users/hyunwookim/Desktop/Your_Folder_Here/translated_proc_creation_win_powershell_base64_hidden_flag.yml
Translated rule saved to /Users/hyunwookim/Desktop/Your_Folder_Here/translated_proc_creation_win_powershell_base64_encoded_cmd.yml
Translated rule saved to /Users/hyunwookim/Desktop/Your_Folder_Here/translated_proc_creation_win_powershell_frombase64string.yml
Translated rule saved to /Users/hyunwookim/Desktop/Your_Folder_Here/translated_proc_creation_win_powershell_base64_invoke.yml
Translated rule saved to /Users/hyunwookim/Desktop/Your_Folder_Here/translated_proc_creation_win_powershell_base64_encoded_cmd_patterns.yml
Translated rule saved to /Users/hyunwookim/Desktop/Your_Folder_Here/translated_proc_creation_win_powershell_base64_encoded_obfusc.yml
Translated rule saved to /Users/hyunwookim/Desktop/Your_Folder_Here/translated_proc_creation_win_powershell_base64_iex.yml
Translated rule saved to /Users/hyunwookim/Desktop/Your_Folder_Here/translated_proc_creation_win_powershell_frombase64string_archive.yml
Translated rule saved to /Users/hyunwookim/Desktop/Your_Folder_Here/translated_proc_creation_win_powershell_base64_mppreference.yml
Translated rule saved to /Users/hyunwookim/Desktop/Your_Folder_Here/translated_proc_creation_win_powershell_base64_reflection_assembly_load_obfusc.yml
hyunwookim@Hyuns-MBP-2 Sigma_conversion_to_all % 
```
## Future Updates
I plan to explore SigmAIQ's LLM model to write detections in English language and convert them into any SIEM language.