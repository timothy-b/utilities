# Snippets

A big ol' fashioned pile of hacks, and some commands.

- [Snippets](#Snippets)
  - [Android](#Android)
    - [Disable vibration for an app](#Disable-vibration-for-an-app)
    - [Diagnosing phantom notifications](#Diagnosing-phantom-notifications)
  - [Bitcoin](#Bitcoin)
    - [Wallet password recovery](#Wallet-password-recovery)
  - [Docker](#Docker)
    - [Installing on Windows 10 non-Pro/Enterprise/Educational](#Installing-on-Windows-10-non-ProEnterpriseEducational)
      - [Dealing with that Powershell error](#Dealing-with-that-Powershell-error)

## Android

### Disable vibration for an app 
https://www.xda-developers.com/stop-vibrations-android-apps/

e.g., com.twitter.android

```bash
adb shell
cmd appops set com.twitter.android VIBRATE ignore
```
"You won’t see any confirmation in the prompt, but as long as you don’t get an error message it should have worked."

### Diagnosing phantom notifications
https://www.theverge.com/2018/10/19/18001608/android-notification-history-how-to-view

1. Long press anywhere on your home screen
2. Select widgets at the bottom of the screen
3. Scroll down and tap the “Settings shortcut” widget
4. Tap “Notification Log”
5. Place the widget on your home screen
6. Tap the widget and scroll through your past notifications

## Bitcoin

### Wallet password recovery
https://github.com/gurnec/btcrecover

Running straight against the wallet:
```cmd
python btcrecover.py --wallet forgotpw_wallet --autosave savefile --tokenlist tokens.txt
```

Extracting the vital info:
```cmd
python extract-scripts\extract-electrum2-partmpk.py forgotpw_wallet
```

Running against the vital info:
```cmd
python btcrecover.py --data-extract --autosave savefile --tokenlist tokens.txt
```

## Docker

`docker help`

`docker COMMAND --help`

### Installing on Windows 10 non-Pro/Enterprise/Educational

https://forums.docker.com/t/installing-docker-on-windows-10-home/11722/29
1. Open Regedit. 
2. Go to `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion`
3. Change the value of `EditionID` to `Professional`.
4. Change the value of `ProductName` to `Windows 10 Pro`.
5. Run the latest `Docker for Windows` installer.
6. Run the program to complete first-time setup.
7. Change the above registry keys back.

#### Dealing with that Powershell error
https://stackoverflow.com/questions/42950853/docker-the-computer-windows10-on-se-could-not-be-resolved/45099242#45099242

```
Unable to execute Start: Unable to create: The running command stopped because the preference variable "ErrorActionPreference" or common parameter is set to Stop:
```

Now restart docker and after restart completion execute following commands in dos admin mode to setup the network card manually

netsh interface ipv4 set address name="vEthernet (DockerNAT)" static 10.0.75.1 255.255.255.0

You have to run this command everytime whenever you are doing system restart and docker completes start process (due to any reason). TIP : create a batch file of this command and save somewhere handy.

Note: The ps hack would get undone by any docker update. so be aware...

**Hack**

Open C:\Program Files\Docker\Docker\resources\mobylinux.ps1 with any editor in admin mode. Find following code (around line 164)
```
$networkAdapter | Remove-NetIPAddress -Confirm:$false -ea SilentlyContinue

$networkAdapter | Set-NetIPInterface -Dhcp Disabled -ea SilentlyContinue

$networkAdapter | New-NetIPAddress -AddressFamily IPv4 -IPAddress $switchAddress -PrefixLength ($SwitchSubnetMaskSize) -ea Stop | Out-Null
```

Add a return after line 165 in a new line like below and save the file.

```
$networkAdapter | Remove-NetIPAddress -Confirm:$false -ea SilentlyContinue

$networkAdapter | Set-NetIPInterface -Dhcp Disabled -ea SilentlyContinue

return

$networkAdapter | New-NetIPAddress -AddressFamily IPv4 -IPAddress $switchAddress -PrefixLength ($SwitchSubnetMaskSize) -ea Stop | Out-Null
```

Now restart docker and after restart completion execute following commands in dos admin mode to setup the network card manually

```cmd
netsh interface ipv4 set address name="vEthernet (DockerNAT)" static 10.0.75.1 255.255.255.0
```

You have to run this command everytime whenever you are doing system restart and docker completes start process (due to any reason). TIP : create a batch file of this command and save somewhere handy.

Note: The ps hack would get undone by any docker update. so be aware...
