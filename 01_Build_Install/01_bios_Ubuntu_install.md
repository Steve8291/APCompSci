# BIOS & Ubuntu Install
- Remove BIOS password if necessary by removing the jumper and rebooting
- Enter BIOS
    - BIOS/System Setup: `F2` or `Del`
    - Boot Menu: `F12`
- Make the following changes in BIOS:
    - General -> Boot Sequence -> UEFI (note if there are problems with install, temporarily switch to "Legacy")
    - Date/Time (set the date and time)
    - System Configuration -> SATA Operation -> ACHI (this is the only way to disable RST which Ubuntu requires)
    - System Configuration -> Smart Reporting -> Enable

- Insert jump drive, enter boot menu and install Ubuntu

Note: If you need to change the boot order in BIOS to make the usb drive first choose the "USB-HDD" option

Note: if the computer fails to boot the next time you poweroff it might have reverted back to Legacy mode in the BIOS. This is likely due to a dead CMOS battery on the motherboard. A good battery will test >= 2.8V

# Ubuntu Noble Numbat 24.04 Notes

## Firmware Updates
[Linux Vendor Firmware Service](https://fwupd.org/)
```bash
fwupdmgr get-devices # List devices with fwupd support
fwupdmgr refresh # Download fwupd metadata
fwupdmgr get-updates
```

## Update Ubuntu:
```bash
sudo apt update && apt upgrade
sudo snap refresh
```

## Install Apps
```bash
sudo apt install plocate

sudo snap install opera
```

## UI Tweaks
- Getting around inside Ubuntu
- Add Terminal to Bookmarks bar
- Auto hide bookmarks bar
- System Settings -> Appearance -> Style -> Dark
- System Settings -> Ubuntu Desktop -> Dock -> Auto-hide the Dock

## Firewall
```bash
sudo ufw enable
```

## Enable Source Highlighting in `less`
```bash
sudo apt install source-highlight
echo 'export LESSOPEN="| /usr/share/source-highlight/src-hilite-lesspipe.sh %s"' >> ~/.bashrc
echo "export LESS=' -cR '" >> ~/.bashrc
source ~/.bashrc
```

## Visual Studio Code
```bash
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/keyrings/packages.microsoft.gpg
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" | sudo tee /etc/apt/sources.list.d/vscode.list
sudo apt update
sudo apt install code
```

## Install & Configure git
```bash
sudo apt install git
git config --global user.name "Your Git UserName"
git config --global user.email "Your Git Email"