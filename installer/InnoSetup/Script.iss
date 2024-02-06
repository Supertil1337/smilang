; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Smilang"
#define MyAppVersion "1.0"
#define MyAppPublisher "Tilmann Prechtl"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{9A454F3C-FB90-4C29-B6DA-8067FEBE90CE}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DisableDirPage=yes
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\tilma\Documents\GitHub\esolang\installer\InnoSetup
OutputBaseFilename=mysetup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "german"; MessagesFile: "compiler:Languages\German.isl"

[Icons]
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"

[Files]
Source: "C:\Users\tilma\Documents\GitHub\esolang\build\main.exe"; DestDir: {app}
Source: "C:\Users\tilma\Documents\GitHub\esolang\build\converter.exe"; DestDir: {app}
Source: "C:\Users\tilma\Documents\GitHub\esolang\installer\register.bat"; DestDir: {app}

;[Registry]
;Root: HKLM; Subkey: "Software\Classes\SmilangScript\Shell\Open\Command"; Flags: uninsdeletekeyifempty; ValueType: string; ValueName: "RunInterpreter"; ValueData: "{app}\main.exe %1 %*"
;Root: HKLM; Subkey: "Software\Classes\.smiley"; Flags: uninsdeletekeyifempty; ValueType: string; ValueName: "Association"; ValueData: "SmilangScript"

[Run]
Filename: "{app}\register.bat"; Flags: runascurrentuser shellexec; Parameters: """{app}\main.exe"""

