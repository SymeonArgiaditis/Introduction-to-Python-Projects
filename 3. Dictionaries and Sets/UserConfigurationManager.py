test_settings = {
    'Theme': 'dark',
    'Notifications': 'enabled',
    'Volume': 'high'
}

#ADD SETTING
def add_setting(settings: dict, keyValue: tuple):
    
    key, value = keyValue
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings.update({key:value})
        return f"Setting '{key}' added with value '{value}' successfully!"

#UPDATE SETTING
def update_setting(settings: dict, keyValue: tuple):
    
    key, value = keyValue
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

#DELETE SETTING
def delete_setting(settings: dict, keyValue: tuple):
    
    key = keyValue
    key = key.lower()

    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

#Test #1
#print(delete_setting({'theme':'light'}, 'theme'))

#VIEW SETTINGS
def view_settings(settings: dict):
    if settings == {}:
        return "No settings available."
    else:
        result = "Current User Settings:\n" 
        for key, value in settings.items():
            result += f"{key.capitalize()}: {value}\n"

        return result
        
        #print(settings.items())

#Test #2
print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))
