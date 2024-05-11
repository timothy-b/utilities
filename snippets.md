# Snippets

A big ol' fashioned pile of hacks, and some commands.

- [Snippets](#snippets)
  - [Android](#android)
    - [Disable vibration for an app](#disable-vibration-for-an-app)
    - [Diagnosing phantom notifications](#diagnosing-phantom-notifications)
  - [Bitcoin](#bitcoin)
    - [Wallet password recovery](#wallet-password-recovery)
  - [Docker](#docker)
    - [Installing on Windows 10 non-Pro/Enterprise/Educational](#installing-on-windows-10-non-proenterpriseeducational)
      - [Dealing with that Powershell error](#dealing-with-that-powershell-error)
  - [Powershell](#powershell)
  - [Raspberry Pi](#raspberry-pi)
  - [Linux](#linux)
    - [Sway](#sway)
      - [cheatsheet:](#cheatsheet)
      - [enabling numlock on boot](#enabling-numlock-on-boot)
      - [setting up monitors](#setting-up-monitors)
      - [running X apps as root](#running-x-apps-as-root)
      - [Setting the login background](#setting-the-login-background)
    - [Firefox / Pale Moon / LibreWolf / FireDragon](#firefox--pale-moon--librewolf--firedragon)
      - [enabling middle mouse scroll](#enabling-middle-mouse-scroll)
      - [Enabling scrollable tabs via mouse wheel](#enabling-scrollable-tabs-via-mouse-wheel)
      - [fixing downloads](#fixing-downloads)
    - [setting permanent mount point for hard drive](#setting-permanent-mount-point-for-hard-drive)
    - [fan control](#fan-control)
    - [proton](#proton)
  - [Windows](#windows)
    - [Disabling auto-wake-up scheduled task](#disabling-auto-wake-up-scheduled-task)

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

## Powershell

`ssh-keygen`

## Raspberry Pi

```bash
raspi-config

raspistill -v -o test.jpg

vcgencmd get_camera
```

## Linux

### Alacritty

#### Fix config errors
_[WARN] see log at /tmp/Alacritty-2994.log ($ALACRITTY_LOG): Unused config key: colors.footer_bar_

`alacritty migrate`

Then comment out obsolete properties until errors stop showing from `~/.config/alacritty/alacritty.toml`. Repeat for dynamic_padding and window.opacity.

### Garuda
#### If Add/Remove Software doesn't show up as a menu option
```pacman -Syu pamac-aur```

### Sway

#### cheatsheet:

https://wiki.garudalinux.org/en/sway-cheatsheet

#### Enabling numlock on boot

https://wiki.archlinux.org/title/Sway#Initially_enable_CapsLock/NumLock

edit `.config/sway/config.d/input`

append `input type:keyboard xkb_numlock enabled`

#### Setting up monitors
Use `wdisplays` ("Displays") to arrange monitors.


Then `swaymst -t get_outputs` to get current config.

Then edit `~/.config/sway/config.d/output`.

my config:
```
output DP-1 mode 2560x1440@154Hz position 1440 0
output HDMI-A-1 resolution 1440x900 position 0 540
```

#### Running X apps as root

Make sure the output of `pgrep -af polkit` indicates that you have a polkit daemon & agent running:
```bash
883 /usr/lib/polkit-1/polkitd --no-debug
2122 /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1
```

Then try:

`xhost si:localuser:root`

Without this, you'll see errors like:

```bash
Authorization required, but no authorization protocol specified

qt.qpa.xcb: could not connect to display :0
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, xcb.

fish: Job 1, 'sudo garuda-boot-options' terminated by signal SIGABRT (Abort)
```

If that doesn't do the trick, e.g, pacmac-manager is silently not able to install from AUR, then create `~/.config/environment.d/.conf` with contents:
```
DISPLAY=:0
WAYLAND_DISPLAY=wayland-0
```
and reboot. See https://github.com/keybase/client/issues/19614 for details.

Docker (and specifically containerd) can also cause polkit issues. Try disabling docker, docker.socket, and containerd. See https://bbs.archlinux.org/viewtopic.php?id=284158&p=2 for details.


#### Setting the login background
Set `Background = none` in `/etc/qtgreet/config.ini`

#### Set desktop background
https://wiki.archlinux.org/title/Sway#Wallpaper

#### Fix all workspaces being displayed on all monitors
Edit `~/.config/waybar/config`

Set `"all-outputs": false`

#### Set default web browser
Edit `~/.profile`
Set `BROWSER=brave`

Edit `~/.config/sway/config.d/default`
`set bindsym $mod+o exec firedragon` -> `set bindsym $mod+o exec brave`

#### Setting the lockscreen background

Edit `~/.config/swaylock/config`
Change `image=`

#### Change lock binding to Ctrl+Win+l
Edit `.config/sway/config.d/default`

Under `Lock Screen`, append `bindsym $mod+Ctrl+l exec ~/.config/sway/scripts/lockman.sh`

#### Move between workspaces like Windows virtual desktops
Edit `~/.config/sway/config.d/default`
Add:
```
bindsym Ctrl+$mod+Left workspace prev
bindsym Ctrl+$mod+Right workspace next
```

#### Open calculator with keyboard key

Edit `~/.config/sway/config.d/default`
Add `bindsym XF86Calculator exec gnome-calculator`

To make it float instead of tile:
Edit `~/.config/sway/config.d/application_defaults`
Add `for_window [app_id="Calculator"] floating enable`

### Firefox / Pale Moon / LibreWolf / FireDragon

#### Enabling middle mouse scroll
https://wiki.gentoo.org/wiki/Firefox#Middle_mouse_scroll_.28autoscroll.29

##### on Brave:
https://chromewebstore.google.com/detail/autoscroll/occjjkgifpmdgodlplnacmkejpdionan

#### Enabling scrollable tabs via mouse wheel

Go to `about:config`, search for `toolkit.tabbox.switchByScrolling`, set to true.

#### Fixing downloads

https://www.reddit.com/r/LibreWolf/comments/103gqhc/librewolf_does_not_save_anything/

### Setting permanent mount point for hard drive

https://github.com/ValveSoftware/Proton/wiki/Using-a-NTFS-disk-with-Linux-and-Windows

1. get user ID with `id -u`
2. get group ID with `id -g`
3. get disk partition with `fdisk -l`
4. get UUID with `blkid`
5. edit /etc/fstab with entry like so:
   `UUID=38CE9483CE943AD8 /media/gamedisk ntfs uid=1000,gid=1000,rw,user,exec,umask=000 0 0`

### Fan control

https://github.com/Eraden/amdgpud

_available in AUR_

- monitor GPU temp & fan speed with `amdmond watch --format short`
- edit control matrix at `/etc/amdfand/config.toml`
- apply changes with `amdfand service`

### Proton

Install Steam and then `protonup-qt-bin`, get latest GE version.

### Reinstalling Grub when it breaks
From liveusb, mount encrypted drive:

https://forums.opensuse.org/t/how-do-you-mount-an-encrypted-drive-from-the-command-line/135136

`fdisk -l` to find drive, partition, & boot partition

```bash
mkdir /mnt
mkdir /mnt/garuda
cryptsetup luksOpen /dev/nvme0n1p4 garuda
mount /dev/mapper/garuda /mnt/garuda
```

Then chroot & reinstall Grub:

https://forum.garudalinux.org/t/grub-fails-after-update/78

```sh
garuda-chroot /mnt/garuda/@ #chroot in
mount /dev/nvme0n1p5 /boot/efi #mount boot partition
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=garuda --recheck #install Grub
update-grub #update Grub
exit
```

## Windows

### Disabling auto-wake-up scheduled task

powercfg /lastwake

https://answers.microsoft.com/en-us/windows/forum/all/no-permission-to-disable-a-task-in-task-scheduler/4ec2c460-7c2f-4593-b84f-c9b1687ae797

https://download.sysinternals.com/files/PSTools.zip

psexec.exe -i -s %windir%\system32\mmc.exe /s taskschd.msc

