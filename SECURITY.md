# Security and transparency

The release is readable source, not a compiled program. Inspect `Launch-WoFF.bat`
in a text editor before running it. Check the release's SHA-256 values if desired.

The launcher uses built-in Windows commands and a plain-text PowerShell command
for read-only checks. It does not download or execute remote code, add startup
entries, access credentials, collect telemetry, modify the registry, change
permissions, request elevation, or disable any protection. The game and Steam
are separate programs and continue their normal activity.

`RunAsInvoker` asks for the caller's existing privileges. It neither grants admin
rights nor makes an operation succeed when normal permissions prohibit it.
`WIN7RTM` requests Windows 7 compatibility behavior only for the launched process.
Both flags are process-local, not permanent registry settings.

This project has no digital signature, independent security audit, or claimed
antivirus certification. A checksum only identifies a file. Do not ignore or
disable security warnings because a README describes software as safe.

If you find a security issue, open a minimal issue describing the problem without
credentials, exploit payloads, or private logs. For a sensitive vulnerability,
request a private reporting channel before sharing details publicly.

No game files or third-party executables belong in releases. Official releases
should contain only the launcher, App ID text, license, documentation, and checksums.
