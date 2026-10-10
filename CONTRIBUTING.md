# Contributing

Keep the launcher short, readable, and free of downloads, privilege escalation,
system-setting edits, credential access, and game binary patches.

For bug reports, use the issue form. State whether the failure occurs before
launch, at the title screen, during loading, playing, or saving. Report exact
messages and game/Windows versions. Do not upload copyrighted game files or
unredacted private logs.

For changes, describe the purpose and include tests. Run:

```powershell
python -m unittest discover -s tests -v
python tools/build_release.py
```

The automated tests do not launch the real game. Do not claim full gameplay
compatibility solely from those tests. Preserve CRLF line endings in `.bat` files.

Pull requests are welcome. Launcher changes should not require users to disable
UAC/antivirus, grant broad folder permissions, or permanently enable admin mode.
