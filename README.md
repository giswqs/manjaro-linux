# manjaro-linux

[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Shell scripts for setting up [Manjaro Linux](https://manjaro.org/get-manjaro/) for Python programming and deep learning**

Author: Qiusheng Wu (<https://wetlands.io>)

## How to use these shell scripts?

- Open the Terminal and enter the following commands
- git clone <https://github.com/giswqs/manjaro-linux.git>
- cd manjaro-linux
- sh shell-script-file (e.g., sh 01-update-mirrors)

## My favorite apps:

- Package manager: pamac (enable AUR)
- Backup: timeshift
- Dist utility: gnome-disk-utility (for auto mount options)
- System cleaner: stacer-bin
- Workspace theme: arc-kde papirus-icon-theme papirus-maia-icon-theme
- Browser: google-chrome brave
- Programming: visual-studio-code-bin r rstudio-desktop-bin pycharm-professional miniconda3 cuda cudnn python-tensorflow-cuda
- Office Suite: softmaker-office-2018-bin
- Cloud backup: dropbox insync onedrive
- Remote desktop: teamviewer anydesk nomachine krdc remmina
- FTP client: filezilla
- Email clients: mailspring wavebox
- ISO files: etcher furiusisomount xfburn, woeusb
- Image editor: gimp pinta krita
- Vector editor: inkscape
- Screen recorder: peek flameshot obs-studio
- PDF editor: masterpdfeditor-free gscan2pdf pdfarranger moonshiner pdfchain
- Chat: skypeforlinux-stable-bin electronic-wechat zoom slack-desktop
- Wallpaper: variety
- Pandora Radio client: pithos
- Media server: plex-media-server rhythmbox
- E-book reader: calibre
- Virtual machine: virtualbox crossover
- Firewall: gufw
- System info: hardinfo
- Math: mathpix-snipping-tool
- Geospatial: google-earth qgis saga-gis
- Download manager: motrix

## Installation

Choose erase disk and the BTRFS file system.

## Settings

- Enter BIOS to change boot order to boot from USB first
- Power settings: System Settings > Power Management > Suspend when inactive for > Do nothing
- Keyboard settings: System Settings > Keyboard > Numlock on startup: Turn on
- Choose Breath Dark theme: System Settings >Quick Settings >Breath Dark
- Disable log out confirmation: System Settings >System >Session >Desktop Sesssion >Uncheck "Ask for confirmation" >On login, Start with an empty session
- Enable AUR: Pamac >Preferences >Third Party >Enable AUR support > Check for updates
- Change terminal shortcut: Konslole >Settings >Configure Keyboard Shortcuts > Search Paster >Custom Shortcut >Ctrl+V

## Start Rustdesk

Start rustdesk before login

```bash
kate /etc/systemd/system/rustdesk.service
```

Paste the following content

```text
[Unit]
Description=RustDesk Remote Desktop
After=network.target

[Service]
ExecStart=/usr/bin/rustdesk --service
Restart=always
User=root
Environment=DISPLAY=:0

[Install]
WantedBy=multi-user.target
```

Then run the following commands

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable rustdesk
sudo systemctl start rustdesk
```

Then run

```bash
sudo systemctl status rustdesk
```
