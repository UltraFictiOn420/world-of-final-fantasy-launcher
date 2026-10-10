# v1.0.0 - Standard-User Launcher

Initial public release of a small, open-source Windows launcher for the Steam
edition of **World of Final Fantasy**.

## Download and install

Download **WoFF-Standard-User-Launcher-v1.0.0.zip** below and extract it.
Copy **Launch-WoFF.bat** beside **WOFF.exe**. Only if no `steam_appid.txt` exists,
copy the supplied App ID text file there too. Keep Steam running and double-click
the launcher normally, **not as administrator**.

The command window closes immediately after the game is started. Errors remain
visible until you press a key. No game is stopped, patched, or overwritten.

## What it does

- Starts from the game's own folder.
- Applies `RunAsInvoker WIN7RTM` only to that launch.
- Refuses an elevated caller, missing files, an already-running game, or missing Steam.
- Makes no persistent system-setting changes and contains no downloads.

## Transparency

The entire launcher is a readable `.bat` file. No installer, executable, DLL,
trainer, or cheat table is included. Source, MIT license, security explanation,
and checksums are included. Inspect the source before running it; don't disable
security software if you see a warning.

## Testing and limits

The original launch method successfully opened the game on one user's Windows
11 PC, and normal game-memory access was verified afterward. The final launcher
retains that method and removes the lingering command window. Automated checks
do not launch a real game. The final build's full gameplay, saving, DLC, Steam
features, and other PCs still need verification. This is a community workaround,
not an official patch or guaranteed universal fix.

Back up saves before troubleshooting. Delete the launcher to return to your old
method; no registry cleanup is required.

Use the release's ZIP checksum file to verify the archive, and the included
`CHECKSUMS.sha256` for its contents. Checksums verify bytes, not security.

For help, read the repository README and open an issue with the exact failure
and Windows/game versions. Remove private details from any logs.
