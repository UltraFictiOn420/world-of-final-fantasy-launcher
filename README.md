# World of Final Fantasy Standard-User Launcher

A small, open-source Windows launcher for **World of Final Fantasy, Steam/PC**.
It starts `WOFF.exe` from the game folder with Windows 7 compatibility and
normal user privileges, without leaving a command window open after launch.

**Download:** [Latest release](https://github.com/UltraFictiOn420/world-of-final-fantasy-launcher/releases/latest)

**Status:** v1.0.0 community workaround, not an official Square Enix patch.
The initial launcher successfully started the game without the reported startup
crash on one user's computer; normal memory access was then verified.
The final launcher retains that launch method and removes the wait/pause on
success. Its checks and source have been tested, but the final launch itself,
long play sessions, saving, achievements, controller support, and other systems
have not all been verified. This is not a guaranteed fix for every crash.

## Quick start

1. Download `WoFF-Standard-User-Launcher-v1.0.0.zip` from the latest release and
   extract it to a temporary folder. Do not execute files from inside the ZIP.
2. In Steam, open the game's **Properties → Installed Files → Browse**.
3. Copy **`Launch-WoFF.bat`** beside **`WOFF.exe`**.
4. **Only if `steam_appid.txt` is absent**, copy the supplied plain-text
   `steam_appid.txt` there too. It contains only the game's Steam App ID,
   `552700`. Do not overwrite an existing file.
5. Save and close any running copy of the game. Keep Steam running normally,
   signed into an account that owns the game.
6. Double-click **`Launch-WoFF.bat` normally**. Do **not** use Run as administrator.

The command window briefly appears for checks, then closes when the game is
started. It does not wait for you to finish playing. If a check fails, the window
stays open with a readable explanation until you press a key.

You can make a desktop shortcut to `Launch-WoFF.bat`. An advanced alternative is
to pass the game folder as its first argument:

```bat
"C:\Tools\Launch-WoFF.bat" "D:\SteamLibrary\steamapps\common\WOFF"
```

## What you are downloading

There is **no installer, compiled executable, DLL, trainer, or cheat table** in
this package. The batch file is the entire launcher source. Right-click it and
choose **Edit**, or open it in Notepad, to inspect it before running it.

The launcher does exactly this:

1. Checks for `WOFF.exe`, the `resource` folder, and `steam_appid.txt`.
2. Uses a visible, plain-text PowerShell command to check whether its caller is
   elevated, whether WoFF is already running, and whether Steam is running.
3. Sets `__COMPAT_LAYER=RunAsInvoker WIN7RTM` in its own process environment.
4. Changes its working folder to the game folder and starts `WOFF.exe`.
5. Exits immediately after asking Windows to start the game.

It does **not** download anything, connect to a website, collect information,
install services, edit the registry, change file permissions, disable UAC or
antivirus, request admin privileges, patch game files, modify saves, or bypass
Steam ownership/DRM checks. Steam and the game retain their normal behavior and
may make their usual network connections and file writes.

The optional App ID text file identifies the game to Steam; it does not provide
a license. You still need a legitimate copy and the Steam client.

No security software can be promised to accept a script. If Windows or your
antivirus warns about it, **do not disable your protection to run it**. Inspect
the source and checksum, or report the warning. This project is not digitally
signed and has no claimed antivirus certification. See [Security](SECURITY.md).

## Why this might help

The tested game's executable manifest requests `asInvoker` (the caller's
privileges). The user's compatibility settings separately forced administrator
mode. The original launch experiment applied `RunAsInvoker WIN7RTM` for just one
launch, without changing those saved settings, and the user reported startup
success. `RunAsInvoker` does not grant permissions: operations needing actual
administrator access can still fail.

Launching from the correct folder may also avoid missing-resource problems.
A player reported observing WoFF looking for `resource` in `Steamworks Shared`
when launched through Steam, but in the correct folder when launched directly.
That is a [first-hand community report](https://steamcommunity.com/app/552700/discussions/0/3421061982941966857/?ctp=17),
not proof that every affected installation has the same cause.

Valve documents that Steam API initialization uses the current working directory
when locating `steam_appid.txt` and can fail if Steam and the game use different
privilege levels. [Steamworks API documentation](https://partner.steamgames.com/doc/sdk/api)

## Compatibility and limitations

- Intended for the Windows Steam edition; the locally inspected x64 executable
  reports version **2.0.0.0**. MAXIMA DLC-specific behavior is not separately verified.
- Windows 11 was used for the reported startup success. Other Windows versions
  and PCs need testing.
- Requires built-in Windows PowerShell for read-only preflight checks. It does
  not change PowerShell execution policy or run a downloaded PowerShell script.
- Does not repair corrupt installs, driver issues, missing runtime components,
  save corruption, or every possible launch/runtime crash.
- A successful launch does not prove that loading or saving works. Back up saves
  before troubleshooting, then check those actions yourself.
- Starting directly can affect Steam Input, overlays, achievements, or cloud-save
  behavior depending on the installation. Those features are not guaranteed.
- Changing Windows' saved compatibility settings is not necessary for this
  launcher. Keep your previous working launch method as a fallback.

## Troubleshooting

| Message or symptom | What to do |
| --- | --- |
| `WOFF.exe` not found | Place the launcher in the actual game folder, not the desktop. |
| `resource` missing | Check the game installation; do not copy resources into unrelated Steam folders. |
| `steam_appid.txt` missing | Copy the included App ID file only if no existing file is present. |
| Elevated caller | Open the launcher normally from a non-admin desktop session. |
| WoFF already running | Save and close the game normally; the launcher never kills it. |
| Steam missing | Open Steam normally and sign into the account that owns the game. |
| Check/start failed | Note the exact message; do not disable security software or change permissions broadly. |
| Game opens, then crashes | Return to your old method and report when the crash occurred. |
| Old test-launcher window still open | The new launcher cannot close an old window retroactively. Close the old window after the old game session has ended. |

For reports, use [Issues](https://github.com/UltraFictiOn420/world-of-final-fantasy-launcher/issues).
Include Windows version, game version, the exact message, and whether loading
and saving worked. Review logs before posting: remove account names, personal
paths, save data, and other private details. Use the provided issue forms.

## Verify the download

Each release includes SHA-256 checksums. In PowerShell, run:

```powershell
Get-FileHash '.\WoFF-Standard-User-Launcher-v1.0.0.zip' -Algorithm SHA256
```

Compare the result with the release's ZIP checksum. The archive also includes
`CHECKSUMS.sha256` for its contents. Checksums confirm matching bytes; they are
not a substitute for inspecting the source or an independent security review.

## Remove it

Delete `Launch-WoFF.bat` and its shortcut. If you added the supplied App ID file,
you may also remove **that newly added copy**; leave any pre-existing file alone.
There are no installed components or launcher-created registry changes to undo.

## Source and license

Published by **UltraFictiOn420**.
The launcher code is original; community troubleshooting reports are credited
above. [MIT License](LICENSE). This project is unaffiliated with Square Enix,
Valve, Microsoft. World of Final Fantasy and related names belong to
their respective owners. No game binaries, game resources, or saves are distributed.

See [Changelog](CHANGELOG.md), [Testing](docs/TESTING.md),
[Contributing](CONTRIBUTING.md), and [Repository map](docs/PROJECT_MAP.md).
