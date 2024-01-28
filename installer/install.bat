md %USERPROFILE%\Smilang
COPY main.exe %USERPROFILE%\Smilang
assoc .smiley=SmilangScript
ftype SmilangScript="%USERPROFILE%\Smilang\main.exe" %1 %*