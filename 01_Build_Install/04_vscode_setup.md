## Visual Studio Code Installation
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
```

## Link to GitHub Account
Note: This will open your browser for confirmation.  
Click "Source Control" and select "Clone Repository".  

## User Interface Settings
- View -> Appearance -> Sticky Scroll -> `Off`
- View -> Appearance -> MiniMap -> `Off`

## Extensions
- PlatformIO IDE
- ShellCheck
